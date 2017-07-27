from flask import Flask, request, Response, g
import os
import subprocess
import signal

app = Flask(__name__)
GIT_URL = 'git://github.com/Grungnie/beercaddy.git'
PROGRAM_ROOT = '/home/skippy/PycharmProjects'
REPO_NAME = 'beercaddy'

@app.route("/build", methods=['POST'])
def build():

    if request.get_json()['repository']['url'] == GIT_URL:
        # Kill current python process - how???
        try:
            os.killpg(os.getpgid(g.sleeping.pid), signal.SIGTERM)
        except:
            print('Looks like nothong was running')

        # cd to root dir
        os.chdir(PROGRAM_ROOT)

        # blow away program
        subprocess.call('rm -R {}'.format(REPO_NAME), shell=True)

        # clone repo
        subprocess.call('git clone {}'.format(GIT_URL), shell=True)

        # cd into dir
        os.chdir('{}/{}'.format(PROGRAM_ROOT, REPO_NAME))

        # create virtualenv
        subprocess.call('virtualenv -p python3 venv', shell=True)
        subprocess.call('source venv/bin/activate', shell=True)

        # install requiremnets.txt
        subprocess.call('pip install requirements.txt', shell=True)

        # run program
        g.sleeping = subprocess.Popen('python main.py', shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

    # return a response
    resp = Response()
    resp.status_code = 202
    return resp


if __name__ == '__main__':
    app.run(debug=True)

