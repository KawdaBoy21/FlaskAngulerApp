from flask import Flask, request, jsonify
from .entities.entity import Session, engine, Base
from .entities.exams import Exam, ExamSchema
from flask_cors import CORS
from .auth import AuthError, requires_auth


# generate database schema
Base.metadata.create_all(engine)


# creating Flask app
app = Flask(__name__)
CORS(app)

# sess = Session()
# check for existing data
# exams = sess.query(Exam).all()

# if len(exams) == 0:
#     # create and persist dummy exam
#     python_exam = Exam("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
#     sess.add(python_exam)
#     sess.commit()
#     sess.close()
#
#     # reload exams
#     exams = sess.query(Exam).all()
#
# # show existing exams
# print('### Exams:')
# for exam in exams:
#     print(f'({exam.id}) {exam.title} - {exam.description}')


@app.route('/exams', methods=['GET', 'POST'])
# @requires_auth
def get_exam():

    if request.method == 'GET':

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

    elif request.method == 'POST':

        # mount exam object
        posted_exam = ExamSchema(only=('title', 'description'))\
                        .load(request.get_json())

        exam = Exam(**posted_exam.data, created_by="HTTP Post Request")

        # presist exam
        session = Session()
        session.add(exam)
        session.commit()

        # returnig created exam
        new_exam = ExamSchema().dump(exam).data
        session.close()
        return jsonify(new_exam), 201


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

