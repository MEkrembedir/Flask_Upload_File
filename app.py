from flask import *
import os
import tkinter as tk
from tkinter import filedialog

app = Flask(__name__)

# Home Page/Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Dosya yükleme/Upload File
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join('upload', filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

