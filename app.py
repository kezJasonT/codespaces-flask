from flask import Flask, render_template
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the chicken go to the seance? To talk to the other side!",
    "Why don't some fish play piano? They're scared of the keys!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

@app.route('/')
def home():
    random_joke = random.choice(jokes)
    return render_template('index.html', joke=random_joke)

if __name__ == '__main__':
    app.run(debug=True)