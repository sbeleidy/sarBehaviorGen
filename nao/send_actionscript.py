
import requests
import json

EVENT_NAME = "ActionScript"
SKILL_ID = "7d6fe0a1-61b4-4df5-872a-568776310d2f"

headers = {
    'Accept': 'application/json', 
    'Content-type': 'application/json'
}

class Nao:
    IP = "192.168.1.3"
    # http://127.0.0.1:5000/api
    server_ip = "127.0.0.1"
    server_port = "5000"
    server_url_root = "/api"
    server_url = "http://" + server_ip + ":" + server_port + server_url_root
    robot_ip = "192.168.1.3"
    robot_port = "9559"


    def __init__(self, address='192.168.1.2'):
        self.setAddress(address)


    def setAddress(self, address):
        """
        Set the IP address of the robot
        """
        self.robot_ip = address
        

    def startSkill(self):
        """
        This function starts the skill on the Misty.
        The skill is necessary for executing an action script
        """
        data = {"ip": self.robot_ip, "port": self.robot_port}
        url = self.server_url + "/connect"
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.json())
        return response


    def moveArms(self, arm, direction):
        """
        This function demonstrates how to directly control parts of Misty.
        This function will be obsolete once the Misty Skill is updated.
        The 'arm' parameter can be 'left', 'right', or 'both'
        The 'direction' parameter can be 'up', 'down', or 'straight'
        """
        if direction == "up":
            position = -90
        elif direction == "straight":
            position = 0
        elif direction == "down":
            position = 45

        data = { "Arm": arm, "Position": position, "Velocity":30}

        response = requests.post(self.arms_url, headers=headers, data=json.dumps(data))
        print(response.json())

    def executeActionScript(self, action_script):
        """
        This function sends an action script to Misty. 
        The skill must already be started (see the `startSkill` function).
        The 'action_script' parameter must be a list of dictionaries,
        where each dictionary describes one action in the action script.
        """
        payload = { "intent": "Explain1", "description": "Testing", "actionList": action_script };
        #data = {"Skill": SKILL_ID, "EventName": EVENT_NAME, "Payload": payload};
        print(json.dumps(payload))
        url = self.server_url + "/behavior"
        # TODO: add timeout
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(response.json())
        return response


def testActionScript():
    print("Reminder: Start Nao server before running this script")
    n = Nao("192.168.1.7")
    n.startSkill()
    action = [{ 'name': 'SetEyes', 'args': ['happy'] }, { 'name': 'SayText', 'args': ['This is a test, this is only a test.  You may now resume your debugging activities.'] }, { 'name': 'LookInDirection', 'args': ['center'] }, {'name': 'Pause','args': [500]}, { 'name': 'TiltHead', 'args': ['right', 'small'] }]
    action = [{ 'name': 'PointAt', 'args': ['downwards', 'both']}, {'name': 'Pause', 'args': [2000]}, {'name': 'SayText', 'args':['Congratulations!']}, { 'name': 'PointAt', 'args': ['upwards', 'both']}]
    action = [{ 'name': 'PointAt', 'args': ['default', 'both']}, { 'name': 'SetEyes', 'args': ['default'] }, { 'name': 'LookInDirection', 'args': ['center'] }]
    #action = [{'name': 'PointAt', 'args': ['straightOut', 'left']}, {'name': 'SetEyes', 'args': ['thinking']}, {'name': 'SayText', 'args': ['Do you want any help?']}, {'name': 'LookInDirection', 'args': ['center']}, {'name': 'SetEyes', 'args': ['looking']}, {'name': 'PointAt', 'args': ['downwards', 'both']}]
    n.executeActionScript(action)

if __name__ == '__main__':
    testActionScript()


# moveArms("left", "up")

# moveArms("right", "straight")

# moveArms("both", "down")

#startSkill()
#executeActionScript([{ 'name': 'SayText', 'args': ['My name is Misty. What is your name?'] }])

#print("executed action:", action)
#executeActionScript(action)


# if get_response.status_code == 200:
#     # Parse the JSON response into a Python dictionary
#     data = json.loads(get_response.text)
    
#     # Access the data using dictionary keys
#     print("Title: ", data['title'])
#     print("Completed: ", data['completed'])
# else:
#     print('Request failed with error code: ', get_response.status_code)


# POST example
# post_response = requests.post(url, headers=headers, data=json.dumps(data))

# if post_response.status_code == 201:
#     print(post_response.content)
# else:
#     print('Request failed with error code: ', post_response.status_code)
