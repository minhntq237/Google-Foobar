import math

def solution(area):
    returnList = []
    while area > 0:
        squareSide = math.floor(math.sqrt(area))
        squareSize = squareSide**2
        returnList.append(squareSize)
        area = area - squareSize
    return returnList

print(solution(1532474567657))