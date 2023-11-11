import random
word_list=["lindsay","adverb","noun"]

chosen_word=random.choice(word_list)

display=[]
wordlen=len(chosen_word)
for letter in chosen_word:
    display+="_"
print(display)   
guess=input("what letter do you think it is").lower()


for letter in chosen_word:
    if letter==guess:
        print("right")
    else:
        print("wrong")