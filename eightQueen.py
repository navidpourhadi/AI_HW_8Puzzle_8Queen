""""
Student : Navid pourhadi

this project implement for eight queen that execute by local searches to get the goal
algorithms: hillClimbing and simulate annealing

"""

import random, copy
import time


def createChess():
    temp = []
    for i in range(0, 8):
        temp.append([])
        for j in range(0, 8):
            temp[i].append(0)

    x = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        print "enter location of queens in each colomn:"
        x[i] = input()
        temp[i][x[i] - 1] = 1
    # for i in range(0, 8):
    #     y = random.randint(0, 7)
    #     putQueen(temp, i, y)
    #     location.append(y)
    return temp


def putQueen(array, x, y):
    array[x][y] = 1;


def printChess(Arr):
    temp = ""
    for i in range(0, 8):
        temp += "_____"
    temp += "\n"
    for j in range(0, 8):
        for i in range(0, 8):
            if Arr[i][j] == 1:
                temp += "| Q  "
            else:
                temp += "|    "
        temp += "| " + str(j + 1) + "\n"
        for i in range(0, 8):
            temp += "|____"
        temp += "|\n"
    print (temp)
    print("  1    2    3    4    5    6    7    8  ")


def move(array, m, n):
    for i in range(0, 8):
        if array[m][i] == 1:
            array[m][i] = 0
            array[m][n] = 1
    return array


def getSuccessors(problem):
    successors = []

    for i in range(0, 8):
        for j in range(0, 8):
            if problem[i][j] == 0:
                temp = copy.deepcopy(problem)
                move(temp, i, j)
                successors.append(temp)

    return successors


def heuristic(array):
    h = 0;
    for i in range(0, 8):
        for j in range(0, 8):
            if array[i][j] == 1:
                for m in range(i + 1, 8):
                    for n in range(0, 8):
                        if array[m][n] == 1:
                            if (j == n) | (m - i == j - n) | (m - i == n - j):
                                h = h + 1
    return h


def HillClimbing1(problem):
    for i in getSuccessors(problem):
        if heuristic(i)<heuristic(problem):
            problem = i;
            printChess(problem)
            problem = HillClimbing1(problem)
            break
    return problem


def HillClimbing2(array):
    min_h = 28
    min_x = 8
    min_y = 8
    m = 0
    temp = array
    h_array = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(0, 8):
        for j in range(0, 8):
            if temp[i][j] == 1:
                m = j
                h_array[i][j] = heuristic(temp)
                temp[i][j] = 0

        for k in range(0, 8):
            if k != m:
                temp[i][m] = 0
                temp[i][k] = 1
                h_array[i][k] = heuristic(temp)
                temp[i][k] = 0
                temp[i][m] = 1
    for i in range(0, 8):
        for j in range(0, 8):
            if h_array[i][j] < min_h:
                min_h = h_array[i][j]
                min_x = i
                min_y = j
    if min_h < heuristic(array):
        if array[min_x][min_y] == 0:
            print "huristic is -" + str(heuristic(array)) + "-  and minimum heuristic for next step is  " + str(
                min_h) + "\n\n\n\n"
            move(array, min_x, min_y)
            printChess(array)
            HillClimbing2(array)
    return array


def schedule(t):
    return t - t * .03


def simulated_annealing(problem, T, i):
    T = self.schedule(T)

    randomInput = random.randint(0, len(getSuccessors(problem)) - 1)
    randomeSuccessor = getSuccessors(problem)[randomInput]
    E = heuristic(problem) - heuristic(randomeSuccessor)
    if (E > 0):
        problem = randomeSuccessor

    elif uniform(0, 1) < math.exp(E / T):
        problem = randomeSuccessor

    printChess(problem)
    if heuristic(problem) == 0:
        return problem
    if i - 1 > 0:
        problem = simulated_annealing(problem, T, i - 1)

    return problem


# main
problem = createChess()
printChess(problem)

print "which algorithm:\n\n1-Hill Climbing with first better heuristic\n\n2-Hill Climbing with maximum slope\n\n3-Simulated annealing"
x = input()
if x == 1 :
    problem=HillClimbing1(problem)
if x == 3:
    problem=simulatedAnnealing(problem, 1)
if x == 2:
    problem=HillClimbing2(problem)

print "\n\n\n\n\n\n"
if heuristic(problem) == 0:
    print "******************we get the goal*****************"
else:
    print "goal not achieved :(((("

printChess(problem)
print "\n\n\n" + "heuristic of final step is :" + str(heuristic(problem)) + "\n\ncost of this game is :"

