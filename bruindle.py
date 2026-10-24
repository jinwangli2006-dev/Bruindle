import random

ucla_words = ['bruin','ucla','westwood','sproul','rieber', 'royce','powell','ackerman','kerckhoff','library','pauley','basketball','janss','bear','wooden','cssi','olympic','deneve','starship']
cs30_words = ['syntax','functions','debugging','list','string','boolean','dictionary','tuple','conditional','loop','turtle','map', 'filter','lambda','reduce','recursion','return','true','false']
LA_words = ['angeles','hollywood','rams','downtown','lakers','griffith','ucla','california', 'beverly','grove','socal','lax','koreatown','usc', 'getty','dodgers','universal']


def choose_version():
    """Ask until the player picks a version, then return its secret word."""
    while True:
        version = input("Which version would you like to play?(uc/cs/la): ").lower()
        if version == 'uc':
            return random.choice(ucla_words)
        if version == 'cs':
            return random.choice(cs30_words)
        if version == 'la':
            return random.choice(LA_words)
        print('Invalid')


def score_guess(guess, chosen):
    """Split a guess into right-position, wrong-position and not-in-word letters.

    Duplicates score the way Wordle does: a guessed letter only counts as
    wrong-position while the hidden word still has unmatched copies of it.
    """
    right = []
    wrong = []
    not_in_word = []
    unmatched = {}
    for i in range(len(chosen)):
        if guess[i] == chosen[i]:
            right.append(guess[i] + ' in position ' + str(i + 1))
        else:
            unmatched[chosen[i]] = unmatched.get(chosen[i], 0) + 1
    for i in range(len(chosen)):
        if guess[i] == chosen[i]:
            continue
        if unmatched.get(guess[i], 0) > 0:
            wrong.append(guess[i] + ' in position ' + str(i + 1))
            unmatched[guess[i]] -= 1
        else:
            not_in_word.append(guess[i])
    return right, wrong, not_in_word


def game():
    chosen = choose_version()
    lives = 6
    print('The word is', len(chosen), 'letters long')
    while lives > 0:
        guess = input('Please enter a guess: ').lower()
        if guess == chosen:
            print('You won! Great game :)')
            play_again()
            return
        if len(guess) != len(chosen):
            print('Invalid')
            continue
        lives -= 1
        right, wrong, not_in_word = score_guess(guess, chosen)
        print('the following letter(s) are in the right position: ' + str(right))
        print('the following letter(s) are in the wrong position: ' + str(wrong))
        print('the following letter(s) are not in the word: ' + str(not_in_word))
        if lives == 0:
            print('You lost all your lives! The word was: ' + chosen + ". Better luck next time :)")
            play_again()
            return


def play_again():
    retry = input("Would you like to play again?(y/n): ").lower()
    if retry == 'y':
        game()
    elif retry == 'n':
        print('Thanks for playing!')
    else:
        print('Invalid')


print('Welcome to BRUINDLE, a Wordle alternative')
print('You may choose to play between three versions: UCLA, CS30, or LA!')
while True:
    instructions = input("Would you like a brief overview of the game?(y/n): ").lower()
    if instructions == 'y':
        print('Alright, so the rules are simple. You will be given a random word and are instructed to guess what the word is. The length of the word will be given to you before the game begins. You will have 6 attempts per word and be told which letters are incorrect, which are correct, and which are in the correct position. Good luck!')
        break
    if instructions == 'n':
        print('Here we go.')
        break
    print('Invalid')
game()
