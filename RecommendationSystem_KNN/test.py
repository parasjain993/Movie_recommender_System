import csv
import math
import operator

def preprocess(filename, trainingSet=[], testSet=[]):
    with open(filename, 'trainingSet') as csvfile:
        lines = csv.reader(csvfile)
        print(type(lines))
        dataset = list(lines)
        rows = len(dataset)
        cols = len(dataset[0])
        for x in range(rows - 1):
            for y in range(cols):
                dataset[x][y] = float(dataset[x][y])
            if x < (rows * 0.8):
                trainingSet.append(dataset[x])
            else:
                dataset[x][cols-1] = 0
                testSet.append(dataset[x])


def evaleuclidean(inp1, inp2, dim):
    distance = 0
    for x in range(dim):
        distance += pow((inp1[x] - inp2[x]), 2)
    return math.sqrt(distance)


def KNN(trainingSet, input, k):
    distances = []
    length = len(input) - 1
    for x in range(len(trainingSet)):
        dist = evaleuclidean(input, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def main():
    trainingSet = []
    testSet = []
    preprocess('trainingSet.xls', trainingSet, testSet)
    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))
    k = 4
    predict = 0
    col = len(testSet[0])
    for x in range(len(testSet)):
        neighbors = KNN(trainingSet, testSet[x], k)
        for y in range(len(neighbors)):
            predict += neighbors[y][col-1]
        predict /= k
        print((x+1) + '. test sample prediction -> ' + predict)

main()
