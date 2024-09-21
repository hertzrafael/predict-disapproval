from numpy import nan
from pandas import DataFrame

from src.extract import Extract

class Transform:

    def __init__(self, extract: Extract):
        self.extract = extract
        self.result = None

    def init(self):
        merged_frame = (self.extract.notes
            .merge(self.extract.disciplines, how='left', left_on='discipline_id', right_on='id')
            .drop(columns=['id_y'])
            .rename(columns={'id_x': 'id', 'name': 'discipline_name'})
            .merge(self.extract.students, how='left', left_on='student_id', right_on='id')
            .drop(columns=['id_y'])
            .rename(columns={'id_x': 'id', 'name': 'student_name'})
            .merge(self.extract.years, how='left', left_on='year_id', right_on='id')
            .drop(columns=['id_y'])
            .rename(columns={'id_x': 'id', 'name': 'year_name'})
        )

        self.__check_na__(merged_frame)

    def __check_na__(self, df: DataFrame):
        mean_count = DataFrame(df.groupby('student_id')['discipline_id'].value_counts()).reset_index()
        print(mean_count)

        self.result = df