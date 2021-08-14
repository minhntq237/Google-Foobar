from __future__ import division #For Python 2.7
import numpy as np
import fractions as fractions
from operator import itemgetter

import random

'''
By Nguyen Trung Quang Minh
This is an absorbing matrix problem. The given matrix is all the state in step 1. As the steps increases, the probabilities of it jumping from one state to another changes
Eventually, the matrix will approach the limiting matrix, where we get the real probabilities of the initial states leading to all the absorbing states
Calculate F*R in the limiting matrix 
==> F x R = (I-Q)^-1 x R

Read more here:
https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
'''

def sortMatrix(baseMatrix):
    sumOfMatrix = []
    for i in range(len(baseMatrix)):
        if i == 0:
            continue
        rowSum = sum(baseMatrix[i])
        sumOfMatrix.append([rowSum, i])
    sortedSum = sorted(sumOfMatrix, key=itemgetter(0), reverse=True)
    
    indexKeys = [0] + [i[1] for i in sortedSum]
    
    newMatrix = []
    for i in indexKeys:
        baseRow = baseMatrix[i]
        sortedRow = []
        for j in indexKeys:
            sortedRow.append(baseRow[j])
        newMatrix.append(sortedRow)

    return newMatrix 
    

def findTerminal(baseMatrix):
    stageStatus = []
    for row in baseMatrix:
        if sum(row) == 0:
            stageStatus.append(True)
        else:
            stageStatus.append(False)
    return stageStatus


def transformMatrix(startingMatrix):
    newMatrix = []
    for row in startingMatrix:
        rowSum = sum(row)
        if rowSum == 0:
            newMatrix.append(row)
            continue
        newRow = []
        for elem in row:
            newElement = elem / rowSum
            newRow.append(newElement)
        newMatrix.append(newRow)
    return newMatrix

def countTerminal(baseMatrix):
    stageStatus = 0
    for row in baseMatrix:
        if sum(row) == 0:
            stageStatus += 1
    return stageStatus

def findQAndRMatrix(baseMatrix):
    R = []
    Q = []
    absorbingStateCount = countTerminal(baseMatrix)
    for i in range(len(baseMatrix)):
        rowOfR = []
        rowOfQ = []
        for j in range(len(baseMatrix)):
            if i < len(baseMatrix) - absorbingStateCount and j < len(baseMatrix) - absorbingStateCount:
                rowOfQ.append(baseMatrix[i][j])
            elif i < len(baseMatrix) - absorbingStateCount:
                rowOfR.append(baseMatrix[i][j])
        if i < len(baseMatrix) - absorbingStateCount:
            R.append(rowOfR)
            Q.append(rowOfQ)
    return R, Q

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def solution(matrix):
    if not (countTerminal(matrix)):
        return [0,0]
    if not (sum(matrix[0])):
        resultMatrix = []
        resultRow = [1]
        for i in range(countTerminal(matrix)-1):
            resultRow.append(0)
        resultMatrix.append(resultRow)
    else:
        matrix = sortMatrix(matrix)
        formattedMatrix = transformMatrix(matrix)
        R, Q = findQAndRMatrix(formattedMatrix)
        I = np.identity(len(Q))
        firstCalc = np.subtract(I, Q)
        if np.linalg.det(firstCalc):
            F = np.linalg.inv(firstCalc)
        else:
            F = np.linalg.pinv(firstCalc)
        resultMatrix = np.matmul(F, R)

    numerators = []
    denominators = [] 
    for i in resultMatrix[0]:
        denominator = fractions.Fraction(i).limit_denominator().denominator
        denominators.append(denominator)
        numerator = fractions.Fraction(i).limit_denominator().numerator
        numerators.append(numerator)

    answerArray = []
    cloneDenominators = denominators.copy()
    maxDenominator = cloneDenominators.pop()
    while len(cloneDenominators) > 0:
        newDenominator = cloneDenominators.pop()
        maxDenominator = compute_lcm(maxDenominator, newDenominator)

    for i in range(len(numerators)):
        newNumerator = numerators[i]*(maxDenominator/denominators[i])
        answerArray.append(int(round(newNumerator)))
    answerArray.append(int(round(maxDenominator)))

    return answerArray

###############################################

def generateTestCases(matrixSize):
    rando = random.randrange(0, matrixSize)
    testCase = [[random.randrange(0, 9) for i in range(matrixSize)] for i in range(rando)] + [[0 for i in range(matrixSize)] for i in range(matrixSize-rando)]
    return testCase

        

testCase1 = [
    [0, 1, 0, 0, 0, 1], 
    [4, 0, 0, 3, 2, 0], 
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
    ]

testCase2 = [
    [0, 2, 1, 0, 0], 
    [0, 0, 0, 3, 4], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]
    ]

testCase3 = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

testCase4 = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 0]
]

testCase5 = [
    [1, 1, 1, 1, 1, 1], 
    [1, 2, 3, 4, 5, 6], 
    [0, 0, 0, 9, 8, 7],
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
    ]

testCase6 = [[0]]

testCase7 = [
    [6, 7, 3, 1, 6, 5,  3, 1, 5, 2],
    [6, 3, 3, 0, 8, 6,  4, 3, 2, 8],
    [1, 1, 0, 2, 7, 6,  5, 4, 3, 3],
    [7, 5, 8, 1, 6, 1,  0, 7, 3, 6],
    [6, 4, 7, 0, 6, 8,  2, 7, 0, 6],
    [4, 5, 7, 3, 2, 7,  0, 3, 6, 6],
    
    [0, 0, 0, 0, 0, 0,  0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,  0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,  0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,  0, 0, 0, 0]
    ]

""" R, Q = findQAndRMatrix(transformMatrix(testCase1))
print(R)
print(Q)
 """
print(solution(testCase1))
print(solution(testCase2))
print(solution(testCase3)) 
print(solution(testCase4))
print(solution(testCase5))
print(solution(testCase6))

print(np.array(testCase7)) 
print(solution(testCase7), end=" ")
print(sum(solution(testCase7))/2)

""" a = 0

while a != -1:
    a += 1
    testCase = generateTestCases(10)
    print(np.array(testCase))
    print(solution(testCase), end=" ")
    print(sum(solution(testCase))/2)
    if sum(solution(testCase))%2 == 1:
        break

print(a) """
