from extract import Extract
from actions import Actions
from src.model import Model
from src.transform import Transform

def run():
    model = Model()
    extract = Extract()
    transform = Transform(extract)
    transform.init()

    result = transform.result
    print(result)

    #actions = Actions(frame, model)
    #student_notes = actions.calc_chance_disapprove(0, 9)

    #print(student_notes)

if __name__ == '__main__':
    run()