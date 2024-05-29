from hangman import HangMan

colors=['blue','red','yellow','purple','green','black','white','pink','orange']
fruits=['apple','orange','banana','pineapple','mango','grapes','cheery','watermelon']
cities=['tehran','paris','newyork','cairo','vienna','lagos','astana','bogota','seoul']
topics={'Colours':colors,'Fruits':fruits,'Cities':cities}

import random as rnd
#choice list migire pas .values( ) ro migirim
# print(rnd.choice(rnd.choice(list(topics.values()))))
a=rnd.choice(list(topics.keys()))
print(a)
# lst=topics[a]
# word=rnd.choice(lst)
# words=HangMan(word)
# words.set_choice_length()
# words.game()

