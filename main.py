import random

gamelist = ["R", "P", "S"]


#check the user's input

userInput = input("Pick an option between R, P or S: ").upper()

while userInput.rstrip() not in gamelist:
    print("Not a valid value")
    userInput = input("Pick an option between R, P or S: ").upper()

#Rock beats Scissors
#Paper beats Rock
#Scissors beats Paper

#computer value

computerValue = random.choice(gamelist)
print("Computer chose " + computerValue)

if computerValue == userInput:
    print("There is a tie")

elif computerValue == "R" and userInput == "S":
    print("Computer Wins!")
    
elif computerValue == "P" and userInput == "R":
    print("Computer Wins!")
    
elif computerValue == "S" and userInput == "P":
    print("Computer Wins!")
          
elif userInput == "R" and computerValue == "S":
    print("You win!")
    
elif userInput == "P" and computerValue == "R":
     print("You win!")
     
elif userInput == "S" and computerValue == "P":
    print("You win!")


