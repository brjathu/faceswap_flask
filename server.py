from flask import Flask, render_template, request, send_from_directory
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import os

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'uploads/'
configure_uploads(app, photos)


@app.route('/new', methods=['GET', 'POST'])
def new():
    os.system("sudo rm uploads/a.jpg")
    os.system("sudo rm uploads/b.jpg")
    return render_template('new.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        print(filename)
        return filename
    return render_template('index.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    os.system("sudo /home/brjathu/anaconda3/envs/virtualX/bin/python faceswap.py  uploads/a.jpg uploads/b.jpg")
    return render_template('process.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    out = os.path.join(app.root_path, "results")
    print(out)
    return send_from_directory(directory=out, filename="output.jpg")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
    # app.run(debug=True)
