from time import time


def find_winner(moveOne, moveTwo):
    playerOneScore = 0
    playerTwoScore = 0
    castle = 0
    while playerOneScore < 20 and playerTwoScore < 20 and castle < 10:
        if moveOne[castle] > moveTwo[castle]:
            playerOneScore += castle + 1
        elif moveOne[castle] < moveTwo[castle]:
            playerTwoScore += castle + 1
        castle += 1
    if playerOneScore > playerTwoScore:
        print("Player one wins!")
    elif playerTwoScore > playerOneScore:
        print("Player two wins!")
    else:
        print("It's a tie!")
    return playerOneScore, playerTwoScore


def generate_strategies(castles, soldiers):
    if castles == 1:
        return [[soldiers]]
    else:
        possible_moves = []
        possible_first_castle = [soldiers-i for i in range(soldiers+1)]
        for first_castle in possible_first_castle:
            submoves = generate_strategies(castles-1, soldiers-first_castle)
            for submove in submoves:
                submove_copy = submove.copy()
                submove_copy.insert(0, first_castle)
                possible_moves.append(submove_copy)
        return possible_moves