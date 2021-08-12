My solution for the Doomsday Fuel challenge.
With the help of 
> https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md

In solution 2-1, I employed the concept of Eigenvector and EigenValue to calculate the limiting matrices, but the execution or approach was wrong

For solution 2-2, I used the Absorbing Markov chain concept from the GitHub linked above to find the limiting matrix (i.e. matrix where the number of timesteps approach infinity). 
This is currently my main approach and I'm in the process of optimizing. Test case failed: 4/10 

Update 1: using np.linalg.pinv() for cases in which matrix F is singular, in which case the Moore-Penrose pseudo inverse is the inverse of the matrix.

Update 2: Handle special cases where starting state is terminal

