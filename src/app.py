from extract import extract_all
from actions import Actions

def run():
    frame = extract_all()

    actions = Actions(frame)
    student_notes = actions.get_notes_by_student(1)

    print(actions)

if __name__ == '__main__':
    run()