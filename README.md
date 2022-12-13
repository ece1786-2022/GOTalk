# GOTalk
We have implement two models to play with. The GPT2 is not deployed since it's result doesn't match our expectation. But a develop version is available. 

# Fine-tuned GPT2

To run the GPT2 generation file:
```
cd generate
```
Then run the GPT2_generation_engine.ipynb to see output.

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

