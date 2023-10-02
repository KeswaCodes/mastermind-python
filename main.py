'''
this module is a mock of the mastermind game created by zinksw@gmail.com
'''
import random
import time
import sys

def game_obj_display():

    print('      WELCOME TO THE MASTERMIND MOCK BY ZINKSW@GMAIL.COM     ')
    time.sleep(2)
    print('OBJECTIVE: ')

    print('   	- to guess the random number set by the computer in order to be crowned mastermind')
    print('   	- enter one value only')
    print(' 	- for the first round, the user will be asked to enter a range of the numbers of the random number')
    print(' 	- with unlimited guesses, the user can guess as many times what the random chosen number is')
    print(' 	- once the number has been guessed then the user has the option to decide whether or not they would like to play again')
    print('        - the game cannot be played with negative numbers')
    print('        - to quit the game, you can simply just enter "q" or "exit" ')
    print('        - ENJOY !')

def generate_num():
    '''
    generate_num() is a function that generates a random number within a given index and returns the number generated

    min (int) is the minimum value of the range to generate a value within 
    max (int) is the maximum value for the range 


    '''
    value = str(random.randint(100, 10000))
    return value

def gen_rand_fill_num(random_number):
    '''
    gen_rand_fill_num is a function that generates a non filled number of the random number chosen
    this function returns the filled number, ie if the number is 1234 this function will return XXXX
    
    random_number (int) is the random number chosen 
    '''

    rand_list = []
    
    for i in random_number:
        rand_list.append('X')

    return ''.join(rand_list)

def get_guess(random_number):
    '''
    get_guess is a function that takes input from user, validates it and uses it to perform specific actions 
    
    random_number is the filled number that has to be guessed
    
    '''
    guess = input('Please enter a guess: ')

    if guess.lower() == 'q' or guess.lower() == 'exit':
        quit_game()
    else:

        if guess.isdigit() and len(guess) == 1:
            return guess
        else:
            print('Invalid input, please enter a valid input!!\n')
            get_guess(random_number)

    return guess


def check_double_values(user_guess, random_number, filled_number):
    '''
    check_double_values is a function that checcontrol_play_again
    '''
    r_list = make_list(random_number)

    for number in filled_number:
        if number in r_list:
            r_list.remove(number)
    
    if user_guess in r_list:
        return True

    else:
        return False


def make_list(iterable):
    '''
    make_list is a function that creates a list from the iterable given
    
    iterable () can be of any type, just as long as it is an iterable
    this function returns the list generated
    '''
    result = []
    for i in iterable:
        result.append(i)
    
    return result

def fill_in_guess(user_guess, random_value, filled_number):
    '''
    fill_in_guess is a function that fills in the user's correct guess in the correct index
    
    user_guess (str) is the user's guess
    random_value (str) is the random code generated
    filled_number (str) is the filled in number that the user has to guess
    '''

    # make_list is a function that creates a list
    answer_list = make_list(random_value)
    filled_list = make_list(filled_number)

    occurance = answer_list.count(user_guess)

    for i in range(occurance):
        index = answer_list.index(user_guess)
        answer_list[index] = '#'
        filled_list[index] = user_guess

    # return a string of the filled list of characters
    return ''.join(filled_list)


def check_play_again():
    '''
    check_play_again is a function that checks whether the user wants to play again or not 
    
    this function returns a boolean; true if the user wants to play again, else quits the game
    '''
    otpt = input("Would you like to play again? (y/n) ")
    otpt = otpt.lower().strip()

    if otpt == 'y' or otpt == 'yes' or otpt == '':
        return True
    return False

    


def run_game(random_number, filled_number):
    
    print(random_number)
    print("What's the number?:", filled_number)
    while True:

        guess = get_guess(random_number)
        if check_double_values(guess, random_number, filled_number) is True:
            filled_number = fill_in_guess(guess, random_number, filled_number)
            print('Good guess !!!')
            print('Guess the number: ', filled_number)
            
            if 'X' in filled_number:
                pass
            else:
                break
        
        else:
            print('Try again...')
            run_game(random_number, filled_number)
    

    print('Congratulations. You are the mastermind!!!')
    
    result = check_play_again()
    random_num = control_play_again(result)
    filled_num = gen_rand_fill_num(random_num)

    run_game(random_num, filled_num)
    return result # check_play_again()

def quit_game():
    print('Terminating game...')
    time.sleep(1)
    print('Bye!')
    sys.exit(0)

def make_list_numbers():

    num_list = []
    for i in range(30):
        number = random.randint(1000, 10000)
        if number not in num_list:
            num_list.append(number)

    return num_list


def choose_number(number_list):
    index = random.randint(0, 29)
    return number_list[index]

def control_play_again(repeat):
    if repeat is True:
        num_list = make_list_numbers()
        return str(choose_number(num_list))
    else:
        quit_game()
    

if __name__ == '__main__':
    
    print('Starting the mastermind game...')
    time.sleep(1)
    game_obj_display()
    print()
    print('Disclaimer!!!! The min and max values will only be set once throughout the game')

    # min_val, max_val = min_max_user()
    ran_num = generate_num()
    randomly_fill_num = gen_rand_fill_num(ran_num)

    run_game(ran_num, randomly_fill_num)