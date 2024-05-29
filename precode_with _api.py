import os

word="orangee"
word_list=list(word)
length=len(word)
choices=3*length

guess=length*'_'.split("sth")

for i in range(choices):
    inp=input("enter a letter: ")
    print("*****************")
    
    if inp in word_list:
        for letter in word_list:
            if letter == inp:
                print(">>Correct<<")
                print(f"{choices} choice remain\n")
                index = word_list.index(inp)
                guess[index]=inp
                word_list[index]=""
                choices-=1

                if "".join(guess) == word:
                    print("".join(guess),end='\n')
                    print("you won!!")
                    os._exit(0)
        print(f"word ({length} letters) = ","".join(guess),end='\n**************************\n')

    else :
        print(">>Wrong<<")
        print(f"{choices} choice remain\n")
        print(f"word ({length} letters) = ","".join(guess),end='\n**************************\n')
        choices-=1
        
print("you lose sucker!!")
        

