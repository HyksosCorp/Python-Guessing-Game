import game_settings as gs
import numpy as np
import random
from readchar import readchar

replay = True
lost = False
score = 0

# file_name = 

while replay:

    guess_count = 0

    
    
    print("\nPython Guessing Game.\n\nContinue by pressing any key...")
    readchar()
    
    gs.game_start()
    game_word = gs.get_game_word()
    
    word_len = len(game_word)
    word_list = list(game_word)
    guess_list = word_list.copy()
    
    blank_spacer = int((word_len * 0.75))
    rand_index = random.sample(range(0,word_len),blank_spacer)

    for i in range(blank_spacer):
        guess_list[rand_index[i]] = "_"

    print(str(guess_list) + "\n")

    guessing = True
    while guessing:
        
        print("\nInput a letter")
        guess_char = str(readchar(), encoding="utf-8")
        print("guessed character:" + guess_char + "\n")
        
        mask_list = (np.array(guess_list) == np.array(word_list))

        for i in range(word_len):
            if mask_list[i] == False:
                if guess_char == word_list[i]:
                    guess_list[i] = guess_char
                    
            elif mask_list[i] == True:
                if guess_char == word_list[i]:
                    print("Letter(s) previously identified or desplayed!\n")

            
            continue
        guess_count += 1
        print(guess_list)
        
        if guess_count == word_len + 3:
            print("\nTOO many guesses!!!")
            print("Word was:" + game_word)
            lost = True
            break

        if guess_list == word_list:
            guessing = False
        
    print("Final Guess Count: " + str(guess_count))
   
    score = score + int(((word_len * 100) /guess_count))
    print("Current Score: " + str(score))
    
    print("Replay and add onto your current score? [Y]es or [N]o")
    replay_confirmation = str(readchar(), encoding="utf-8").casefold()

    if  lost == True:
        print("Final score:" + str(score))
        replay = False
        break

    elif replay_confirmation == "n".casefold():
        print("Final score:" + str(score))
        replay = False
        break

    elif replay_confirmation == "y".casefold:
        replay = True
        continue

    


    