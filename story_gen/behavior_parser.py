# from pyshop.pyshop import PyShop
# from pyshop.pyshop import State
# import json
# import argparse
# import sys
import re


def sentence_parser(para):
    lines = re.split(r'(?<=[.!?])', para)
    intentList = []
    for x in lines:
        # print(x)
        intent = intent_parser(x)
        # print(intent)
        keyVal = {"intent": intent, "content": x, "emothion": "posititve"}
        intentList.append(keyVal)

    return intentList


def intent_parser(line):
    return "inform"


if __name__ == '__main__':
    paragraph = "Hello there! My name is Binky. Binky is confused; Binky is talking in 3rd person and doesn't know why. Do you know why? What if Binky can't stop!? Bonky told Binky to get over it, but Binky is having a hard time \"getting over it.\" Binky tired now. Maybe Binky will speak better after some sleep/rest. Goodnight!"

    intents = sentence_parser(paragraph)

    print(intents)