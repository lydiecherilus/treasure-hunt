from art_work import (treasure_island, hole, rhino, lake, alligator,
                      boat, house, congrats, fire, alien, ghost, duck)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print(treasure_island)

print("If you don't choose from the options presented you will lose.")
print("****")
input("Good luck! Press enter to start the game! \n")

game_end = False
while not game_end:
  # Player is presented by first set of choices.
  choice = input('You are at a crossroad. Where do you want to go? Type "left" or "right" \n')
  # If player's choice is right, the game will end.
  if choice.lower() == "right":
    print(hole)
    print("Sorry, You fell into a hole. Game Over.")
    print(rhino)
    print("Thank you for playing!")

  # If player's choice is left, the game will continue.
  # New choices will be presented to player.
  elif choice.lower() == "left":
    print(lake)
    
    # Player is presented the second set of choices.
    print("****")
    print("You have come to a lake. There is an island in the middle of the lake.")
    input('Are you a good swimmer? Type "Yes" or Type "No" \n')
    print("****")
    print("Do you want to swim or wait for a boat?")
    second_choice = input('Type "wait" to wait for a boat. Type "swim" to swim across. \n')

    # If player's choice is "swim", the game will end.
    if second_choice.lower() == "swim":
      print("****")   
      print(alligator)
      print("Sorry, you got eaten by an alligator.")
      print("Thank you for playing! ")

    # If player's choice is "wait", the game will continue and new choices will be presented.
    elif second_choice.lower() == "wait":
      print("****")
      print("Nice choice, here is a boat to help get you to the island!")
      print(boat)
      
      print("****")
      input('You arrive! Did you have a safe trip? Type "Yes" or Type "No" \n')
      # Player will be presented by new choices and the right choice will win the game!
      print(house)
      
      print("****")
      # Player is presented by third and last set of choices.
      third_choice = input("You are at the island. This house has 3 doors -- red, yellow & blue. Choose a color! \n")
    
      # If player's choice is "yellow", player wins the game!.
      if third_choice.lower() == "yellow":
        print(congrats)
        print("You found the treasure! You Win!")
        
        print("Congratulations!!! Thank you for playing! ")
      # If player's choice is "red", player loses the game!.
      elif third_choice.lower() == "red":
        print(" **** ")
        print(fire)
        print("It's a room full of fire. Game Over.")
        print("Thank you for playing!")

      # If player's choice is "blue", player loses the game!.
      elif third_choice.lower() == "blue":
        print(" **** ")   
        print(alien)
        print("You got attacked by alien. Game Over.")
        print("Thank you for playing!")

      # If player's choice is anything else, player also loses the game!.
      else:
        print(" **** ")
        print("You chose a door that doesn't exist. Game Over.")
        print(duck)
        print("Thank you for playing!")
      
    # If player's choice is not "swim" or "wait", the game will end.
    else:
      print(" **** ")
      print(ghost)
      print('You did not choose "swim" or "wait". You got attacked. Game Over.')
      print("Thank you for playing!")

  # If player's choice is not "left" or "right", the game will end.
  else: 
    print(" **** ")
    print(duck)
    print('You did not choose "left" or "right". Game Over.')
    print("Thank you for playing! ")

# option to restart the game.
  restart = input('Type "yes" if you want to play again -- otherwise type "no". \n')
  if restart == "no":
    game_end = True
    print("Goodbye")