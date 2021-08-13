def solution(l, t):
    indexList = []
    total = 0
    i = 0

    while (total != t):
        if total < t:
            if i > len(l)-1:
                break
            else:
                total += l[i]
                indexList.append(i)
                i += 1
        elif total > t:
            discardIndex = indexList.pop(0)
            total = total - l[discardIndex]
            
    if total == t:
        return [indexList[0], indexList[-1]]
    else:
        return [-1,-1]

print(solution([4,3,10,2,8], 12))
print(solution([1,2,3,4], 15))
print(solution([1,1,1,1,14], 15))