import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteriaList, StoppingCriteria
# from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

BOS = "[BOS]"
EOS = "[EOS]"

class KeywordsStoppingCriteria(StoppingCriteria):
    def __init__(self, keywords_ids:list):
        self.keywords = keywords_ids

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        if input_ids[0][-1] in self.keywords:
            return True
        return False

class GPT2: 
    def __init__(self) -> None:  
        self.tokenizer = AutoTokenizer.from_pretrained("huangtuoyue/GPT2-large-GOTfinetuned_v5")
        self.model = AutoModelForCausalLM.from_pretrained("huangtuoyue/GPT2-large-GOTfinetuned_v5")  
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        # for context generation #
        # 1. stop if we get [BOS] -- Jon talking
        stop_context_words = ['[BOS]']
        stop_context_ids = [self.tokenizer.encode(w)[0] for w in stop_context_words]
        self.stop_context_criteria = KeywordsStoppingCriteria(stop_context_ids)
        # 2. exclude EOS
        bad_context_words = ['[EOS]']
        bad_context_ids = self.tokenizer(bad_context_words, add_special_tokens=False).input_ids

        # for dialogue generation #
        # 1. stop if we get [EOS] -- Jon stops talking
        stop_dialogue_words = ['[EOS]']
        stop_dialogue_ids = [self.tokenizer.encode(w)[0] for w in stop_dialogue_words]
        self.stop_dialogue_criteria = KeywordsStoppingCriteria(stop_dialogue_ids)
        # 2. exclude BOS
        bad_dialogue_words = ['[BOS]', ' "', ' Jon', ' said', ' he', ' Snow']
        self.bad_dialogue_ids = self.tokenizer(bad_dialogue_words, add_special_tokens=False).input_ids
    def _generate(self, text, pred_dialogue):
        encoded_input = self.tokenizer(text, return_tensors='pt').input_ids
    
        # for context generation
        if not pred_dialogue: 

            outputs = self.model.generate(encoded_input.to(self.device), do_sample=True, min_length=60, max_new_tokens=150, pad_token_id = 50256,
                                    temperature=0.95, top_p = 1, repetition_penalty = 1.1,
                                    stopping_criteria=StoppingCriteriaList([self.stop_context_criteria]), bad_words_ids = bad_context_ids)
            
            # for dialogue generation
        else:
            outputs = self.model.generate(encoded_input.to(self.device), do_sample=True, min_length=3, max_new_tokens=50, pad_token_id = 50256, 
                                    temperature=1.1, top_p = 1, repetition_penalty = 1, 
                                    stopping_criteria=StoppingCriteriaList([self.stop_dialogue_criteria]), bad_words_ids = bad_dialogue_ids)
            
        # deceode outputs and keep speical_tokens
        res = self.tokenizer.batch_decode(outputs, skip_speical_tokens=False)
        return res[0]

    def generate(self, context, pred_dialogue):
        incorrect_generation = 0
        total = 0
        options = []
        prev_context_end_idx = len(context)
        context_list = context.split()

        # check context length #
        if len(context_list) < 50: # used last 50 words to generate new context
            run_context = TreebankWordDetokenizer().detokenize(context_list)
            last_idx = len(run_context)

        else: 
            run_context = TreebankWordDetokenizer().detokenize(context_list[-50:])
            last_idx = len(run_context)
        
        # dialogue generation #
        pred = self._generate(run_context, pred_dialogue)
        
        # count total generation time #
        total += 1

        # check if generation includes [BOS] & [EOS] #
        words = pred.split()
        eos_list = []
        bos_list = []
        for j, word in enumerate(words): 
            if word == BOS: 
                bos_list.append(j)
            elif word == EOS:
                eos_list.append(j)
        
        # Validity for context generation #
        if words[-1] == BOS and not pred_dialogue: # correct context
        # if '[BOS]' in words: # correct context
            context = pred
            # print(context)
            print(context[last_idx:-5] + ":")
            print("\n")
            f.write(context[last_idx:-5]+ ":")
            f.write("\n")

            pred_dialogue = True

        elif words[-1] != '[BOS]' and not pred_dialogue: # no [BOS]
            # print("Invalid Context: no BOS or too long \n")
            incorrect_generation += 1

            pred_dialogue = False
        elif pred_dialogue:
            if words[-1] != '[EOS]':
                # print("Invalid Dialogue: no EOS or too long \n")
                incorrect_generation += 1

            elif words[-1] == '[EOS]': # correct dialogue
                option = TreebankWordDetokenizer().detokenize(words[bos_list[-1]+1:eos_list[-1]])
                options.append(option)
                pred_dialogue = True
                if len(options) == 3: 
                    pass
        # Validity for dialogue generation #