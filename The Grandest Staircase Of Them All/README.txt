Solution for "The Grandest Staircase Of Them All"

In its essence, this problem requires the input integer to be split into different number, meaning we need to find the distinct partition count for it.

According to "http://oeis.org/A008289", the formula required here is:
  Q(n, k) = Q(n-k, k) + Q(n-k, k-1) for n>k>=1, where Q(n, k) is the distinct partition for the number n, with the maximun part value of k.
From observing the formula, this question is similar to the Fibonacci function:
  F(n) = F(n-1) + F(n-2)
  
With the fibonacci number calculation, memoization and dynamic programming is used to avoid recalculating redundant cases.
Therefore, my solution is to create a 2d array to store all the Q function result at different n and k value. 


Reference:

https://www.reddit.com/r/learnprogramming/comments/5vysej/google_foobar_level_3_help/

http://oeis.org/A008289

