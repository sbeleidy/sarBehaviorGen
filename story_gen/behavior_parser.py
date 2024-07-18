
import re
import anthropic
import os

SESSION_KEY = os.environ.get("ANTHROPIC_API_KEY")

def sentence_parser(para):

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key = SESSION_KEY,
    )

    lines = re.split(r'(?<=[.!?])', para)
    intentList = []
    for x in lines:
        if len(x) > 2:
            # print(x)
            intent = behavior_type(x, client)
            # print(intent)
            keyVal = {"intent": intent[0].text.lower(), "content": x, "emotion": "posititve"}
            intentList.append(keyVal)

    return intentList


def behavior_type(line, c_obj):

    response = c_obj.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        temperature=0,
        system="""There are four types of intents. An \"inform\" intent 
                communicates factual information to the inculocutor. An \"inquire\" intent communicates a 
                request for information from the inculocutor. A \"social\" intent uses social norms to 
                facilitate a natural, positive, and smooth interaction. An \"instruct\" intent provides 
                infromation to the inculocutor on how to proceed with their task.""",
        messages = [
            {
                "role": "user", "content": [
                    {
                        "type": "text",
                        "text": "For the following sentence, identify the appropriate intent. Answer with only the name of one of the four intents: \"" + line + "\""
                    }
                ]
            }
        ]
    )

    return response.content


if __name__ == '__main__':
    # paragraph = "Hello there! My name is Binky. Binky is confused; Binky is talking in 3rd person and doesn't know why. Do you know why? What if Binky can't stop!? Bonky told Binky to get over it, but Binky is having a hard time \"getting over it.\" Binky tired now. Maybe Binky will speak better after some sleep/rest. Goodnight!"
    paragraph = "Hello there! How are you today? Are you ready to start your task? Try moving the green triangle left."
    # paragraph = "Hello there!"

    intents = sentence_parser(paragraph)

    print(intents)