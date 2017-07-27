from flask import Flask, request, Response
from json import dumps

app = Flask(__name__)

@app.route("/build", methods=['POST'])
def build():
    print(dumps(request.get_json()))

    resp = Response()
    resp.status_code = 202
    return resp


if __name__ == '__main__':
    app.run(debug=True)

