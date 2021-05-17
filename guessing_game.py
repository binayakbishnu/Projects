word = "etch"

guessed = ""

attempts=0
while guessed != word:
    if attempts >= 5:
        print("\nAttempts over\nTry next time")
        exit(0)
    
    letter=0
    position=0
    guessed = input("Enter guess: ")

    for i in guessed:
        for j in word:
            if i == j and guessed.index(i)!=word.index(j):
                letter+=1
            elif i ==j and guessed.index(i) == word.index(j):
                position+=1

    print(f"Letter matched but not position: {letter}")
    print(f"Letter and position matched: {position}")
    print(f"Letter not at all matched: {len(word)-(letter+position)}")
    
    attempts+=1
    


print(f"\nWell Played\n{attempts} attempts")