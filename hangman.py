import os
import requests
import random as rnd

class HangMan:
    def __init__(self,api) :
        self.api=api
        self.word=None
        self.length=None
        self.choices=None

    def api_data_set(self):
        # self.api = 'https://api.api-ninjas.com/v1/randomword'
        response = requests.get(self.api, headers={'X-Api-Key': 'by9Fu6ZMDue6FdcJBpgUNw==SvDAHgEaGOCm2gr5'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            word=response.json()["word"].lower()
            self.word=word

    def default_data_set(self):
        colors=['blue','red','yellow','purple','green','black','white','pink','orange']
        fruits=['apple','orange','banana','pineapple','mango','grapes','cheery','watermelon']
        cities=['tehran','paris','newyork','cairo','vienna','lagos','astana','bogota','seoul']
        topics={'Colors':colors,'Fruits':fruits,'Cities':cities}

        topic_choice=rnd.choice(list(topics.keys()))  #yeki az topic ha be onvane random entekhab mishe
        words_of_topic=topics[topic_choice]  #list topic entekhab shode ro mirize to variable
        word=rnd.choice(words_of_topic)  #yeki az kalamte list ro entekhab mikone
        self.word=word
    def set_choice_length(self):
        self.length=len(self.word)
        self.choices=(3*self.length)


    def game(self):
        guess=self.length * '_'.split("sth")
        
        word_parse_letters=list(self.word)
        print(f'{self.length} letters word.')
        
        
        while True :
            inp=input("enter a letter: ")
            if self.choices == 1:
                break

            if len(inp) == 1:
                print("*****************")
                if inp in word_parse_letters:
                    for letter in word_parse_letters:
                        if letter == inp:
                            print(">>Correct<<")
                            print(f"{self.choices} choice remain\n")
                            index = word_parse_letters.index(inp)
                            guess[index]=inp
                            word_parse_letters[index]=""

                            if "".join(guess) == self.word:
                                print("The Correct word is :","".join(guess),end='\n')
                                print("Congrats! You WON!!")
                                os._exit(0)
                            
                    print(f"word ({self.length} letters) = ","".join(guess),end='\n**************************\n')
                    return self.word

                else :
                    self.choices-=1
                    print(">>Wrong<<")
                    print(f"{self.choices} choice remain\n")
                    print(f"word ({self.length} letters) = ","".join(guess),end='\n**************************\n')
                    return "ali"
            else:
                print('You should enter only one letter!')
                self.choices-=1
                print(f"{self.choices} choice remain\n")

            print("You LOSE :((")
            print(f"The Correct word was :{self.word}")
            return 'hasn'