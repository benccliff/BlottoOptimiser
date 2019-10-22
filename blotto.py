import csv


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


def generate_moves(castles, soldiers):
    if castles == 1:
        return [[soldiers]]
    else:
        possible_moves = []
        possible_first_castle = [soldiers-i for i in range(soldiers+1)]
        for first_castle in possible_first_castle:
            submoves = generate_moves(castles-1, soldiers-first_castle)
            for submove in submoves:
                submove_copy = submove.copy()
                submove_copy.insert(0, first_castle)
                possible_moves.append(submove_copy)
        return possible_moves


def write_moves_to_file():
    castles = 10
    soldiers = 100
    possible_moves = generate_moves(castles, soldiers)
    with open("possible_moves.csv", 'w') as output:
        writer = csv.writer(output)


def main():
    write_moves_to_file()


if __name__ == "__main__":
    main()
