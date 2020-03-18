import pandas as pd
import numpy as np
game_file = "play_list.csv"
ds = pd.read_csv(game_file, header=0)
game_word = None
presented_categories = list(ds["Categories"])
cleaned_presented_categories = [x for x in presented_categories if str(x) != 'nan']

def game_start():
    
    global game_word
    
    print("\nCategory List:\n" + str(cleaned_presented_categories))

    selecting = True

    while selecting:
        try:  

            i = 0
            category_confirmation = True
            user_category = input("\nPlease select a catagory\n").casefold()

            while category_confirmation:

                if user_category == str(cleaned_presented_categories[i]).casefold():
                    print("Category '{}' has been selected!".format(user_category))
                    category_confirmation = False

                    selecting = False
                elif user_category != cleaned_presented_categories[i]:
                    i+=1

        except KeyError:
            print("Category '{}' not found...".format(user_category))
        except IndexError:
            print("Category '{}' not found...".format(user_category))

    # print("Cleaning data...\n")
    category_list_clean = [category.casefold() for category in list(ds.columns.values)]
    ds.columns = category_list_clean
    # print("Data Cleaned!\n")

    # print("Generating Word...\n")
    game_category = ds[user_category]
    cleaned_game_catagory = [x for x in game_category if str(x) != "nan"]
    game_word = np.random.choice(cleaned_game_catagory)
    # print("Word Generated!\n")

def get_game_word():
    return game_word

    
        
