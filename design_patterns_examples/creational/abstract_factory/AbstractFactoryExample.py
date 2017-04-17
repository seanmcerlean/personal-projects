import abc
import csv
import json
import os


class AbstractMarkupFactory(object, metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def createFileReader(self):
        NotImplementedError('create file reader is not implemented')

    def createDBReader(self):
        NotImplementedError('create DB reader is not implemented')


class AbstractFileReader(object, metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def open_file(self, filename):
        NotImplementedError('open file is not implemented')

    @abc.abstractclassmethod
    def print_file(self):
        NotImplementedError('print file is not implemented')


class CSVReaderFactory(AbstractMarkupFactory):
    def createFileReader(self):
        return FileReaderFactory.createReader('csv')

    def createDBReader(self):
        pass


class JSONReaderFactory(AbstractMarkupFactory):
    def createFileReader(self):
        return FileReaderFactory.createReader('json')

    def createDBReader(self):
        pass


class FileReaderFactory:
    @staticmethod
    def createReader(type):
        if type == "csv":
            return CSVFileReader()
        elif type == "json":
            return JSONFileReader()
        else:
            NotImplementedError("This type is not implemented")


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



if __name__ == "__main__":
    readerFactory = CSVReaderFactory()
    reader = readerFactory.createFileReader()
    reader.open_file(os.path.dirname(__file__) + "/test.csv")
    reader.print_file()

    readerFactory = JSONReaderFactory()
    reader = readerFactory.createFileReader()
    reader.open_file(os.path.dirname(__file__) + "/test.json")
    reader.print_file()