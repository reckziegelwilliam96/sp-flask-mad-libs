from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route('/')
def show_form():
    '''Create form to fill in for prompts to text'''
    prompts = story.prompts

    return render_template("home.html", prompts=prompts)

@app.route('/story')
def get_words():
    '''Show story result of prompts and text'''
    text = story.generate(request.args)
    
    return render_template('story.html', text=text)