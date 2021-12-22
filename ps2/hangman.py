# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_set = set(secret_word)
    for letter in letters_guessed:
      if letter in secret_word_set:
        secret_word_set.remove(letter)
      if len(secret_word_set) == 0:
        return True
    return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    returned_word = list('_')*len(secret_word)
    for i in range(len(secret_word)):
      if secret_word[i] in letters_guessed:
        returned_word[i] = secret_word[i]

    return ' '.join(returned_word)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = list(string.ascii_lowercase)
    for letter in letters_guessed:
      if letter in letters_not_guessed:
        letters_not_guessed.remove(letter)
    return ''.join(letters_not_guessed)

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word_length = len(secret_word)
    guesses = 6
    letters_guessed = []
    print('The secret word is ' + str(secret_word_length) + ' letters long.')
    
    while guesses > 0:
      print('-------------------------------------------------')
      print('You have ' + str(guesses) + ' guesses remaining.')
      print('Here are the available letters you may guess ' + get_available_letters(letters_guessed) + '.\n')
      guess = input('Please type in your guessed letter:')
      
      if guess not in string.ascii_lowercase:
        print('your guess must be a lowercase letter. Try again')
        continue
      letters_guessed.extend(guess)
      if guess in secret_word:
        print('You guessed a correct letter!')
      else:
        print('INCORRECT GUESS')
        guesses -= 1
      print(get_guessed_word(secret_word, letters_guessed))
      if is_word_guessed(secret_word, letters_guessed):
        print('YOU WIN')
        return
      
    print('You are out of guesses. you lose.')
    print('the word was ' + secret_word)
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_without_spaces = my_word.replace(' ','')
    letter_set = set(my_word_without_spaces)
    if len(my_word_without_spaces) != len(other_word):
      return False
    for i in range(len(my_word_without_spaces)):
      if my_word_without_spaces[i] != '_' and my_word_without_spaces[i] != other_word[i]:
        return False
      if my_word_without_spaces[i] == '_' and other_word[i] in letter_set:
        return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    returned_list = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        returned_list.append(word)
    if not returned_list:
      print('No matches found')
    else:
      print(' '.join(returned_list))
        
    

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word_length = len(secret_word)
    guesses = 6
    letters_guessed = []
    print('The secret word is ' + str(secret_word_length) + ' letters long.')
    
    while guesses > 0:
      print('-------------------------------------------------')
      print('You have ' + str(guesses) + ' guesses remaining.')
      print('Here are the available letters you may guess ' + get_available_letters(letters_guessed) + '.\n')
      guess = input('Please type in your guessed letter, or type * for a hint:')
      if guess == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        continue
      if guess not in string.ascii_lowercase:
        print('your guess must be a lowercase letter. Try again')
        continue
      letters_guessed.extend(guess)
      if guess in secret_word:
        print('You guessed a correct letter!')
      else:
        print('INCORRECT GUESS')
        guesses -= 1
      print(get_guessed_word(secret_word, letters_guessed))
      if is_word_guessed(secret_word, letters_guessed):
        print('YOU WIN')
        return
      
    print('You are out of guesses. you lose.')
    print('the word was ' + secret_word)


def test_hangman():
    #tests added
    assert is_word_guessed(secret_word, list(secret_word))
    assert is_word_guessed('hangman', list('hangma'))
    assert not is_word_guessed('abcd', list('abc'))

    assert get_guessed_word('apple',list('al')) == 'a _ _ l _'
    assert get_guessed_word('apple',list('bc')) == '_ _ _ _ _'
    assert get_guessed_word('apple',list('aple')) == 'a p p l e'
    assert get_guessed_word('apple',list('a')) != 'a p p l e'

    assert get_available_letters(list('abcdefghijklmnopqrstuvwxy')) == 'z'
    assert get_available_letters(list('a')) == 'bcdefghijklmnopqrstuvwxyz'

    assert match_with_gaps('a_t','act')
    assert match_with_gaps('a _ t','act')
    assert not match_with_gaps('a_t','bot')
    assert not match_with_gaps('a_t','boot')

    show_possible_matches('a_tigen')
    show_possible_matches('tige_')
    show_possible_matches('ta_')

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    
    #hangman(secret_word)
    hangman_with_hints(secret_word)

    #test_hangman()
