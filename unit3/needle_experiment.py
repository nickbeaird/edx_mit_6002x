import random
import math

def stdDev(L=None):
    if not L or len(L) < 1:
        return float('NaN')
    
    # Get the mean of the length of the words
    count = 0
    for number in L:
        count += number
    mean = count / len(L)

    # Compute the standard deviation using the mean
    numerator = 0
    for number in L:
        variance = (number - mean) ** 2
        numerator += variance

    std_dev = math.sqrt((numerator / len(L)))

    return std_dev

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y) **0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))


def getEstimate(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(curEst) +\
        ', Std. dev. = ' + str(round(sDev, 6))\
        + ' , Needles = ' + str(numNeedles))
    return (curEst, sDev)


def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEstimate(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

if __name__ == '__main__':
    random.seed(0)
    estPi(precision=0.005, numTrials=100)