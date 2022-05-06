import graphlib
from pyexpat import model
import flask
import keras.models
import os
import sys
import json
from model import markov, syllables, rhymeindex, rhyme, split_lyrics_file, generate_lyrics, build_dataset, compose_poetry, vectors_into_song, train, main
from flask import Flask, render_template, url_for, request
from load import *
from keras.models import model_from_json
"""
from keras.models import Sequential
from keras.layers import LSTM 
from keras.layers.core import Dense

# opening and store file in a variable

json_file = open('model.json','r')
loaded_model_json = json_file.read()
json_file.close()

# use Keras model_from_json to make a loaded model

loaded_model = model_from_json(loaded_model_json)

# load weights into new model

loaded_model.load_weights("model.h5")
print("Loaded Model from disk")

# compile and evaluate loaded model

loaded_model.compile(loss='mse',optimizer='rmsprop')

"""

with open('model/model.json', 'r') as json_file:
    model = model_from_json(json_file.read())


app = Flask(__name__, static_url_path='/static')


@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contacts.html')

@app.route("/generate", methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        text = request.form['text_file']
        
        with open("text_file.txt", "w+") as f:
            f.write(text)
        #poetry_file = 'Shakespearean_poetry.txt'
        #text_file = 'text_file.txt'
        depth = 4 
        #train_mode = True        
        #main(depth, train_mode)
        train_mode = False
        main(depth, train_mode)
        
        with open('Shakespearean_poetry.txt') as f:
            f.seek(0)
            text_user = f.read()
            

        return render_template('result.html', text_file=text_user)
    else:
        return render_template('generatepage.html')

@app.route('/predict', methods=["GET", 'POST'])
def predict():
    modelData = request.get_data()
    




if __name__ == "__main__":
    app.run(debug=True)