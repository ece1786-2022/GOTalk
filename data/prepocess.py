from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sklearn.model_selection import train_test_split
#file = open("./data/txtfiles/got1_Jon.txt", "r")
file = open("./txtfiles/GOT_Jon1235all.txt", "r")
testfile = open("./GOT_Jon1235all_fined_Final.txt","w")

START = "[BOS]"
END = "[EOS]"
verbs = ["said", "felt", "told"]

def alterline(line:str): 
    words = word_tokenize(line)
    # case 2
    start = []
    end = []
    for i, word in enumerate(words): 
        if word == '“':
            start.append(i)
        if word == '”':
            end.append(i)
    # words = list(map(lambda x: x.replace(',', " "), words))
    # words = list(map(lambda x: x.replace('.', " "), words))
    # words = list(map(lambda x: x.replace(" ’ ", " ' "), words))

    if len(start) > 2 or len(start) != len(end): 
        word_ls = list(map(lambda x: x.replace('“', ""), words))
        word_ls = list(map(lambda x: x.replace('”', ""), word_ls))
        return TreebankWordDetokenizer().detokenize(word_ls)
    # Case 1
    if len(words) > 0 and words[0] == 'Jon':
        if len(start) == 1:
            word_ls = list(map(lambda x: x.replace('“', START), words))
            word_ls = list(map(lambda x: x.replace('”', END), word_ls))
            return TreebankWordDetokenizer().detokenize(word_ls)
            # print('\n')
    # Case 2
    if len(start) == 2:
        pos = end[0]
        if words[pos+1] == "Jon" and (words[pos+2][-2:] == "ed" or words[pos+2] in verbs):
            mid_context = words[end[0]+1:start[1]]
            dialogue_1 = [START] + words[start[0] + 1:end[0]]
            dialogue_2 = words[start[1]+1:end[1]] + [END]
            newline = words[:start[0]] + mid_context + dialogue_1 + dialogue_2 + words[end[1]+1:]
            return TreebankWordDetokenizer().detokenize(newline)
    # Case 3
    if len(start) == 1:
        pos = end[0]
        
        if pos < len(words) - 2 and words[pos+1] == "Jon"  and (words[pos+2][-2:] == "ed" or words[pos+2] in verbs):
            context = words[end[0]+1:]
            dialogue = [START] + words[start[0] + 1:end[0]] + [END]
            newline = words[:start[0]] + context + dialogue
            return TreebankWordDetokenizer().detokenize(newline)
    word_ls = list(map(lambda x: x.replace('“', ""), words))
    word_ls = list(map(lambda x: x.replace('”', ""), word_ls))
    
    return TreebankWordDetokenizer().detokenize(word_ls)




for i in range(9856):
    line = file.readline()
    if len(line.split()) == 1:
        continue 
    if line != "\n":
        newline = alterline(line)
        testfile.write(newline)
        testfile.write('\n')
testfile.close()


file = open("./GOT_Jon1235all_fined_Final.txt", "r")
full_texts =[]
texts = []
labels = []
for i in range(4903):
    line = file.readline()
    words = word_tokenize(line)
    sentence = TreebankWordDetokenizer().detokenize(words)
    if len(sentence) == 0: 
        print(line, i)
    if sentence[-1] == ']':
        sentence = sentence + ' '
    sentence = sentence.replace(" ’ ", " ' ")
    # sentence = sentence.replace("“", '"')
    # sentence = sentence.replace("”", '"')
    sentence = sentence.replace(". [BOS]", "[BOS]")
    sentence = sentence.replace(", [BOS]", "[BOS]")
    sentence = sentence.replace("Jon said,", "Jon said")
    sentence = sentence.replace("Jon said .", "Jon said")
    full_texts.append(sentence)
    # texts.append(TreebankWordDetokenizer().detokenize(words[:-1]))
    # labels.append(TreebankWordDetokenizer().detokenize(words[1:]))
    
train, test = train_test_split(full_texts, test_size=0.2, shuffle=False)


file = open('./GOT_Train_Final1.txt', 'w')
for i in train:
    if '[BOS]' in i or '[EOS]' in i:
        file.write(" " + i)
    # file.write('\n')
file.close()

file = open('./GOT_Test_Final1.txt', 'w')
for i in test:
    if '[BOS]' in i or '[EOS]' in i: # keep rows with EOS or BOS
        file.write(" " + i)
    # file.write('\n')
file.close()