from graph import SimpleAgentGraph

import tts

graph = SimpleAgentGraph()

while True:
    events = graph.run(input("Enter a message: "))

    for event in events:
        # if "messages" in event:
        #     event["messages"][-1].pretty_print()

        if "chatbot" in event:
            message = event["chatbot"]["messages"][-1].content
            if message != "":
                print(message)
                tts.text_to_speech(message, speaker=47)
