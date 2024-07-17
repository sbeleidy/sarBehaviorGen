class RobotExpression:

    def __init__(self, speech:str, title=None, emotion="Neutral", color="Light Blue") -> None:
        self.speech = speech
        if title is None: 
            self.title = speech 
        else: 
            self.title = title

        self.emotion = emotion
        self.color = color
    
    def toDict(self)-> dict:
        """Convert to dictionary

        Returns:
            dict: The dictionary of values of the robot expression
        """
        return {
            "title": self.title,
            "speech": self.speech,
            "color": self.color,
            "emotion": self.emotion
        }


class PeerbotsButton:
    def __init__(self, speech:str, title=None, emotion="Neutral", color="Light Blue", labelColor="Light Blue") -> None:
        self.speech = speech
        if title is None: 
            self.title = speech 
        else: 
            self.title = title

        self.emotion = emotion
        self.color = color
        self.labelColor = labelColor

    def toDict(self)-> dict:
        """Convert to dictionary

        Returns:
            dict: The dictionary of values of the robot expression
        """
        return {
            "title": self.title,
            "speech": self.speech,
            "color": self.color,
            "emotion": self.emotion,
            "labelColor": self.labelColor
        }