import random
from words import word_list

def getRandom():
    word = random.choice(word_list)
    return word.upper()

def play(word):
 word_completion = "_"*len(word)
 guessed=False
 guessed_letter = []
 guessed_word = []
 tries = 6


 
 print("let us play Hangman it will be really fun")
 print('the length of the word is ',len(word))
 print(word_completion)

 while not guessed and tries>0:
    guess = input("please guess a letter or a word: ").upper()
    if len(guess)==1 and guess.isalpha():
        if guess in guessed_letter:
            print("you have already guessed this letter" ,guess)
            displayhangman(tries)
            print(word_completion)
        elif guess not in word:
                print(guess, "is not in the word ")
                tries = tries-1
                displayhangman(tries)
                if tries==0:
                    print("you ran out of tries, you lost the word we were lookinf or was ",word)
                    break
                guessed_letter.append(guess)
                
        else:
                    print("good ",guess,"is a part of the given word")
                    displayhangman(tries)
                    guessed_letter.append(guess)
                    word_as_list=list(word_completion)
                    indices=[i for i, letter in enumerate(word) if letter==guess]
                    for index in indices:
                             word_as_list[index]=guess
                    word_completion="".join(word_as_list)
                    print(word_completion)
                    if "_" not in word_completion:
                             print("congragulations you have won this game")
                             break
                             displayhangman(tries)
    elif len(guess)==len(word):
       if word == guess:
        print("congragulations you have won this game")
        break
       
       else :
            print("Not a valid guess")
            tries-=1
            displayhangman(tries)
            word_as_list=list(word_completion)
            indices=[i for i, letter in enumerate(word) if letter==guess]
            for index in indices:
              word_as_list[index]=guess
              word_completion="".join(word_as_list)
            print(word_completion)
            
            if tries==0:
                 print("sorry,you ran out of tries, you lost the word was ",word)
                 break

def displayhangman(tries):
    if tries==0:
        print( """
        
        
            -----
             |
             0
            \\|/
             |
            / \\
        """)
        
    elif tries==1:
      print( """
            -----
             |
             0
            \\|/
             |
            / 

        """)
    elif tries==2:
      
      print(  """
            -----
             |
             0
            \\|/
             |
            
        """)
    elif tries==3:
        print("""
            -----
             |
             0
            \\|
             |
            
        """)
    elif tries==4:
       
         print( """
            -----
             |
             0
             |
             
            
        """)
    elif tries==5:
        print("""
            -----
             |
             0
            
            
            
        """)
    elif tries==6:
         print("""
            -----
             |


            
        
        """)
         
         

def main():
     x=getRandom()
     play(x)
     while input('do you want to play again ?(Y/N): ').upper == 'Y':
                     main()

main()



