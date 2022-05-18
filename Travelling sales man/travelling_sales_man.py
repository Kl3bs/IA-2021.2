import random


def validState(solution, matrix):
    for i in range(len(solution)-1):
        if(matrix[solution[i]][solution[i+1]] != -1):

            i = i+1
        else:

            return 0

    return 1


def randomSolution(matrix):
    cities = list(range(len(matrix)))
    solution = []

    for i in range(len(matrix)):
        randomCity = cities[random.randint(0, len(cities) - 1)]

        solution.append(randomCity)
        cities.remove(randomCity)

    if (validState(solution, matrix)):

        return solution

    else:
        return randomSolution(matrix)


def routeLength(matrix, solution):
    routeLength = 0

    for i in range(len(solution)):
        routeLength += matrix[solution[i - 1]][solution[i]]
    return routeLength


def getNeighbours(solution, matrix):
    neighbours = []

    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]

            if(validState(neighbour, matrix)):
                neighbours.append(neighbour)
            else:

                i = i+1

    return neighbours


def getBestNeighbour(matrix, neighbours):
    bestRouteLength = routeLength(matrix, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(matrix, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength


def hillClimbing(matrix):
    currentSolution = randomSolution(matrix)
    currentRouteLength = routeLength(matrix, currentSolution)
    neighbours = getNeighbours(currentSolution, matrix)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(
        matrix, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution, matrix)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(
            matrix, neighbours)

    for i in range(len(currentSolution)):
        print("C", currentSolution[i] + 1, " ", end='', sep='')

    print("\nTotal cost = ", currentRouteLength)

    return currentSolution, currentRouteLength


def main():

    matrix = [[0, 30, 84, 56, -1, -1, -1, 75, -1, 80],
              [30, 0, 65, -1, -1, -1, 70, -1, -1, 40],
              [84, 65, 0, 74, 52, 55, -1, 60, 143, 48],
              [56, -1, 74, 0, 135, -1, -1, 20, -1, -1],
              [-1,  -1, 52, 135, 0, 70, -1, 122, 98, 80],
              [70, -1, 55, -1, 70, 0, 63, -1, 82, 35],
              [-1, 70, -1, -1, -1, 63, 0, -1, 120, 57],
              [75, -1, 135, 20, 122, -1, -1, 0, -1, -1],
              [-1, -1, 143, -1, 98, 82, 120, -1, 0, -1],
              [80, 40, 48, -1, 80, 35, 57, -1, -1, 0]]

    hillClimbing(matrix)


if __name__ == "__main__":
    main()
