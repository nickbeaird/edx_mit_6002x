
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pylab

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        # import pdb; pdb.set_trace()
        x, m = line.split(' ')
        distances.append(float(x))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def plotData(inputFile):
    masses, distances = getData(inputFile)
    masses = pylab.array(masses)
    distances = pylab.array(distances)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo', 
                label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    pylab.show()


def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo', 
                label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    # find linear fit
    a, b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a * pylab.array(forces) + b
    k = 1.0/a
    pylab.plot(forces, predictedDistances,
                label = 'Displacements predicted by\nlinear fit, k = '
                + str(round(k, 5)))
    pylab.legend(loc = 'best')
    pylab.show()


def fitDataWithCubic(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo', 
                label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    # find linear fit
    a, b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a * pylab.array(forces) + b
    k = 1.0/a
    pylab.plot(forces, predictedDistances,
                label = 'Displacements predicted by\nlinear fit, k = '
                + str(round(k, 5)))
    a,b,c,d = pylab.polyfit(forces, distances, 3)
    predictedDistances = a*(forces**3) + b*forces**2 + c**forces + d
    pylab.plot(forces, predictedDistances, 'b:', label = 'cubic fit')
    pylab.legend(loc = 'best')
    pylab.show()


if __name__ == '__main__':
    print(getData('spring_data.txt'))
    plotData('spring_data.txt')
    fitData('spring_data.txt')
    fitDataWithCubic('spring_data.txt')

