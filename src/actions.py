from pandas import DataFrame
from src.model import Model

class Actions:

    def __init__(self, frame: DataFrame, model: Model):
        self.frame = frame
        self.model = model

    def get_notes_by_student(self, student_id: int) -> DataFrame:
        return (self.frame
                .query(f'student_id == {student_id}')
        )

    def calc_chance_disapprove(self, student_id: int) -> float:
        return self.model.predict(3)
