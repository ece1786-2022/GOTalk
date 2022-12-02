from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sklearn.model_selection import train_test_split
#file = open("./data/txtfiles/got1_Jon.txt", "r")
file = open("./txtfiles/got3_Jon.txt", "r")
testfile = open("./got3_fined.txt","w")


# cases: clean symbol near ""
# Jon index 0, "" => token, 
# Jon mid, mid -> front, 1 and 2 combine
# Jon mid, no 2, find next period. second " before Jon 
START = "<|endoftext|>"
END = "<|endoftext|>"


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

    if len(start) > 2 or len(start) != len(end): 
        word_ls = list(map(lambda x: x.replace('“', ""), words))
        word_ls = list(map(lambda x: x.replace('”', ""), word_ls))
        return TreebankWordDetokenizer().detokenize(word_ls)
    if len(words) > 0 and words[0] == 'Jon':
        if len(start) == 1:
            word_ls = list(map(lambda x: x.replace('“', START), words))
            word_ls = list(map(lambda x: x.replace('”', END), word_ls))
            return TreebankWordDetokenizer().detokenize(word_ls)
            # print('\n')
    if len(start) == 2: 
        pos = end[0]
        if words[pos+1] == "Jon" and (words[pos+2][-2:] == "ed" or words[pos+2] in verbs):
            mid_context = words[end[0]+1:start[1]]
            dialogue_1 = [START] + words[start[0] + 1:end[0]]
            dialogue_2 = words[start[1]+1:end[1]] + [END]
            newline = words[:start[0]] + mid_context + dialogue_1 + dialogue_2 + words[end[1]+1:]
            return TreebankWordDetokenizer().detokenize(newline)
    
    # case 3
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



for i in range(2429):
    line = file.readline()
    if len(line.split()) == 1:
        continue 
    if line != "\n":
        newline = alterline(line)
        testfile.write(newline)
        # testfile.write('\n')
testfile.close()


# file = open("./got3_fined.txt", "r")
# full_texts =[]
# texts = []
# labels = []
# for i in range(1210):
#     line = file.readline()
#     words = word_tokenize(line)
#     sentence = TreebankWordDetokenizer().detokenize(words)
#     if len(sentence) == 0: 
#         print(line, i)
#     if sentence[-1] == ']':
#         sentence = sentence + ' '
#     full_texts.append(sentence)
#     # texts.append(TreebankWordDetokenizer().detokenize(words[:-1]))
#     # labels.append(TreebankWordDetokenizer().detokenize(words[1:]))
    
# train, test = train_test_split(full_texts, test_size=0.2, shuffle=False)


# file = open('./got3_train.txt', 'w')
# for i in train:
#     file.write(i)
# file.close()

# file = open('./got3_test.txt', 'w')
# for i in test:
#     file.write(i)
# file.close()


# print(tmp, tmp.index(6))

# s = '''“He’s not like the others,” Jon said. “He never makes a sound. That’s why I named him Ghost. That, and because he’s white. The others are all dark, grey or black.” '''
# words = word_tokenize(s)
# l = []
# for i, word in enumerate(words): 
#     if word == '“':
#         l.append(i)
# print(len(l))
