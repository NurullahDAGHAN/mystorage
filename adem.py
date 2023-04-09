import random


def get_word():
    words = ["python", "computer", "science", "programming", "algorithm"]
    return random.choice(words)a


def play_game():
    word = get_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nInvalid character. Please try again.')

    if lives == 0:
        print('\nYou died, sorry. The word was', word)
    else:
        print('\nCongratulations! You guessed the word', word, '!!')


play_game()



