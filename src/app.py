from extract import extract_all
from actions import Actions
from src.model import Model

def run():
    model = Model()
    frame = extract_all()

    actions = Actions(frame, model)
    student_notes = actions.get_notes_by_student(1)

    print(student_notes)

if __name__ == '__main__':
    run()