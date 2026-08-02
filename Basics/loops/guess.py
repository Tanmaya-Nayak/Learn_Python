import random

jackpot = random.randint(1, 100)
guess = int(input("Enter No: "))
count = 1
while jackpot != guess:
    if jackpot < guess:
        print("Guess Lower")
    else:
        print("Guess Higher")
    guess = int(input("Enter No again: "))
    count += 1
else:
    print("U guessed it correctly")
    print("Attempts: ", count)
