import random

wordList = ["hello", "world", "Ash", "life", "happy"]

word = random.choice(wordList)

guessedWord = ['_'] * len(word)

attempts = 10
def hang(attempts):
    if attempts==9:
        print(' |')
        print(' O')
    if attempts==8:
        print(' |')
        print(' O')
        print(' |')
    if attempts==7:
        print(' |')
        print(' O')
        print('\|')
        
    if attempts==6:
        print(' |')
        print(' O')
        print('\|/')
    if attempts==5:
        print(' |')
        print(' O')
        print('\|//')
    if attempts==4:
        print(' |')
        print(' O')
        print('\|/')
        print(' |')
    if attempts==3:
        print(' |')
        print(' O')
        print('\|/')
        print(' |')
        print('/')
    if attempts==2:
        print(' |')
        print(' O')
        print('\|/')
        print(' |')
        print('//\\')
        
    if attempts==1:
        print('MAN IS HANGED')
    

while attempts > 0:
   
    print("\nCurrent word: " + ' '.join(guessedWord))

    guess = input("Guess a letter: ").lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: " + str(attempts))
        hang(attempts)

        
            
    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break
else:
    print("\nYou've run out of attempts! The word was: " + word)


