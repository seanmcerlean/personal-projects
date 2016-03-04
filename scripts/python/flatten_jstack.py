"""
Script to generate flattened java stack traces suitable for generating flamegraphs
See http://www.brendangregg.com/flamegraphs.html for details
"""
import argparse
import re
from collections import Counter


class JstackFlattener:

    def __init__(self, filename, include_threadname=False, thread_states=('RUNNABLE',)):
        self._include_threadname = include_threadname
        self._thread_states = thread_states

        self._stacks = []
        self._flat_stacks = []
        self._rolled_stacks = []

        with open(filename) as stack_file:
            self.original_file = stack_file.read()

    def _get_next_stack(self):
        """
        Generator to get the next stack in the original file and processes it into a dictionary
        :return: A stack dictionary of form stack = {'lines': [], 'name': '', 'state': ''}
        """
        pattern = r'\".+\n +java.+\n(?:\s+at.+\n|\s+-.+\n)*'
        for string_stack in re.findall(pattern, self.original_file):
            stack = self._process_stack(string_stack)
            yield stack

    @staticmethod
    def _process_stack(stack_string):
        """
        Process a supplied java stack and extracts the details into a dictionary
        :param stack_string: The stack to be processed as a string
        :return: A stack dictionary in the form {'lines': [], 'name': '', 'state': ''}
        """
        stack = {'lines': [], 'name': '', 'state': ''}

        for line in stack_string.split('\n'):
            if line.startswith('"'):
                stack['name'] = line.split('"')[1]
            elif line.lstrip().startswith('at'):
                at_function = line.lstrip().split('(')[0]
                function = at_function.split('at ')[1]
                stack['lines'].insert(0, function)
            elif line.lstrip().startswith('java.lang.Thread.State: '):
                stack['state'] = line.lstrip().split(': ')[1]

        return stack

    def extract_stacks(self):
        """
        Extracts all stacks from a stack into a dictionary and places them in self.stacks
        :return: None
        """
        self._stacks = [stack for stack in self._get_next_stack()]
    
    def _flatten_stack(self, stack):
        """
        Flattens a supplied stack so that all stack lines appear on 1 line seprated by 1
        The line stacks with the bottom method, normally a run method
        :param stack: Stack dictionary to be processed
        :return: Flat stack string
        """
        flattened_stack = ';'.join(stack['lines'])
        if self._include_threadname:
            flattened_stack = stack['name'] + ';' + flattened_stack
        return flattened_stack

    def flatten_stacks(self):
        """
        Flatten all stacks in self_stacks that are in one of the self_thread_states (default is RUNNABLE)
        and add them to the self.flat_stacks dictionary
        :return: None
        """
        self._flat_stacks = []
        for stack in self._stacks:
            if stack['state'] in self._thread_states and stack['lines']:
                flat_stack = self._flatten_stack(stack)
                self._flat_stacks.append(flat_stack)
 
    def rollup_stacks(self):
        """
        Roll up all stacks in self._flat_stacks so that multiple stacks with the same line appear in the form
        method1;method2;method3;method4:n where n is rthe number of times the stack appears in self._flat_stacks
        :return: None
        """
        self._rolled_stacks = []
        counts = Counter(self._flat_stacks)
        rolled_stacks = [key + ':' + str(value) for key, value in counts.iteritems()]
        sorted(rolled_stacks, key=lambda x: int(re.search(r'\d+$', x).group()))
        self._rolled_stacks = rolled_stacks

    def print_file(self):
        """
        Prints the original file with out changes
        :return: None
        """
        print(self.original_file)
    
    def print_stacks(self, filt=None):
        """
        Prints the name of each stack followed by the functions called in each stack on separate lines
        :param filt: A filter string that will cause a stack trace to be ignored if it appears in the trace
        :return: None
        """
        for stack in self._stacks:
            pr_stack = stack['name'] + '\n'.join(stack['lines']) + '\n'
            if (filt is None) or (filt is not None and filt not in pr_stack):
                print(pr_stack)

    @staticmethod
    def _print_flat_stack_list(stack_list, filt):
        """
        Prints all flat stacks in stack_list on separate lines
        :param stack_list: A list of flat (single line) stack traces
        :param filt: A filter string that will cause a stack trace to be ignored if it appears in the trace
        :return: None
        """
        pr_stacks = [stack for stack in stack_list if stack]

        if filt is not None:
            pr_stacks = [stack for stack in pr_stacks if filt not in stack]

        print('\n'.join(pr_stacks)) 

    def print_flattened_stacks(self, filt=None):
        """
        Prints all stacks in self._flat_stacks on separate lines
        :param filt: A filter string that will cause a stack trace to be ignored if it appears in the trace
        """
        self._print_flat_stack_list(self._flat_stacks, filt)

    def print_rolled_stacks(self, filt=None):
        """
        Prints all stacks in self._rolled_stacks on separate lines
        :param filt: A filter string that will cause a stack trace to be ignored if it appears in the trace
        """
        self._print_flat_stack_list(self._rolled_stacks, filt)

if __name__ == "__main__":
    def parse_arguments():
        parser = argparse.ArgumentParser(description='Flatten and roll up Jstacks suitable for making flamegraphs')
        parser.add_argument('file', help='File to process')
        parser.add_argument(
            '--include_threadname', dest='include_threadname', action='store_true',
            help='Whether or nor to include threadnames in flat stacks'
        )
        parser.add_argument(
            '--thread_states', type=tuple, help='Thread states to be included in flat stacks'
        )
        parser.add_argument('--print_type', help='Type of stacks to print', choices=('rolled', 'flat', 'full') )
        parser.set_defaults(include_thread_name=False, thread_states=('RUNNABLE',), print_type='rolled')
        return parser.parse_args()

    args = parse_arguments()

    flattener = JstackFlattener(args.file, args.include_threadname, args.thread_states)
    flattener.extract_stacks()
    flattener.flatten_stacks()
    flattener.rollup_stacks()
    if args.print_type == 'full':
        flattener.print_stacks()
    elif args.print_type == 'flat':
        flattener.print_flattened_stacks()
    elif args.print_type == 'rolled':
        flattener.print_rolled_stacks()
