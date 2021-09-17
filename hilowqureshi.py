import random    
x=(random.randint(1,100))
tries=0
guess=0

while guess != x and tries < 8:
    tries= tries + 1
    guess= int(input("What is your guess? "))

    if guess > x:
        print("You need to guess lower")
    if guess < x:
        print("You need to guess higher")
    if guess == x: 
        print("You guessed right, you're awesome!")
