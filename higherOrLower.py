import random
totalTurns = 0
averagePerTurn = 0
highestGuessingValue = 100000000
timesRun = 100000
highestRounds = 0


def play(x):
    global totalTurns, highestRounds
    for y in range(1,timesRun):
        rounds = 0
        low = 1
        high = x
        computerGuess = 0
        number = random.randint(low, high)
        while number != computerGuess:
            computerGuess = random.randint(low, high)
            if computerGuess > number:
                rounds = rounds + 1
                high = computerGuess-1
            elif computerGuess < number:
                rounds = rounds + 1
                low = computerGuess+1
            else:
                rounds = rounds + 1
        if rounds >= highestRounds:
            highestRounds = rounds
        totalTurns = totalTurns + rounds
        averagePerTurn = totalTurns / y
        if y % 1000 == 0:
            print(y)
    print(f'The new Total Turns are: {totalTurns}')
    print(f'The average amount of turns are: {averagePerTurn}')
    print(f'The highest attempt took {highestRounds} rounds!')




play(highestGuessingValue)
