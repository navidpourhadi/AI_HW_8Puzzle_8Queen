""""
Student : Navid pourhadi

this project implement for eight puzzle that execute by local searches to get the goal
algorithms: hillClimbing and simulate annealing

"""


import copy,time

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

