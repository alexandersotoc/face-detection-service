from flask_api import status
from flask import Flask, request, jsonify

from src.face_detection import find_faces
from src.utils import upload_file, delete_file

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5mb

@app.route('/face-detection', methods=['POST'])
def face_detection():
    filename = upload_file(request, UPLOAD_FOLDER)
    if filename:
        try:
            result = find_faces(filename)
            delete_file(filename, UPLOAD_FOLDER)
            return result
        except:
            delete_file(filename, UPLOAD_FOLDER)
            return { 'message': "Bad request" }, status.HTTP_400_BAD_REQUEST
    else:
        return { 'message': "Bad request" }, status.HTTP_400_BAD_REQUEST

@app.errorhandler(404)
def page_not_found(error):
    return { 'message': 'Not found' }, status.HTTP_404_NOT_FOUND

if __name__ == "__main__":
    app.run(port=8900, debug=True)