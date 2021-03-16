import random
# word list
word_list = ['ardvark','baboon','camel']

len_word_list = len(word_list)

pick_random_word = random.choice(word_list)

len_pick_random_word = len(pick_random_word)

print("_ "*len_pick_random_word)

guess_letter = input("\nGuess a letter from word: ")

if len(guess_letter) > 1:
    print("Please enter a single letter word")
else:
    for character in pick_random_word:
        if character == guess_letter:
            print("True")
        else:
            print("False")

print(f"The random picked from list is {pick_random_word}")