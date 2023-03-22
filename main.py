


from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# --- Enter your API here----below is just an example

openai.api_key = "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"
model_engine = "text-davinci-003" # Update model as needed

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


