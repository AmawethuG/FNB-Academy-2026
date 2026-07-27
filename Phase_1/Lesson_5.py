#The High-Score Tracker Game

while True:
    score = input("Enter your score or type 'stop' to exit: ")
    if score.lower() == 'stop':
        print("Game session ended! ")
        break
    else:
        score = int(score)
        if score >= 100:
            print("Wow! That’s a new high score!")
        else:
            print("Good try, keep playing!")

    