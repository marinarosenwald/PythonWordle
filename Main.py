from parseWords import ReturnWords
import random

#initialize attempts var
maxAttempts = 6

#initialize an array of all possible words then randomly choose an index from that array 
obj = ReturnWords()
# dic:
# dic = obj.usedWords
words = obj.SelectWords
length = obj.length

select = random.randint(0, length) 

#initialize the word and uppercase it 
selectedWord = words[select].upper()

# create a dictionary for the word to check for letter positions of the selected word vs guess word
characters = {}
i = 0
for uniqChar in selectedWord:
    if uniqChar not in characters:
        characters[uniqChar] = []
    characters[uniqChar].append(i)
    i+=1 

# main loop
# while the user still has tries 
# 1) if invalid length - alert and don't advance to the next attempt
# 2) if correct - alert and end
# 3) else - check for correct letters and correct positions and alert the user 

attempts = 1
while attempts < maxAttempts+1: 
    output = "Attempt number " + str(attempts) + ": "
    guess = input(output).upper()
    if len(guess) != 5:
        print("Must be a 5 character word\n")
    
    elif guess == selectedWord:
        print("YOU'VE GUESSED IT!!!") 
        print(selectedWord) 
        break 

    # REMOVING THIS BECAUSE IT RUINS THE GAME
    # LEAVING THE HASHMAP IN COMMENTS FOR EXAMPLE PURPOSES 
    # feel free to comment out the dictionary code marked "dic" to see working creation and use of a dictionary/HashMap
    # dic:
    # elif not guess in dic[guess[0]]: 
    #     print("Not in Wordle history\n")


    else:
        letters = []
        stringCorrect = "-----"
        index = 0 
        for letter in guess: 
            if letter in selectedWord:
                if letter not in letters:
                    letters.append(letter) 
                if index in characters[letter]:
                    stringCorrect = stringCorrect[:index] + letter + stringCorrect[index + 1:]
            index += 1 

        print("\ncorrect letters: ")
        print(letters)
        print("correct positions: " + stringCorrect+"\n")
        attempts+=1

# if wrong tell the user the word 
if attempts > maxAttempts : 
    print()
    print("The word was: " + selectedWord)
