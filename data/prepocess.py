file = open("./txtfiles/got1.txt", "r")
testfile = open("Jon_1.txt","w")


# cases: clean symbol near ""
# Jon index 0, "" => token, 
# Jon mid, mid -> front, 1 and 2 combine
# Jon mid, no 2, find next period. second " before Jon 

verbs = ["said", "felt"]
def alterline(line:str): 
    words = line.split()
    



for i in range(980):
    line = file.readline()
    if line != "\n" and i >= 817:
        print(line)
        testfile.write(line)
testfile.close()