
import requests
import json

IP = "127.0.0.1:5000"
# EVENT_NAME = "ActionScript"
STORY = "Hello there! My name is Binky. Binky is confused; Binky is talking in 3rd person and doesn't know why. Do you know why? What if Binky can't stop!? Bonky told Binky to get over it, but Binky is having a hard time \"getting over it.\" Binky tired now. Maybe Binky will speak better after some sleep/rest. Goodnight!"
# STORY = "Hello there! How are you today? Are you ready to start your task? Try moving the green triangle left."
# STORY = "Hello there!"
STORY = ["Peek a bruce.", "The geese want to play with Bruce today.", "Bruce does not want to play.",  "He's going for a walk alone.",  "Let's join him!", "But...",  "where is Bruce?",  "There he is!", "He was hiding behind the tree.",  "That tree is too small to hide behind."]
# action_url = "http://" + IP + "/api/skills/event"
story_url = "http://" + IP + "/get-plan"

headers = {
    'Accept': 'application/json', 
    'Content-type': 'application/json'
}

def parseStory():
    data = {"Story": STORY}
    response = requests.post(story_url, headers=headers, data=json.dumps(data))
    print(response.text)



if __name__ == '__main__':
    parseStory()