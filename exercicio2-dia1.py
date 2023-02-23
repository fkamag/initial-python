entrada = [ [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0],
          ]

# resultado para (0, 4) = True
# resultado para (1, 1) = False

# print(entrada[0][4])
# print(entrada[1][1])

def naval_battle(board, line, column):
    if (board[line][column] == 1):
        return True
    return False

print(naval_battle(entrada, 0, 4))
print(naval_battle(entrada, 1, 1))
