import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    same_colors_drawn = 0
    for trial in range(numTrials):
        balls = [0, 0, 0, 1, 1, 1]
        drawn_balls = []
        for draw in range(0, 3):
            ball = balls.pop(random.randrange(0, len(balls)))
            print(balls)
            print("draw:", draw)
            drawn_balls.append(ball)
        if len(set(drawn_balls)) == 1:
            same_colors_drawn += 1

    return same_colors_drawn / numTrials



print(noReplacementSimulation(10))