
import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from behavior_parser import sentence_parser
from behavior_gen import SarBehaviorGenerator, State

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route('/get-intents', methods = ['POST'])
@cross_origin()
def get_intents_from_text():
    """Parse text and break it up into sentences with attached intent and emotions

    Returns:
        Array of:   sentences with intent and emotion
            intent: the intent for the sentence
            content: the content of the sentence
            emotion: the emotion to express when verbalizing the sentence
    """
    data = json.loads(request.data)
    res = sentence_parser(data["text"]) 
    return jsonify(res)

@app.route('/get-plan', methods = ['POST'])
@cross_origin()
def get_plan_from_text():
    data = json.loads(request.data)
    sentences = sentence_parser(data["text"]) 

    sbg = SarBehaviorGenerator(None)
    state1 = State("interactive")
    state1.add(["gaze","center"])
    state1.add(["rapport","low"])
    state1.add(["affect","neutral"])

    intents = [[x["intent"], x["content"], x["emotion"]] for x in sentences]
    plan = sbg.planBehaviorFor(intents, state1)
    return jsonify({
        "sentences": sentences,
        "plan": plan
    })


if __name__ == '__main__':
   app.run(port=5000)
