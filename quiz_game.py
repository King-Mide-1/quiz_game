print("Welcome to my computer game")
playing = input("Do you want to play: ")

if playing.lower() != "yes":
    quit()
print("Okay! let's play (level 1) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct! let's proceed to level 2")
    score += 1
else:
    print("Incorrect")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("correct! let's proceed to level 3")
    score += 1
else:
    print("Incorrect")
answer = input("What does CFR stand for? ")
if answer.lower() == "cost and freight":
    print("correct! let's proceed to level 4")
    score += 1
else:
    print("Incorrect")
answer = input("What does INCOTERMS stand for? ")
if answer.lower() == "international commercial terms":
    print("correct! let's proceed to level 5")
    score += 1
else:
    print("Incorrect")
answer = input("What does LPR stand for? ")
if answer.lower() == "local purchase requisition":
    print("Congratulations you have completed the game")
    score += 1
else:
    print("Incorrect")
print("You got " + str(score) + " questions correctly!")
print("Your total percentage is " + str((score / 6) * 100) + "%")
