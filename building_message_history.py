import openai

openai.api_key = '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'

def makeGPTCall(user_input, message_history):
    # build message history
    message_history.append({"role": "user", "content": user_input})
    completion = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages= message_history,
    )

    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content

message_history = []
# gpt api does not remember a conversation, so the message history needs to be stored
while True:
    user_input = input("Question :> ")
    if user_input.strip() == "q":
        exit()
    print("Question asked by the user:", user_input)

    reply = makeGPTCall(user_input, message_history)
    print(reply)