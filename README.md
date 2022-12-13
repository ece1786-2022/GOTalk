# GOTalk
We have implement two models to play with. The GPT2 is not deployed since it's result doesn't match our expectation. But a develop version is available. \

# Fine-tuned GPT2

To play the game with fine-tuned GPT2 

1. Open this notebook: https://github.com/ece1786-2022/GOTalk/blob/main/generate/GPT2_generation_engine.ipynb
2. Run though the first 3 cells to load the model from our hugging-face Repo and load required settings. Recommend to run with GPUs or the generations will be slow
3. You could change the Game Iterations (How many rounds to play) in the last cell with ITERATION
4. You could change the Pre-set Introduction in the last cell with context
5. Run the last cell to start the game
6. Input 'A', 'B' or 'C' when you are required to choose the dialogues
7. After the game ends, all the scripts will be saved in the play.txt for you to review

# GPT3 text-completion model

The GPT3 version is deployed on EC2 at http://3.85.50.72:5000

To run a local version:
```
cd Interface/backend
pip install -r requirements.txt
chmod 777 start.sh  
./start.sh
```
The local version will run at http://localhost:5000


## Useful Links
Data source:
https://www.kaggle.com/datasets/khulasasndh/game-of-thrones-books?select=004ssb.txt

Pretrained GPT2 model — HScomcom/gpt2-game-of-thrones:
https://huggingface.co/HScomcom/gpt2-game-of-thrones?text=My+name+is+Lewis+and+I+like+to

Final fine-tuned GPT2 model —- huangtuoyue/GPT2-large-GOTfinetuned_v5:
https://huggingface.co/huangtuoyue/GPT2-large-GOTfinetuned_v5

Complete GPT2 100 game generations:
https://github.com/ece1786-2022/GOTalk/blob/main/Evaluation/GPT2_Result_Evaluation.numbers
	
Complete GPT3 100 game generations:
https://github.com/ece1786-2022/GOTalk/blob/main/Evaluation/GPT3_evaluation_text.txt


