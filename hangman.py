# import random
# # from typing import Protocol
# from IMAGE import IMAGES
# name=input("enter your name:")
# print("welcome" ,name)
# store = ["Thanks","Please","happy","gone","run"]
# word=random.choice(store)
# chance=1
# hang=0
# for i in range(len(word)):
#     print("_ ",end="")
# print(word)
# allguess="" 
# while chance<=10:
#     guess=input("guess the letter in the word: ")
#     if guess in word:
#         allguess=allguess+guess
#     print(allguess)
#     guessmade=""
#     i=0
#     if guess not in word:
#         print(IMAGES[hang])
#         hang=hang+1
#     while i<len(word):
#         if  word[i].upper() in allguess:
#             guessmade=guessmade+word[i]
#         else:
#             guessmade=guessmade+"_ "
#             print(hang,chance)
#         i=i+1
#     print(guessmade)
#     if len(word)==len(guessmade):
#         if word==guessmade:
#             print("win!!")
#             break    
#         elif word!=guessmade:
#             print("try again!")
#             break
#         chance=chance+1
#         if hang==len(IMAGES):
#             print("you lose the game")
#             

import random
from IMAGE import IMAGES

def hangman(name,word):
    print("welcome" ,name)
    chance=1
    hang=0
    for i in range(len(word)):
        print("_ ",end="")
    print(word)
    allguess="" 
    while chance<=10:
        guess=input("guess the letter in the word: ")
        if guess in word:
            allguess=allguess+guess
        print(allguess)
        guessmade=""
        i=0
        if guess not in word:
            print(IMAGES[hang])
            hang=hang+1
        while i<len(word):
            if  word[i] in allguess:
                guessmade=guessmade+word[i]
            else:
                guessmade=guessmade+"_ "
                print(hang,chance)
            i=i+1
        print(guessmade)
        if len(word)==len(guessmade):
            if word==guessmade:
                print("win!!")
                break    
            elif word!=guessmade:
                print("try again!")
                break
        chance=chance+1
        if hang==len(IMAGES):
            print("you lose the game")
            break
        
nam=input("enter your name:")
store = ["Thanks","Please","happy","gone","run"]
wor=random.choice(store)
hangman(nam,wor)