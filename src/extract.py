import os
from pandas import read_csv

def extract_all():
    disciplines = read_csv(__get_path__('disciplines.csv'))
    notes = read_csv(__get_path__('notes.csv'))
    students = read_csv(__get_path__('students.csv'))
    years = read_csv(__get_path__('years.csv'))

    return (notes
        .merge(disciplines, how='left', left_on='discipline_id', right_on='id')
        .drop(columns=['id_y'])
        .rename(columns={'id_x': 'id', 'name': 'discipline_name'})
        .merge(students, how='left', left_on='student_id', right_on='id')
        .drop(columns=['id_y'])
        .rename(columns={'id_x': 'id', 'name': 'student_name'})
        .merge(years, how='left', left_on='year_id', right_on='id')
        .drop(columns=['id_y', 'year_id'])
        .rename(columns={'id_x': 'id', 'name': 'year_name'})
    )

def __get_path__(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return str(os.path.join(current_dir, '..', 'files', filename))
