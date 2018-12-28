""""
Student : Navid pourhadi

this project implement for eight queen that execute by local searches to get the goal
algorithms: hillClimbing and simulate annealing

"""



import random,copy
import time


def createChess():
    temp = []
    for i in range(0, 8):
        temp.append([])
        for j in range(0, 8):
            temp[i].append(0)

    x=[0,0,0,0,0,0,0,0]
    for i in range(0,8):
        print "enter location of queens in each colomn:"
        x[i]=input()
        temp[i][x[i]-1]=1
    return temp


def putQueen(array , x , y):
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
        temp += "| " + str(j+1) + "\n"
        for i in range(0, 8):
            temp += "|____"
        temp += "|\n"
    print (temp)
    print("  1    2    3    4    5    6    7    8  ")


def move(array , m , n):
    for i in range(0,8):
        if array[m][i]==1 :
            array[m][i]=0
            array[m][n]=1
    return array



def heuristic(array):
    h = 0;
    for i in range(0, 8):
        for j in range(0,8):
            if array[i][j]==1:
                for m in range(i+1 , 8):
                    for n in range(0,8):
                        if array[m][n]==1 :
                            if (j==n) | (m - i == j - n) | (m - i == n - j) :
                                h = h + 1
    return h
