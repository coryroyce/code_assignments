# Open input file and read each line as a list
with open("221201_Code_Puzzles/day_02/input") as f:
    items = [item.rstrip().split(" ") for item in f]

"""
Part 1 Info:
A = Rock
B = Paper
C = Scissors

X = Rock
Y = Paper
Z = Scissors

Part 2 Info:
X = you need to lose
Y = you need to end the round in a draw
Z = you need to win
"""


def process():
    # Loop through each game and get the scores
    total_score = 0
    for game in items:
        game_score = calculate_round_score(game)
        total_score += game_score

    print(f"Total Score: \n{total_score}")

    # Part 2 Calculate score based on win lose info
    # Loop through each game and get the scores
    total_score_part_2 = 0
    for game in items:
        game_converted = convert_round_based_shape_to_play(game)
        game_score_2 = calculate_round_score(game_converted)
        total_score_part_2 += game_score_2

    print(f"Total Score Part 2: \n{total_score_part_2}")

    return


def convert_round_based_shape_to_play(single_round: list):
    my_play = ""
    opponent_play, game_outcome = single_round

    # Score the win, lose, draw points
    if opponent_play == "A":
        if game_outcome == "X":
            my_play = "Z"
        elif game_outcome == "Y":
            my_play = "X"
        else:
            my_play = "Y"
    elif opponent_play == "B":
        if game_outcome == "X":
            my_play = "X"
        elif game_outcome == "Y":
            my_play = "Y"
        else:
            my_play = "Z"
    elif opponent_play == "C":
        if game_outcome == "X":
            my_play = "Y"
        elif game_outcome == "Y":
            my_play = "Z"
        else:
            my_play = "X"

    converted_single_round = [opponent_play, my_play]

    return converted_single_round


def calculate_round_score(single_round: list):
    opponent_play, my_play = single_round

    win_lose_points = 0
    my_play_points = 0

    win = False
    lose = False
    draw = False

    # Score the win, lose, draw points
    if opponent_play == "A":
        if my_play == "X":
            draw = True
        elif my_play == "Y":
            win = True
        else:
            lose = True
    elif opponent_play == "B":
        if my_play == "X":
            lose = True
        elif my_play == "Y":
            draw = True
        else:
            win = True
    elif opponent_play == "C":
        if my_play == "X":
            win = True
        elif my_play == "Y":
            lose = True
        else:
            draw = True

    # Calculate points from win, lose, draw
    if lose:
        win_lose_points = 0
    elif draw:
        win_lose_points = 3
    if win:
        win_lose_points = 6

    # Calculate my guess points
    if my_play == "X":
        my_play_points = 1
    elif my_play == "Y":
        my_play_points = 2
    elif my_play == "Z":
        my_play_points = 3

    total_points = win_lose_points + my_play_points

    return total_points


if __name__ == "__main__":
    process()
