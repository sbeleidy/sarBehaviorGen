
class SocialRobot:

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
        pass

    def executeActionScript(self, action_script):
        """
        This function sends an action script to the test Robot. 
        The skill must already be started (see the `startSkill` function).
        The 'action_script' parameter must be a list of dictionaries,
        where each dictionary describes one action in the action script.
        """
        for action in action_script:
            print(action)

