# Halley Deme
# Last Edit : October 19
# This program is a blackjack simulator.


# this is used for the get card function in order to retrieve a random number betweeen 1-10
import random

def get_card():
   """
This function is used to get a random card.
   :return: returns a card valued between 1-10
   """
   k = random.randint(1,10)
   return(k)
def get_winner(ut,dt):
   """
   This function compares the user and dealer's total and decides who wins.
   :param ut: This is the user's total
   :param dt: This is the dealer's total
   :return: This says who has the greater total therefore winning.
   """
   if ut> dt:
      return "you won!"
   if dt>ut:
      return "sorry,dealer won :("
   if dt==ut:
      return "It's a tie!"

def main():
   user_total = 0
   user_total = user_total + get_card()
   user_total += get_card()
   print("your total is now " + str(user_total))
   k = input( "would you like another card?")

   if k =="yes" :
      user_total += get_card()
      print("your total is now " + str(user_total))
   if user_total > 21:
      print("Your total is greater than 21, you lost.")
   else:
      dealer_total = 0
      dealer_total= dealer_total + get_card()
      dealer_total+= get_card()
      print("The dealer's total is " + str(dealer_total))
      print(get_winner(user_total,dealer_total))





main()



