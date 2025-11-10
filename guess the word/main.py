import pandas as pd
import numpy as np
import random

df=pd.read_csv('words.csv')
print(df.head(0))

# select the random word from word
random_row=df.sample().iloc[0]
word=random_row['word']
hint1=random_row['hint1']
hint2=random_row['hint2']
hint3=random_row['hint3']
hint_array=np.array([hint1,hint2,hint3])


print("COMPUTER HAS ALREADY SELECTED A WORD.\nSTART GUESSING THE WORDS\n YOU HAVE 4 LIVES ")
print("\n YOUR FIRST HINT :", hint_array[0] ) 

for count in range(3):
    user_input=input("Enter your guess: ")
    if user_input.lower()==word.lower():
        print(f"YOU ARE CORRECT IN {count+1} STEP ")
        break
    else:
        if(count==2):
            print("OHH NO YOU ARE OUT OF LIVES")
            print("CORRECT WORD WAS ",word)
        else:
            print("INCORRECT GUESS. TRY AGAIN")
            print(f"YOUR NEXT HINT IS {hint_array[count+1]}")
    


    






