#!/usr/bin/python
"""
Simple script that parse files with flat core dumps in the form
method1;method2;method3;methodn,THREAD_STATE
Just as an example to mess around with spark. Assumes you are running against the pyspark rather than python
"""

import argparse
import os
import pprint
from pyspark import SparkContext

def parse_arguments():
    """
    Parse the arguments passed to the script
    :return: argparse object holding arguments
    """
    parser = argparse.ArgumentParser(description='Roll Up and simple stats for flat core files')
    parser.add_argument('file', help='File to process')
    parser.add_argument(
        '--spark_home', type=str, help='Home Directory for Apache Spark'
    )
    parser.add_argument(
        '--thread_states', type=tuple, help='Thread states to be included in flat stacks'
    )
    parser.add_argument(
        '--histogram', choices=('stacks', 'functions'), help='Histogram to show - stacks or functions'
    )
    parser.add_argument(
        '--max', type=int, help='Max values to show'
    )
    parser.set_defaults(spark_home='/home/smcerlean/Downloads/spark-1.6.0-bin-hadoop2.6', thread_states=('RUNNABLE',),
                        histogram='functions', max=None)
    return parser.parse_args()

def calculate_stack_counts(stack_rd):
    """
    Calculates a histogram of the stack traces contained in the file
    :param stack_rd: RDD of stacks in form [stack, state]
    :return: Sorted RDD of stacks in form (count, stack)
    """
    return stack_rd.map(lambda x: (x[0], 1)) \
                   .reduceByKey(lambda x, y: x + y) \
                   .map(lambda x: (x[1],x[0])) \
                   .sortByKey(False)

def calculate_function_counts(stack_rd):
    """
    Calculates a histogram of the functions contained in the file
    Functions in a stack are separated by the ; character
    :param stack_rd: RDD of stacks in form [stack, state]
    :return: Sorted RDD of stacks in form (count, stack)
    """
    return stack_rd.flatMap(lambda x: x[0].split(';')) \
                   .map(lambda x: (x, 1)) \
                   .reduceByKey(lambda x, y: x + y) \
                   .map(lambda x: (x[1],x[0])) \
                   .sortByKey(False)

if __name__ == "__main__":
    args = parse_arguments()

    # Took out the final line of the pyspark script and sourced it, but couldn't get a python script to work without this
    os.environ["SPARK_HOME"] = args.spark_home
    sc = SparkContext('local', 'Flat Core File App')

    raw_data = sc.textFile(args.file)

    stack_traces = raw_data.map(lambda x: x.split(',')) \
                           .filter(lambda x: x[0]) \
                           .filter(lambda x: x[1] in args.thread_states)


    if args.histogram == 'stacks':
        calculation_function = calculate_stack_counts
    else:
        calculation_function = calculate_function_counts

    aggregate_data = calculation_function(stack_traces)

    pp = pprint.PrettyPrinter()
    if args.max is None:
        pp.pprint(aggregate_data.take(aggregate_data.count()))
    else:
        pp.pprint(aggregate_data.take(args.max))
