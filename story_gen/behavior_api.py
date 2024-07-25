
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from behavior_parser import sentence_parser
from .. import behavior_gen


app = Flask(__name__)
CORS(app)

@app.route('/storyParser', methods = ['POST'])
def story_parser():
    data = json.loads(request.data)
    res = sentence_parser(data["Story"]) 
    return jsonify(res)

@app.route('/storyBehaviors', methods = ['POST'])
def story_parser():
    data = json.loads(request.data)
    #TODO: Instantiate this just once, not on every call
    sbg = behavior_gen.SarBehaviorGenerator(None)
    state1 = behavior_gen.State("interactive")
    state1.add(["gaze","center"])
    state1.add(["rapport","low"])
    state1.add(["affect","neutral"])
    #TODO: set goal affects?
    intents = [[x["intent"], x["content"], x["emotion"]] for x in data]
    plan = sbg.planBehaviorFor(intents, state1)
    return jsonify(plan)


if __name__ == '__main__':
   app.run(port=5000)
