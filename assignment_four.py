import random
def get_card():
   k = random.randint(1,10)
   return(k)
def get_winner(ut,dt):
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
   print(k)
   if k == yes:

main()



# def get_winner(ut,pt):
#     if ut > pt
#     and ut< 21