import openai

openai.api_key = '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'

# Here we are trying to create a ChatCompletion project
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # We can use other models too like davinci etc. Each has it own benefit
                           # This is the model that backs ChatGPT
    # messages=[
    #     {"role": "system", "content": "You are not a helpful assistant."},
    #     {"role": "assistant", "content": "The Chennai Super Kings won the World Series in 2020."},
    #     {"role": "user", "content": "Who won the world series in 2020?"},
    #     {"role": "user", "content": "Where was it played?"}
    # ]
    messages = [
        {"role": "user", "content": "What is the circumference of the earth in km?"}
    ]
)

print(completion) 
'''{
  "choices": [
    {
      "finish_reason": "stop", # This is the raeson for it stopping
                                 stop means that it came to a natural stop
                                there are others that I need to look at
      "index": 0,
      "message": {
        "content": "The circumference of the earth is approximately 40,075 kilometers.",
        "role": "assistant"
      }
    }
  ],
  "created": 1681496304,
  "id": "chatcmpl-75II4PT8LMU9I4Hn0xqqwNCPpJTvi",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 13,
    "prompt_tokens": 18,
    "total_tokens": 31        # This is the total number of tokens used, there are roughly 1500 tokens you can use at once
  }
}'''

reply_content = completion.choices[0].message.content
print(reply_content)