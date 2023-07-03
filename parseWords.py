

class Parsed:

    # return this object to main so we have the array of selected words and the length of that array 
    # note: if using the dictionary this object makes more sense 

    def __init__(self, usedWords, SelectWords, length):
        self.usedWords = usedWords
        self.SelectWords = SelectWords
        self.length = length

#function: ReturnWords - reads through the given .txt file of used wordle word and creates the attributes in Parsed 
#                        returns the Parsed Object 
def ReturnWords():
    # usedWords is empty unless you uncomment lines labeled "dic"
    #initializing variables for the parsed object 
    usedWords = {}
    SelectWords = []
    length = 0

    # dic: 
    # for i in range (65, 91):
    #     usedWords[chr(i)] = [] 

    # read file and adds to the initialized variables 
    with open('usedWords.txt','r') as file:
        for line in file:
            for word in line.split():   
                # dic:
                # usedWords[word[0]].append(word)
                SelectWords.append(word) 
                length += 1
    
    # creates parsed object and returns it 
    ret = Parsed(usedWords, SelectWords, length)

    return ret



