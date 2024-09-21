import os
from pandas import read_csv

class Extract:

    def __init__(self):
        self.disciplines = read_csv(self.__get_path__('disciplines.csv'))
        self.notes = read_csv(self.__get_path__('notes.csv'))
        self.students = read_csv(self.__get_path__('students.csv'))
        self.years = read_csv(self.__get_path__('years.csv'))

    def __get_path__(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return str(os.path.join(current_dir, '..', 'files', filename))
