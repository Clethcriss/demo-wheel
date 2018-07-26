from flask import Flask, render_template
from os import path
import os

extra_dirs = ['./templates',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        extra_files=extra_files,
        host='0.0.0.0',
        port=8000,
        debug=True
    )
