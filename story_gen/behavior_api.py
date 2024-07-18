
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from behavior_parser import sentence_parser

app = Flask(__name__)
CORS(app)

@app.route('/storyParser', methods = ['POST'])
def story_parser():
    data = json.loads(request.data)
    res = sentence_parser(data["Story"]) # might need to be data[...]
    return jsonify(res)


if __name__ == '__main__':
   app.run(port=5000)
