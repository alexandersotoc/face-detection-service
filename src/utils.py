import uuid
from os import path, remove

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(request, upload_folder):
    if 'file' not in request.files:
        return None

    file = request.files['file']

    if file.filename == '':
        return None

    if file and allowed_file(file.filename):
        _, file_extension = path.splitext(file.filename)
        filename = uuid.uuid4().hex + file_extension
        file.save(path.join(upload_folder, filename))
        return filename
    else:
        return None            

def delete_file(filename, upload_folder):
    filepath = path.join(upload_folder, filename)
    if path.exists(filepath):
        remove(filepath)