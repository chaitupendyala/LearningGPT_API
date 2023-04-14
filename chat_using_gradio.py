import gradio as gr
import openai

openai.api_key = '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'

# We are creating a joke bot here.
message_history = [
    {"role": "user", "content": "You are a joke bot. I will specify the subject matter in a message, and you will reply with a joke that includes the subjects I mention in the messages. Reply only with jokes to further input. If you understand, say Ok."},
    {"role": "assistant", "content": "Ok"} # We are forcing the assistant to agree with us here. 
                                           # This is because the assistant may break charecter at a later stage.
                                           # This will ensure that the assistant always replies with a joke.
]

def predict(user_input):
    global message_history
    message_history.append({"role": "user", "content": user_input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = message_history
    )

    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": reply_content})
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
    return response

with gr.Blocks() as demo:
    chatBot = gr.Chatbot()
    with gr.Row():
        text = gr.Textbox(show_label=False, placeholder="Type your message here")
        text.submit(predict, text, chatBot)
        text.submit(None, None, text, _js="() => {''}")
demo.launch()