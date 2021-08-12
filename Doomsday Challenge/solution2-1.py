import numpy as np
import fractions as fraction

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
    stageStatus = []
    for row in baseMatrix:
        if sum(row) == 0:
            stageStatus.append(True)
        else:
            stageStatus.append(False)
    return stageStatus

def solution(matrix):
    terminalMatrix = findTerminal(matrix)
    equation = []
    formatedMatrix = transformMatrix(matrix)
    for i in range(len(formatedMatrix)):
        equationArray = []
        for j in range(len(formatedMatrix)):
            num = formatedMatrix[j][i]
            if i == j:
                equationArray.append(num-1)
            else:
                equationArray.append(num)
        equationArray.append(0)
        equation.append(equationArray)
    lastArray = [1 for i in range(len(matrix))]
    lastArray.append(0)
    equation.append(lastArray)
    #print(equation)

    rhsArray = [0 for i in range(len(matrix))]
    rhsArray.append(1)
    #print(rhsArray)


    a = np.array(equation)
    b = np.array(rhsArray)
    print(a)
    print(b)

    """ x = np.linalg.solve(a, b)
    print(x)  """
    Apinv = np.linalg.pinv(a)
    x = Apinv.dot(b)
    return x



#Output = [7, 6, 8, 21]
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

solution(testCase1)

""" a = np.array([[2, -4, 4], [34, 3, -1], [1, 1, 1]])
b = np.array([8, 30, 108])
print(a)
print(b)
x = np.linalg.solve(a, b)
print(x) 


Apinv = np.linalg.pinv(a)
y = Apinv.dot(b)
print(y) """
