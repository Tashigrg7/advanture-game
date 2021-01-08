
import time
import random


def print_sleep(string):
    print(string)
    time.sleep(2)


def intro():
    print_sleep("You find yourself standing in an open field, filled with grass and yellow wildflowers. ")
    print_sleep("Rumor has it that a wicked fairie is somewhere around here, "
                "and has been terrifying the nearby village....")
    print_sleep("There are two ways front of you right=house and left=cave\n"
                "Where would like to go?")

def options(items):
    choice = input("1.Enter 1 to knock on the door of the house\n"
                   "2.Enter 2 to peer into the cave. \n")

    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)

def house(items):
    print_sleep("You reach at the door\n"
                "dead man came out with gun\n"
                "This is horror house, he has no eye, mouth,nose\n"
                "body full of blood, trying to shoot you")
    choices = input("Would you like to do::::\n"
                    " (1) fight!!\n"
                    " (2) hide away!!")
    if choices == '1':
       fight(items)
    elif choices == '2':
         hide_away(items)

def hide_away(itmes):
    print_sleep("dead man has no nose but he smells much better")
    print_sleep("you are DEAD......\n"
                "GAME OVER...")
    play_again()

def fight(items):
    print_sleep("If you fight with dead man you need turn on light")
    print_sleep("dead man always scared with light ")

    choices = input("Would you like to \n"
                    "(1) 'turn on'\n"
                    "(2) standing")
    if choices=='1':
         turnon(items)
    elif choices =='2':
         standing(items)

def turnon(itmes):
    print_sleep("you are safe....you won the game..")
    play_again()

def standing(items):
    print_sleep("you are dead.........game over::")
    play_again()


def cave(items):
    print_sleep("You are inside the cave.")
    print_sleep("After a few moments, you find yourself "
                "near tiger, there are more than 10 tiger\n"
                " Tiger are coming near to you\n")
    choices = input("Would you like to____ \n"
                    "(1) throw rock___\n"
                    "(2) run away___")
    if choices == '1':
       throw_rock(items)
    elif choices == '2':
         run_away(items)
def throw_rock(items):
    print_sleep("tiger will attack you "
                "there are more than 10 tiger\n"
                "there is no chance. you DEAD")
    print_sleep("you lost the game!.....")
    play_again()

def run_away(items):
    print_sleep("you are safe because tiger are scare to go outside.")
    print_sleep("tiger mostly stay at cave.")
    play_again()


def play_again():
    option=input("Would you like to play again? (y/n)").lower()
    if option == "y":
       print_sleep("Excellent! Restarting the game..\n")
       play_game()
    elif option == "n":
       print_sleep("Thanks for playing! See you next time.\n")
       exit()
    else:

       play_again()




def play_game():
    items = []
    intro()
    options(items)

play_game()











