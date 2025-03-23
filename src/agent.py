from graph import SimpleAgentGraph

import tts

graph = SimpleAgentGraph()

while True:
    events = graph.run(input("Enter a message: "))

    for event in events:
        if "messages" in event:
            event["messages"][-1].pretty_print()

        # if "messages" in event:
        #     tts.text_to_speech(event["messages"][-1].content)
