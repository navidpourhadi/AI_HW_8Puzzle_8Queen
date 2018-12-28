""""
Student : Navid pourhadi

this project implement for eight puzzle that execute by local searches to get the goal
algorithms: hillClimbing and simulate annealing

"""

import copy,time , math ,random

goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
def CreatePuzzle():

    puzzle = []
    for i in range(0,3):
        puzzle.append([])
        for j in range(0,3):
            print "enter value of ("+str(i)+","+str(j)+")tile (from 0 to 9) :"
            x=input()
            puzzle[i].append(str(x))

    return puzzle



def isgoal(array):
    if array == goal :
        return True



def getSuccessors(array):
    successors = []
    for i in range(0,3):
        for j in range(0,3):
            if array[i][j]== '0' :
                if j != 0 :
                    temp1 = copy.deepcopy(array)
                    temp1[i][j] = temp1[i][j-1]
                    temp1[i][j-1] = '0'
                    successors.append(temp1)

                if i != 0 :
                    temp1 = copy.deepcopy(array)
                    temp1[i][j] = temp1[i-1][j]
                    temp1[i-1][j] = '0'
                    successors.append(temp1)


                if j != 2 :
                    temp1 = copy.deepcopy(array)
                    temp1[i][j] = temp1[i][j+1]
                    temp1[i][j+1] = '0'
                    successors.append(temp1)

                if i != 2 :
                    temp1 = copy.deepcopy(array)
                    temp1[i][j] = temp1[i+1][j]
                    temp1[i+1][j] = '0'
                    successors.append(temp1)

    return successors




def printPuzzle(puzzle):
    for i in range(0,3):
        print puzzle[i][0]+'  '+puzzle[i][1]+'  '+puzzle[i][2]
    print "\n heuristic = "+str(manhattan(puzzle))

    print '________________\n'



def manhattan(puzzle):

    mDistance = 0
    puzzleContents = ['1', '2', '3', '4', '5', '6', '7', '8']
    # search through the numbers in the puzzle
    for x in puzzleContents:
        for i in range(0,3):
            for j in range(0,3):
                # get where the number should be
                if x == goal[i][j]:
                    goalRow = i
                    goalCol = j
                # get where the number is now
                if x == puzzle[i][j]:
                    puzzleRow = i
                    puzzleCol = j
        # calculate the Manhattan Distance based on the points (row/col)
        mDistance += (abs(goalRow - puzzleRow) + abs(goalCol - puzzleCol))

    return mDistance


def hillClimbing1(puzzle):
    for i in getSuccessors(puzzle):
        if manhattan(puzzle) > manhattan(i):
            puzzle = i
            printPuzzle(puzzle)
            hillClimbing1(puzzle)
            break
    return puzzle


def hillClimbing2(puzzle):
    heur = []
    for i in range(0,len(getSuccessors(puzzle))):
        heur.append(manhattan(getSuccessors(puzzle)[i]))
    min_h = 0
    for i in range(0,len(heur)):
        if heur[i] < heur[min_h] :
            min_h = i
    if manhattan(puzzle) > manhattan(getSuccessors(puzzle)[min_h]):
        puzzle = getSuccessors(puzzle)[min_h]
        printPuzzle(puzzle)
        puzzle=hillClimbing2(puzzle)
    return puzzle



def schedule(T):
    return T - T * 0.1


def simulatedAnnealing(puzzle,T,i):
    T = schedule(T)
    randomInput = random.randint(0, len(getSuccessors(puzzle)) - 1)
    randomSuccessor = getSuccessors(puzzle)[randomInput]

    E = manhattan(puzzle)-manhattan(randomSuccessor)
    if E > 0 :
        puzzle = randomSuccessor
    elif random.uniform(0,1) < math.exp(E/T):
        puzzle =randomSuccessor

    printPuzzle(puzzle)
    if i-1 > 0 :
        puzzle = simulatedAnnealing(puzzle,T,i-1)

    return puzzle








puzzle = CreatePuzzle()

print "enter which algorithm ? \n1-hill climbing with first better heuristic\n2-hill climbing with best heuristic\n3-simulated annealing"
x=input()


if x==1 :
    puzzle = hillClimbing1(puzzle)
if x==2 :
    puzzle = hillClimbing2(puzzle)
if x==3 :
    puzzle = simulatedAnnealing(puzzle,100,100)




if isgoal(puzzle):
    print "\n\n\n\n*************** WE GET THE GOAL *****************\n"
    printPuzzle(puzzle)
else:
    print "\n\n\n\n\goal not achieved :((((((((((\n"
    printPuzzle(puzzle)

