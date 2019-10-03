import json
from flask import Flask, render_template, request
from werkzeug import secure_filename
from serve import get_cursive_api  
import os

# create an instance of Flask
app = Flask(__name__)

UPLOAD_FOLDER = "cursive/sample_images/"
MAX_CONTENT_PATH = 5* 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_PATH'] = MAX_CONTENT_PATH
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return "Ritesh Cursive API :: Up and running!"

# load our pre-trained model & function
cursive_api = get_cursive_api()

@app.route('/upload')
def upload():
   return render_template('upload.html')
    
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       filename = (secure_filename(f.filename))
#       f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#       return 'file uploaded successfully'


# Define a post method for our API.
@app.route('/cursive_recognize', methods=['POST'])
def cursive_recognize():
    """ 
    Takes in a json file, extracts the keywords &
    their indices and then returns them as a json file.
    """
    # the data the user input, in json format
    if request.method == 'POST':
        f = request.files['file']
        filename = (secure_filename(f.filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        input_data = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # use our API function to get the keywords
        output_data = cursive_api(input_data)
        print(output_data)
        
        response = json.dumps(output_data)
        print("Console check:: ", response)

        # Deleting all stored files
        filelist = [ f for f in os.listdir(UPLOAD_FOLDER) if f == filename ]
        for f in filelist:
            os.remove(os.path.join(UPLOAD_FOLDER, f))
        filelist = os.listdir("cursive/result/characters/")
        for f in filelist:
            os.remove(os.path.join("cursive/result/characters/", f))
        filelist = os.listdir("cursive/result/data/")
        for f in filelist:
            os.remove(os.path.join("cursive/result/data/", f))
        filelist = os.listdir("cursive/result/resized_images/")
        for f in filelist:
            os.remove(os.path.join("cursive/result/resized_images/", f))
        filelist = os.listdir("cursive/result/words/")
        for f in filelist:
            os.remove(os.path.join("cursive/result/words/", f))
        print("Delete check:: Done")
        # return our json file
        return response