import abc
import csv
import json
import os


class AbstractFileReader(object, metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def open_file(self, filename):
        NotImplementedError('open file is not implemented')

    @abc.abstractclassmethod
    def print_file(self):
        NotImplementedError('print file is not implemented')


class CSVFileReader(AbstractFileReader):

    def __init__(self):
        self._reader = None

    def open_file(self, filename):
        csvfile = open(filename)
        self._reader = csv.reader(csvfile)

    def print_file(self):
        for line in self._reader:
            print(line)


class JSONFileReader(AbstractFileReader):
    def __init__(self):
        self._reader = None

    def open_file(self, filename):
        jsonfile = open(filename)
        self._json_object = json.load(jsonfile)

    def print_file(self):
        for key in self._json_object:
            print(key + ': ' + self._json_object[key])


class FileReaderFactory:
    @staticmethod
    def createReader(type):
        if type == "csv":
            return CSVFileReader()
        elif type == "json":
            return JSONFileReader()
        else:
            NotImplementedError("This type is not implemented")


if __name__ == "__main__":
    reader = FileReaderFactory.createReader("csv")
    reader.open_file(os.path.dirname(__file__) + "/test.csv")
    reader.print_file()

    reader = FileReaderFactory.createReader("json")
    reader.open_file(os.path.dirname(__file__) + "/test.json")
    reader.print_file()