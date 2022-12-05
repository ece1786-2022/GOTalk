import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteriaList, StoppingCriteria
# from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

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

        # for context generation #
        # 1. stop if we get [BOS] -- Jon talking
        stop_context_words = ['[BOS]']
        stop_context_ids = [self.tokenizer.encode(w)[0] for w in stop_context_words]
        stop_context_criteria = KeywordsStoppingCriteria(stop_context_ids)
        # 2. exclude EOS
        bad_context_words = ['[EOS]']
        bad_context_ids = self.tokenizer(bad_context_words, add_special_tokens=False).input_ids

        # for dialogue generation #
        # 1. stop if we get [EOS] -- Jon stops talking
        stop_dialogue_words = ['[EOS]']
        stop_dialogue_ids = [self.tokenizer.encode(w)[0] for w in stop_dialogue_words]
        stop_dialogue_criteria = KeywordsStoppingCriteria(stop_dialogue_ids)
        # 2. exclude BOS
        bad_dialogue_words = ['[BOS]', ' "', ' Jon', ' said', ' he', ' Snow']
        bad_dialogue_ids = self.tokenizer(bad_dialogue_words, add_special_tokens=False).input_ids

    
    def generate(self):
        