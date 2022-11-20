from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("HScomcom/gpt2-game-of-thrones")

model = AutoModelForCausalLM.from_pretrained("HScomcom/gpt2-game-of-thrones")

# model_name = "HScomcom/gpt2-game-of-thrones"

# generator = pipeline("text-generation", model=model_name, tokenizer=model_name)

# output = generator("Once upon a time")


text = "Once upon a time,"

encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

print(output)