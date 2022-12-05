from flask import Flask, request, jsonify, make_response
from flask import request
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
import openai

STATIC_FOLDER = '../frontend/build'

app= Flask(__name__,static_folder=STATIC_FOLDER, static_url_path='')
CORS(app)

endings = {
    1:"Jon Snow becomes the King",
    2:"Jon Snow kills the nightking",
    3:"Jon snow finds his love of the life"
}
# prompt = "This is a role-play-dialogue game and the background of the story will be the Game of Thrones book. \
#   During this game, player will be playing as the Character Jon Snow and help him choose each dialogue from the three\
#   given options whenever Jon is about to speak. Dialogue options consist of the potential words that Jon Snow is going to say.\
#   Depending on the selected dialogue, generate the following context.\
#   The game will end by {} at the context-{}.\
#   \nFormat:\n Context-0: Jon Snow was standing in the courtyard of the Red Keep, surrounded by the noise and commotion of a bustling castle."+\
#   " The sun was setting, casting a pinkish hue across the stone walls and cobbled pathways. "+\
#   "Jon had just been told that he was going to take part in a special mission for the Lord Commander of the Night's Watch, and he was apprehensive. \n \n\n"+\
#   "Dialogue Options: \nA. I'm ready for whatever task is ahead of me"+\
#     "\nB. I'm nervous about this mission \nC. What can I do to help?\n\
#   Option selected: \n"
@app.route('/')   
def server():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/GPT3', methods=['POST'])
def play_gpt3():
    if request.method == "POST":
        data = request.get_json()
        key = data["key"]
        openai.api_key = key
        ending = int(data["ending"])
        round = data["round"]
        count = data["count"]
        option = data["option"]
        context = data["context"]
        complete_prompt = "This is a role-play-dialogue game and the background of the story will be "+ \
            "the Game of Thrones book. During this game, player will be playing as the Character Jon Snow " + \
            "and help him choose each dialogue from the three given options whenever Jon is about to speak and a forth option that is always other. "+ \
            "Dialogue options consist of the potential words that Jon Snow is going to say. Depending "\
            "on the selected dialogue, generate the following context and dialogue options. " +\
            "The game will end by {} at the context-{}.".format(endings[ending], round) + \
            "\nFormat:\nContext-0: Jon Snow was standing in the courtyard of the Red Keep, surrounded by the noise and commotion of a bustling castle."+\
            " The sun was setting, casting a pinkish hue across the stone walls and cobbled pathways. "+\
            "Jon had just been told that he was going to take part in a special mission for the Lord Commander of the Night's Watch, and he was apprehensive. \n \n\n"+\
            "Dialogue Options: \nA. I'm ready for whatever task is ahead of me"+\
                "\nB. I'm nervous about this mission \nC. What can I do to help? \nD. Other. \nOption selected: A. I'm ready for whatever task is ahead of me\n"
        complete_prompt += context
        # if option != '': 
        #     complete_prompt += "Option seleted: {}".format(option)
        complete_prompt += "\nContext-{}:".format(count)
        # print(complete_prompt)
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=complete_prompt,
        temperature=1,
        max_tokens=512,
        top_p=0.9,
        frequency_penalty=0.3,
        presence_penalty=0.2,
        stop="Option selected",
        best_of=3
        )
        text = response.choices[0].text
        # print(text)
        option_A = text.find("A.")
        option_B = text.find("B.")
        option_C = text.find("C.")
        option_D = text.find("D.")
        options = {'A':text[option_A:option_B], 'B':text[option_B:option_C], 'C':text[option_C:option_D]}
        # print(options)
        return make_response({"text": text, "options":options}, 200)





