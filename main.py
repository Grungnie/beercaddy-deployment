from flask import Flask, request, Response, g
from threading import Thread
import os
import subprocess
import signal
import shutil

app = Flask(__name__)
GIT_URL = 'https://github.com/Grungnie/beercaddy'
PROGRAM_ROOT = '/home/pi'
REPO_NAME = 'beercaddy'

@app.route("/build", methods=['POST'])
def build():
    request_json = request.get_json()

    if 'repository' in request_json and 'url' in request_json['repository'] and request_json['repository']['url'] == GIT_URL:
        Thread(target=build_app).start()
    else:
        print('{} is not a valid git url'.format(request.get_json()['repository']['url']))

    # return a response
    resp = Response()
    resp.status_code = 202
    return resp


def build_app():
    # Kill current python process - how???
    try:
        os.killpg(os.getpgid(g.sleeping.pid), signal.SIGTERM)
    except Exception as e:
        print('Kill Exception')
        print(e)

    # cd to root dir
    os.chdir(PROGRAM_ROOT)

    # blow away program
    try:
        shutil.rmtree('{}/{}'.format(PROGRAM_ROOT, REPO_NAME))
    except:
        print('No folder')

    # clone repo
    subprocess.call('git clone {}'.format(GIT_URL), shell=True)

    # run the sh script
    with app.app_context():
        g.sleeping = subprocess.Popen('{0}/beercaddy-deployment/build.sh {0}/{1}'.format(PROGRAM_ROOT, REPO_NAME),
                                      shell=True,
                                      stdout=subprocess.PIPE,
                                      preexec_fn=os.setsid)

if __name__ == '__main__':
    app.run(debug=True)

