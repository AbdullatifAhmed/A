import random
number = random.randint(1,100)
guess = 0
c = 1
print("Guess the number!")
while guess != number:

    guess = int(input("Is it... "))
    if c == 10:
        print('Sorry, you ran out of attempts :( ')
        break
    elif guess == number and c > 3:
        print("Wow! You guessed it right!")
    elif guess < number:
        print("Opps, It's bigger...")
    elif guess > number:
        print("Opps, It's not so big.")
    elif guess == number and c <= 3:
        print ('You are an amazing guesser!')
    c = c + 1