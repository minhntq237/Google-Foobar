def solution(n):
    memo = [[0 for i in range(n + 1)] for j in range(n + 1)]
    memo[0][0] = 1 #At height 0, bricks = 0, count as 1 way 
    for height in range(1, n+1): #Ignore height 0
        for numBricks in range(0, n+1):
            # Q(n, k) = Q(n-k, k) + Q(n-k, k-1) for n>k>=1, with Q(1, 1)=1, Q(n, 0)=0 (n>=1)
            memo[height][numBricks] = memo[height - 1][numBricks]
            if numBricks >= height:
                memo[height][numBricks] += memo[height - 1][numBricks - height]
    return memo[n][n] - 1

print(solution(200))
