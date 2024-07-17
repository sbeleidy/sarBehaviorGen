import requests
import json

IP = "127.0.0.1:5000"
# EVENT_NAME = "ActionScript"
STORY = "Hello there! My name is Binky. Binky is confused; Binky is talking in 3rd person and doesn't know why. Do you know why? What if Binky can't stop!? Bonky told Binky to get over it, but Binky is having a hard time \"getting over it.\" Binky tired now. Maybe Binky will speak better after some sleep/rest. Goodnight!"
# action_url = "http://" + IP + "/api/skills/event"
story_url = "http://" + IP + "/storyParser"

headers = {
    'Accept': 'application/json', 
    'Content-type': 'application/json'
}

def startSkill():
    """
    This function starts the skill on the Misty.
    The skill is necessary for executing an action script
    """
    data = {"Story": STORY}
    # url = "http://" + IP + "/api/skills/start"
    response = requests.post(story_url, headers=headers, data=json.dumps(data))
    print(response.json())



if __name__ == '__main__':
    startSkill()