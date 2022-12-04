from flask import Flask, request, jsonify, make_response
from flask import request
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
import openai

STATIC_FOLDER = '../../frontend/build'

app= Flask(__name__,static_folder=STATIC_FOLDER, static_url_path='')
CORS(app)

OPENAI_API_KEY = "+"
endings = {
    1:"Jon Snow becomes the King",
    2:"Jon Snow kills the nightking",
    3:"Jon snow finds his love of the life"
}
prompt = "This is a role-play-dialogue game and the background of the story will be the Game of Thrones book. \
  During this game, player will be playing as the Character Jon Snow and help him choose each dialogue from the three\
  given options whenever Jon is about to speak. Dialogue options consist of the potential words that Jon Snow is going to say.\
  Depending on the selected dialogue, generate the following context.\
  The game will end by {} at the context-{}.\
  \nFormat:\n Context-0: \n \n\nDialogue Options: \nA. \nB. \nC. \n\
  Option selected: \n"
@app.route('/')   
def server():
    return send_from_directory(app.static_folder, 'index.html')
#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
@cross_origin
@app.route('/api/GPT3', methods=['GET','POST','PUT'])
def play_gpt3():
    if request.method == "POST":
        data = request.get_json()  
        print(data)
        key = data["key"]
        openai.api_key = key
        ending = int(data["ending"])
        round = data["round"]
        count = data["count"]
        option = data["option"]
        context = data["context"]
        complete_prompt = "This is a role-play-dialogue game and the background of the story will be the Game of Thrones book. \
            During this game, player will be playing as the Character Jon Snow and help him choose each dialogue from the three\
            given options whenever Jon is about to speak. Dialogue options consist of the potential words that Jon Snow is going to say.\
            Depending on the selected dialogue, generate the following context.\
            The game will end by {} at the context-{}.\
            \nFormat:\n Context-0: \n \n\nDialogue Options: \nA. \nB. \nC. \n\
            Option selected: \n".format(endings[ending], round)
        complete_prompt += context
        if option != '': 
            complete_prompt += "Option seleted: {}".format(option)
        complete_prompt += "\nContext-{}:".format(count)
        print(complete_prompt)
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=complete_prompt,
        temperature=1,
        max_tokens=256,
        top_p=0.9,
        frequency_penalty=0.3,
        presence_penalty=0.2,
        stop="Option selected",
        best_of=3
        )
        text = response.choices[0].text
        return make_response({"text": text}, 200)





