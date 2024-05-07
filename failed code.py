import random

secretnumber = random.randint (1, 20)

print(' i am thinking of a number between 1 and 20')

for guessestaken in range (1, 7):
    
    print('take a guess')
    
    guess = int(input())
    

    if guess < secretnumber:
        
        print('your guess is too low')
        
    elif guess > secretnumber:
        print('your guess is too high')
        
    else:
        
        break
    
if guess == secretnumber:
    
     print ('good job! you guessed my number ') + str (guessestaken) + ('guesses!' )
    
else:
    
    print('nope wrong number')
    
#نص الكود مش راضي يشتغل لماذاااا؟     
    
