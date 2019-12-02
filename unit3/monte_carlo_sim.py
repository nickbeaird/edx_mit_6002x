"""Return a Monte Carlo simulation from a previous HW assignment
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # The bucket starts with 3 Red and 3 Green balls
    bucket = ['R', 'R', 'R', 'G', 'G', 'G']
    all_one_color = 0

    # run simulation by numTrials
    for i in range(1, numTrials +1, 1):
        bucket_copy = bucket.copy()

        # list the items to grab
        for i in range(3):
            pick = random.randint(0, len(bucket_copy) - 1)
            bucket_copy.pop(pick)
        
        # count the number of times 3 Red balls were drawn
        green_total = 0
        red_total = 0
        for ball in bucket_copy:
            if ball == 'G':
                green_total += 1
            else:
                red_total += 1
        if (green_total == 3) or (red_total == 3):
            all_one_color += 1

    # return fraction of times 3 balls were drawn
    print('% times all Red balls drawn = :' \
        + str(all_one_color/float(numTrials)) \
        + ', out of a total trials = ' + str(numTrials))

    return all_one_color/float(numTrials)


if __name__ == '__main__':
    random.seed(0)
    print(noReplacementSimulation(100))
    print(noReplacementSimulation(1000))
    print(noReplacementSimulation(5000))