from nltk.tokenize import word_tokenize
file = open("./txtfiles/got1_Jon.txt", "r")
testfile = open("Jon_1.txt","w")


# cases: clean symbol near ""
# Jon index 0, "" => token, 
# Jon mid, mid -> front, 1 and 2 combine
# Jon mid, no 2, find next period. second " before Jon 
START = "<START>"
END = "<END>"


verbs = ["said", "felt"]
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
    if len(start) > 2 or len(start) != len(end): 
        return line 
    if len(start) == 2: 
        pos = end[0]
        if words[pos+1] == "Jon" and (words[pos+2][-2:] == "ed" or words[pos+2] in verbs):
            mid_context = words[end[0]+1:start[1]]
            dialogue_1 = [START] + words[start[0] + 1:end[0]]
            dialogue_2 = words[start[1]+1:end[1]] + [END]
            newline = words[:start[0]] + mid_context + dialogue_1 + dialogue_2 + words[end[1]+1:]
            # print(line)
            # print(newline)
    
    # case 3
    if len(start) == 1:
        pos = end[0]
        
        if pos < len(words) - 2 and words[pos+1] == "Jon"  and (words[pos+2][-2:] == "ed" or words[pos+2] in verbs):
            context = words[end[0]+1:]
            dialogue = [START] + words[start[0] + 1:end[0]] + [END]
            newline = words[:start[0]] + context + dialogue
            print(line)
            print(newline)


        # prev = word

tmp = []
for i in range(2205):
    line = file.readline()
    if line != "\n":
        alterline(line)

#         testfile.write(line)
# testfile.close()
# print(tmp, tmp.index(6))

# s = '''“He’s not like the others,” Jon said. “He never makes a sound. That’s why I named him Ghost. That, and because he’s white. The others are all dark, grey or black.” '''
# words = word_tokenize(s)
# l = []
# for i, word in enumerate(words): 
#     if word == '“':
#         l.append(i)
# print(len(l))
