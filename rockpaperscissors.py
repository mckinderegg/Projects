import random

print ('Welcome to Rock, Paper, Scissors \n To leave the game type "end()" \n Pick your weapon:')
user_input = input()
CPU_total = 0
User_total = 0
game = ['Rock', 'Paper', 'Scissors']
while user_input != "end()":
    CPU_pick = random.choice(game)
    print ("You:" + user_input)
    print ("Computer:" + CPU_pick)
    if user_input == game[0] and CPU_pick == game[1]:
        print ("Computer won a point, try again..")
        CPU_total += 1
    elif CPU_pick == game[0] and user_input == game[1]:
        print ("Well done you won a point, go again!")
        User_total += 1
    elif user_input == game[0] and CPU_pick == game[2]:
        print ("Well done you won a point, go again!")
        User_total += 1
    elif CPU_pick == game[0] and user_input == game[2]:
        print ("Computer won a point, try again..")
        CPU_total += 1
    elif user_input == game[1] and CPU_pick == game[2]:
        print ("Well done you won a point, go again!")
        User_total += 1
    elif CPU_pick == game[1] and user_input == game[2]:
        print ("Computer won a point, try again..")
        CPU_total += 1
    else:
        print ("Go again, you both got", user_input)
    print ("Pick Another Weapon:")
    user_input = input()

print ("Total scores are:" + "\n" + "Computer:", str(CPU_total) + "\n" "You:", str(User_total))
if User_total > CPU_total:
    print ("Congratulations you won the game!")
elif User_total == CPU_total:
    print ("Well Done you tied with the computer")
else:
    print ("Better Luck Next Time!")
print ("Thanks for playing")
