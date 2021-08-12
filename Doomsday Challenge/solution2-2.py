from __future__ import division #For Python 2.7
import numpy as np
import fractions as fractions

'''
By Nguyen Trung Quang Minh
This is an absorbing matrix problem. The given matrix is all the state in step 1. As the steps increases, the probabilities of it jumping from one state to another changes
Eventually, the matrix will approach the limiting matrix, where we get the real probabilities of the initial states leading to all the absorbing states
Calculate F*R in the limiting matrix 
==> F x R = (I-Q)^-1 x R

Read more here:
https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md
'''

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

def findTerminal(baseMatrix):
    stageStatus = 0
    for row in baseMatrix:
        if sum(row) == 0:
            stageStatus += 1
    return stageStatus

def findQAndRMatrix(baseMatrix):
    R = []
    Q = []
    absorbingStateCount = findTerminal(baseMatrix)
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

    formattedMatrix = transformMatrix(matrix)
    R, Q = findQAndRMatrix(formattedMatrix)
    I = np.identity(len(Q))
    firstCalc = np.subtract(I, Q)
    F = np.linalg.inv(firstCalc)
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

""" R, Q = findQAndRMatrix(transformMatrix(testCase1))
print(R)
print(Q)
 """
print(solution(testCase1))
print(solution(testCase2))