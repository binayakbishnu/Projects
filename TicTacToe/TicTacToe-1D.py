print("Your board:\n")
print("__|__|__\n__|__|__\n  |  |  \n")

# number_board = [[str(i) for i  in range(j*3, (j+1)*3)] for j in range(3)]

# number_board = [[" " for i  in range(j*3, (j+1)*3)] for j in range(3)]

number_board = [[" " for i  in range(j*3, (j+1)*3)] for j in range(2)]
number_board += [[" " for i  in range(j*3, (j+1)*3)] for j in range(2, 3)]

for row in number_board:
        print('|'.join(row))

print(number_board)

player1 = 'X'
player2 = 'Y'

# board = [[0]*3]*3
# print(board)

player = 'X'
print("X goes first")

flag = 0
while flag == 0:
    # print("Enter your choice: ")
    row, column = input("Enter your choice {}: ".format(player)).split()
    row = int(row)
    column = int(column)
    if player == 'X':
        number_board[row-1][column-1] = 'X'
        player = 'Y'

    elif player == 'Y':
        number_board[row-1][column-1] = 'Y'
        player = 'X'

    # print(number_board)
    for row in number_board:
        print('|'.join(row))

    for row in number_board:
        if ''.join(row) == 'XXX':
            print("\nGame over\nX wins")
            flag = 1

        if ''.join(row) == 'YYY':
            print("\nGame over\nY wins")
            flag = 1


    s = ""
    for i in range(3):
        for j in range(3):
            if i == j:
                s += number_board[i][j]

    if s == 'XXX':
        print("\nGame over\nX wins")
        flag = 1

    if s == 'YYY':
        print("\nGame over\nY wins")
        flag = 1


    for j in range(3):
        s = ""
        for i in range(3):
            s += number_board[i][j]

        if s == 'XXX':
            print("\nGame over\nX wins")
            flag = 1

        if s == 'YYY':
            print("\nGame over\nY wins")
            flag = 1


    c = 3
    for row in number_board:
        if " " not in ''.join(row):
            c -= 1
    if c == 0:
        print("\nGame over\nDraw")
        flag = 1


# print(number_board)
print()
for row in number_board:
        print('|'.join(row))
