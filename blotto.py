import random


def find_winner(pairOne, pairTwo):
    indexOne, moveOne = pairOne
    indexTwo, moveTwo = pairTwo
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
        return indexOne
    elif playerTwoScore > playerOneScore:
        return indexTwo
    else:
        return None


def play_tournament(strategies):
    combinations = []
    victories = [0 for i in range(10)]
    n = len(strategies)
    for i in range(n):
        for j in range(i+1, n):
            combinations.append([(i, strategies[i]), (j, strategies[j])])
    for combo in combinations:
        winner = find_winner(combo[0], combo[1])
        if winner:
            victories[winner] += 1
    winners = [0, 1]
    for i in range(2, 10):
        if victories[i] > victories[winners[0]]:
            winners.remove(winners[0])
            winners.append(i)
        elif victories[i] > victories[winners[1]]:
            winners.remove(winners[1])
            winners.append(i)
    return [strategies[k] for k in winners]


def generate_initial_strategies():
    strategies = []
    for i in range(10):
        current_strategy = [0 for i in range(10)]
        sum = 0
        for j in range(10):
            r = random.randint(0, 25)
            sum += r
            if sum <= 100:
                current_strategy[j] = r
            else:
                break
        if sum < 100:
            current_strategy[0] += 100 - sum
        random.shuffle(current_strategy)
        strategies.append(current_strategy)
    return strategies


def main():
    strategies = generate_initial_strategies()
    winners = play_tournament(strategies)
    print(winners)


if __name__ == "__main__":
    main()
