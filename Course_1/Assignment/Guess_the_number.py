# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

secret_number = 0
number_guess = 0

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_range
    max_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_range
    max_range = 1000
    new_game()
    
    
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, max_range)
    global number_guess
    number_guess = int(math.log(max_range, 2))+ 1
    print "New game."
    print "Range is [0,"+ str(max_range) +")"
    print "Number of remaining guesses is "+ str(number_guess)
    print "\n"

    
def input_guess(guess):
    # main game logic goes here	
    guess = float(guess)
    global number_guess
    number_guess -=1
    if number_guess == 0:
        print "\n"
        print "Guess was " + str(guess)
        print "Number of remaining guess is " + str(number_guess)
        print "You ran out of guesses. The number was " + str(secret_number)
        print "\n"
        new_game()
    elif guess not in range(0, max_range+1):
        print "\n"
        print "Guess was "+ str(guess)
        print "Number of remaining guess is " + str(number_guess)
        print "Out of guess!"
    elif secret_number > guess:
        print "\n"
        print "Guess was "+ str(guess)
        print "Number of remaining guess is " + str(number_guess)
        print "Higher!"
    elif secret_number < guess:
        print "\n"
        print "Guess was "+ str(guess)
        print "Number of remaining guess is " + str(number_guess)
        print "Lower!"
    elif secret_number == guess:
        print "\n"
        print "Guess was "+ str(guess)
        print "Number of remaining guess is " + str(number_guess)
        print "Correct!" 
        print "\n"
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)
frame.add_button("Range [0,100)", range100, 200)
frame.add_button("Range [0,1000)", range1000, 200)
frame.add_input("Enter the guess!", input_guess, 100)

# register event handlers for control elements and start frame
frame.start()

range100()

#ember to check your completed program against the grading rubric
