#!/usr/bin/python3
import random

class game():
    def __init__(self):
        self.selection = ['r', 'p', 's']
        self.human_answer = str(raw_input("Please choose something dummy\n"))
        self.computer_answer = self.get_computer_answer()
        self.who_won()

    def get_computer_answer(self):
        choice = random.choice(self.selection)
        print ("The computer chose " + choice)
        return choice

    def who_won(self):
        if self.human_answer == self.computer_answer:
            print('You tied')
        elif self.human_answer == 'r' and self.computer_answer == 's':
            print ('You win')
        elif self.human_answer == 'p' and self.computer_answer == 'r':
           print ('You win')
        elif self.human_answer == 's' and self.computer_answer == 'p':
            print ('You win')
        else:
            print('You lose')

if __name__=="__main__":
    play_again = True
    while play_again == True:
        new_game = game()
        reply = raw_input("Do you want to play again? (y/n)\n")
        if reply == 'n':
            play_again = False


        # print ("Do you want to play again")

