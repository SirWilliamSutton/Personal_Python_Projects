game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_baord(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print('   0  1  2')
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate (game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: Make sure you input row/column as 0 1 or 2?", e)

game = game_baord(game, player=1, row=2, column=1)

