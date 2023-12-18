from flask import Flask, request, jsonify, send_file
#from flask_pymongo import PyMongo
#from werkzeug.utils import secure_filename
#from gridfs import GridFS
#from bson import ObjectId

app = Flask(__name__)

# In-memory storage for simplicity (not recommended for production)
uploaded_files = {}


# Define a decorator function to check if the user is an Ops User
def ops_user_required(f):
    def wrapper(*args, **kwargs):
        user_type = request.headers.get('User-Type')
        if user_type == 'Ops':
            return f(*args, **kwargs)
        else:
            return jsonify({'error': 'Unauthorized'}), 401

    return wrapper


@app.route('/login', methods=['POST'])
def login():
    # Placeholder for authentication logic
    # You may want to implement a proper authentication mechanism
    return jsonify({'message': 'Login successful'})


@app.route('/upload', methods=['POST'])
@ops_user_required
def upload_file():
    allowed_extensions = {'pptx', 'docx', 'xlsx'}
    file = request.files.get('file')

    if file and file.filename.split('.')[-1] in allowed_extensions:
        # Save the file in memory (you should implement proper file storage)
        uploaded_files[file.filename] = file.read()
        return jsonify({'message': 'File uploaded successfully'})
    else:
        return jsonify({'error': 'Invalid file type or no file provided'}), 400

# Configure MongoDB Atlas
#app.config['MONGO_URI'] = 'your_mongodb_uri'
#mongo = PyMongo(app)

# GridFS setup for handling file storage
#fs = GridFS(mongo.db)

#@app.route("/")
#def home():
 #   return "Hello, Flask!"

# Authentication function
#def authenticate(username, password):
 #   ops_user = mongo.db.ops_users.find_one({'username': username, 'password': password})
  #  return ops_user is not None


# Ops User Endpoints
#@app.route('/ops/login', methods=['POST'])
#def ops_login():
 #   data = request.json
  #  username = data.get('username')
   # password = data.get('password')
    #if authenticate(username, password):
     #   # Implement JWT token generation here if needed
      #  return jsonify({'message': 'Ops User Login Successful'})
    #return jsonify({'message': 'Ops User Login Failed'}), 401


#@app.route('/ops/upload', methods=['POST'])
#def ops_upload():
 #   # Check if the request contains a file
  #  if 'file' not in request.files:
   #     return jsonify({'message': 'No file part'}), 400

    #file = request.files['file']

    # Check if the file is of allowed type
   # allowed_extensions = {'pptx', 'docx', 'xlsx'}
    #if file.filename.split('.')[-1].lower() not in allowed_extensions:
     #   return jsonify({'message': 'File type not allowed'}), 400

    # Save the file to MongoDB using GridFS
    #file_id = fs.put(file, filename=secure_filename(file.filename))
    #return jsonify({'message': 'File Uploaded Successfully', 'file_id': str(file_id)})


# Client User Endpoints
# Include client user endpoints as needed



if __name__ == '__main__':
    app.run(debug=True)
