from __future__ import division #For Python 2.7
import numpy as np
import fractions as fractions
from operator import itemgetter

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

def solution(matrix):
    if not (countTerminal(matrix)):
        return [0]
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
    maxDenominator = max(denominators)
    for i in range(len(numerators)):
        newNumerator = int(numerators[i]*(maxDenominator/denominators[i]))
        answerArray.append(newNumerator)
    answerArray.append(int(maxDenominator))
    
    return answerArray
        

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
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

testCase3 = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

testCase4 = [
    [0, 1, 0, 0, 0, 1], 
    [4, 0, 0, 3, 2, 0], 
    [0, 0, 0, 0, 0, 0],
    [0, 9, 0, 8, 7, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
    ]

""" R, Q = findQAndRMatrix(transformMatrix(testCase1))
print(R)
print(Q)
 """
print(solution(testCase1))
print(solution(testCase2))
print(solution(testCase3)) 
print(solution(testCase4))
