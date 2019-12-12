#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  
  # if i have a total number (n)
  # and we can only remove 1 or 2 or 3 at a time
  # how many combinations of removing 1, or, 2 or 3, until it hits 0 exist?
  # will need a counter to track the number of solutions.
  # may need counters (multiples?) to track the number of times 1-2-or-3 is removed from the total
  # loop (if im looping) would have to stop when n reaches zero.
  # n should always be divisable by one?

  # theoretically  
 '''
 lets say n=10

 our answer would count possible combinations of 1, 2, 3 that add up to 10.
 it can be visualized as

 [1,1,1,1,1,1,1,1,1,1]
 [1,2,1,1,1,1,1,1,1]
 [1,2,2,1,1,1,1,1]
 [1,2,2,2,1,1,1]
 [1,2,2,2,2,1]
 [1,2,2,3,1]
 [1,2,2,3,2]
 [1,2,3,1,1,1,1]
 [1,2,3,2,1,1]
 [1,2,3,2,2]
 [1,2,3,3,1]
 [1,3,1,1,1,1,1,1]
 [1,3,2,1,1,1,1]
 [1,3,2,2,1,1]
 [1,3,2,2,2]
 [1,3,2,3,1]
 [1,3,2,3,]
 [1,3,3,1,1,1]
 [1,3,3,2,1]
 [1,3,3,3]
 [2,1,1,1,1,1,1,1,1]
 [2,2,1,1,1,1,1,1]
 [2,3,1,1,1,1,1]

 '''
 
  # you get the picture
  '''
  so begin with 1,
  append 1 to an array, repeat n-1 times.

  then 2,
  append 2 to the array, repeat n/2-2 times

  then 3,
  append 3, repeat n/3-3 times
  if anything left over append 1 until the sum is n

  '''

  # simplify the problem
  # how many ways can we eat n cookies if we can eat only 1 or 2 at a time?
  # well, if it were only 1 at a time, we could only eat them in 1 way.
  # if it's one or two at a time we can eat the items in eight ways (assuming n is 5)
  # 
  '''
  [1,1,1,1,1]
  [1,2,1,1]
  [1,1,2,1]
  [1,1,1,2]
  [1,2,2]
  [2,1,1,1,1]
  [2,2,1]
  [2,1,2]
  
  '''

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')