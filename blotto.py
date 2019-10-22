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


def factorial(x):

    # base case
    if x == 1:
        f = 1

    # for non-base cases, recursively calculate the factorial
    else:
        f = x * factorial(x - 1)

    return f


def choose(n, m):

    # for finding 'n choose m'
    a = factorial(n)
    b = factorial(m)
    c = factorial(n - m)
    d = b * c

    return int(a / d)


def generate_moves(S, N):
    with open("possible_moves.csv", 'w') as output:
        writer = csv.writer(output)
        last_strategy = []
        i = 0
        while i != choose(S + N - 1, N - 1):
            if i == 0:
                firstStrat = [0] * N
                firstStrat[0] = S
                last_strategy = firstStrat
                writer.writerow(last_strategy)
                i += 1
            else:
                strategy = []
                for k in last_strategy:
                    strategy.append(k)
                if strategy[N - 2] != 0:
                    strategy[N - 2] += -1
                    strategy[N - 1] += 1
                else:
                    j = 1
                    while strategy[N - 2 - j] == 0:
                        j += 1
                    if N - 2 - j == 0:
                        strategy[0] += -1
                        strategy[1] = strategy[N - 1] + 1
                        strategy[N - 1] = 0
                    else:
                        strategy[N - 2 - j] += -1
                        strategy[N - 2 - j + 1] += 1
                last_strategy = strategy
                writer.writerow(strategy)
                i += 1


def main():
    generate_moves(100, 10)


if __name__ == "__main__":
    main()
