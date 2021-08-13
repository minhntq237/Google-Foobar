def solution(l):
    newList = []

    for i in l:
        versionInt = []
        version = i.split(".")
        for j in version:
            versionInt.append(int(j))
        newList.append(versionInt)

    sortedList = sorted(newList)

    returnList = []
    for i in sortedList:
        version = ""
        for j in range(len(i)):
            if j == len(i) - 1:
                version += str(i[j])
            else:
                version += str(i[j]) + "."
        returnList.append(version)
    
    return returnList

testCase = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

print(solution(testCase))