from ollama import Client
client = Client(
  host='https://eh42j4hjocbed9-11434.proxy.runpod.net',
  headers={'x-some-header': 'some-value'}
)
def ask_about_image(input_file, user_question):
    response = client.chat(model='llama3.2-vision:latest', messages=[
    {
            'role': 'user',
            'content': user_question,
            'images': [input_file]
    },
    ])
    return response.message.content