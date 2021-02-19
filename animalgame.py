import random

print ("There are 4 animal categories to choose from:" + " " + "Farm, Wild, Pets & Sea")
user = input("Choose your category:")

Farm = ["Cow","Rabbit","Duck","Shrimp","Pig","Bee","Goat","Deer","Sheep","Fish","Chicken","Horse"]
Wild = ["Monkey","Panda","Zebra","Leopard","Wolf","Eagle","Crab","Giraffe","Camel","Owl","Tiger","Bear","Lion","Elephant","Squirrel","Snake"]
Pets = ["Cat","Dog","Bird","Rabbit","Fish","Turtle","Mouse","Parrot","Hamster"]
Sea =  ["Fish","Seal","Octopus","Shark","Starfish","Whale","Penguin","Jellyfish","Squid","Lobster","Shrimp","Dolphin","Shells"]


hint_Farm = {"Cow":"Makes a distinct sound","Duck":"Has a certain type of feet","Shrimp":"Eaten in chinese food","Pig":"Pink in colour","Bee":"Can hurt you","Goat":"Can get cheese from it","Deer":"Can run out onto roads suddenly","Sheep":"Can use its hair","Chicken":"Tasty dinner!","Horse":"Can ride on it"}
hint_Wild = {"Monkey":"Climbs trees","Panda":"Big, cuddly giant","Zebra":"Has a distinct pattern","Leopard":"Spotty pattern","Wolf":"Very Scary!","Eagle":"Lethal Flying animal","Crab":"Have a 10 toe","Giraffe":"Very Long Animal","Camel":"Has a giant back","Owl":"Stays up through the night","Tiger":"Ferocious cat","Bear":"Big Scary animal","Lion":"Has a loud voice","Elephant":" Largest animal in the wolrd","Squirrel":"Eat nuts","Snake":"Moves sneakily"}
hint_Pets = {"Cat":"Has whiskers","Dog":"Makes a distinct noise","Bird":"Flies","Rabbit":"Hops","Fish":"Swims","Turtle":"Moves Slowly","Mouse":"Small animal","Parrot":"Can be different colours","Hamster":"Rolls around on a wheel"}
hint_Sea = {"Fish":"Has Fins","Seal":"Has Whiskers","Octopus":"Has at 8 legs","Shark":"Has Very Sharp teeth!","Starfish":"Has a certain shape","Whale":"One of the biggest animals in the world","Penguin":"It waddles","Jellyfish":"Can Sting you","Lobster":"Posh food to eat", "Squid":"","Dolphin":""}


if user == "Farm" or user == "farm":
    print ("These are all the options you have to choose from" + "\n" + str(Farm))
    print ()
    print ("You have 5 guesses and 1 hint available to use" + "\n" + "To use your hint type 'hint'")
    print ("A hint uses 1 life!")
    answer = random.choice(Farm)
    attempts_left = 4
    i = 1
    while i < 6:
        guess = input("Attempt" + " " + str(i) + ":")
        if guess == "hint":
            print (hint_Farm[answer])
        elif guess == answer.lower() or guess == answer:
            print ("Well done! You got the right animal")
            break
        elif attempts_left == 1:
            print ("This is your last attempt! Choose Wisely")
        elif i != 5:
            print ("Unlucky, Try again" + " " + str(attempts_left) + " " + "attempts left")
        else:
            print ("Hard luck! You didn't defeat the game this time.")
        attempts_left -= 1
        i += 1


elif user == "Wild" or user == "wild":
    attempts_left = 8
    print ("These are all the options you have to choose from" + "\n" + str(Wild))
    print ()
    print ("You have 10 guesses and 1 hint available to use" + "\n" + "To use your hint type 'hint'")
    answer = random.choice(Wild)

    i = 1
    while i < 10:
        guess = input("Attempt" + " " + str(i) + ":")
        if guess == "hint":
            print (hint_Wild[answer])
        elif guess == answer.lower() or guess == answer:
            print ("Well done! You got the right animal")
            break
        elif attempts_left == 1:
            print ("This is your last attempt! Choose Wisely")
        elif i != 9:
            print ("Unlucky, Try again" + " " + str(attempts_left) + " " + "attempts left")
        else:
            print ("Hard luck! You didn't defeat the game this time.")
        attempts_left -= 1
        i += 1


elif user == "Pets" or user == "pets":
    attempts_left = 2
    print ("These are all the options you have to choose from" + "\n" + str(Pets))
    print ()
    print ("You have 3 guesses")
    answer = random.choice(Pets)

    i = 1
    while i < 4:
        guess = input("Attempt" + " " + str(i) + ":")
        if guess == "hint":
            print (hint_Pets[answer])
        if guess == answer.lower() or guess == answer:
            print ("Well done! You got the right animal")
            break
        elif attempts_left == 1:
            print ("This is your last attempt! Choose Wisely")
        elif i != 5:
            print ("Unlucky, Try again" + " " + str(attempts_left) + " " + "attempts left")
        else:
            print ("Hard luck! You didn't defeat the game this time.")
        attempts_left -= 1
        i += 1


else:
    attempts_left = 7
    print ("These are all the options you have to choose from" + "\n" + str(Sea))
    print ()
    print ("You have 8 guesses and 1 hint available to use" + "\n" + "To use your hint type 'hint'")
    answer = random.choice(Sea)

    i = 1
    while i < 9:
        guess = input("Attempt" + " " + str(i) + ":")
        if guess == "hint":
            print (hint_Sea[answer])
        elif guess == answer.lower() or guess == answer:
            print ("Well done! You got the right animal")
            break
        elif attempts_left == 1:
            print ("This is your last attempt! Choose Wisely")
        elif i != 8:
            print ("Unlucky, Try again" + " " + str(attempts_left) + " " + "attempts left")
        else:
            print ("Hard luck! You didn't defeat the game this time.")
        attempts_left -= 1
        i += 1
print("Thanks for playing! Hope you enjoyed!")
