from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.exams import Exam, ExamSchema

# generate database schema
Base.metadata.create_all(engine)


# creating Flask app
app = Flask(__name__)

# check for existing data
# exams = session.query(Exam).all()
#
# if len(exams) == 0:
#     # create and persist dummy exam
#     python_exam = Exam("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
#     session.add(python_exam)
#     session.commit()
#     session.close()
#
#     # reload exams
#     exams = session.query(Exam).all()

# show existing exams
# print('### Exams:')
# for exam in exams:
#     print(f'({exam.id}) {exam.title} - {exam.description}')


@app.route('/exams')
def get_exam():

    # starting session
    session = Session()

    # fetching from the database
    exam_object = session.query(Exam).all()

    # transforming into JSON-serializable objects
    scema = ExamSchema(many=True)
    exams = scema.dump(exam_object)

    # serializing as JSON
    session.close()
    return jsonify(exams.data)


@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description'))\
                    .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP Post Request")

    # presist exam
    session = Session()
    session.add(exam)
    session.commit()

    # returnig created exam
    new_exam = ExamSchema.dump(exam).data
    session.close()
    return jsonify(new_exam), 201

