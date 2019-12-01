"""Taken from Ch.15 Figure 15.6
"""

def getHorizontalSpeed(a, b, c, minX, maxX):
    """Assumes minX and maxX are distances in inches
    Returns horizontal speed in feet per second.
    """

    inchesPerFoot = 12.0
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*inchesPerFoot  # accel. of gravity in inches/sec/sec
    t = (2*yPeak/g)**0.5
    print('Horizontal speed =', int(xMid/t(*inchesPerFoot)), 'feet/sec')