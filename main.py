

#openai.organization = "org-yl8cj1otp7Fd8e3gapjRf5Gt"
#openai.api_key = os.getenv("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")
from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

#openai.api_key = os.getenv("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")
openai.api_key = "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"
model_engine = "text-davinci-003"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message']
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Conversation:\nUser: {message}\nAI:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run()


