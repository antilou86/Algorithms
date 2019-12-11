#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  
  # if i have a total number (n)
  # and we can only remove 1 or 2 or 3 at a time
  # how many combinations of removing 1, or, 2 or 3, until it hits 0 exist?

  # no matter what N is, n will always be one of the answers. 1 cookie, n times. 
  # we can also do 1 cookie (n - 2) times, and 2 cookies 1 time. 
  # similarly 1 cookie (n - 3) times, and 3 cookies 1 time. 
  # also 1 cookie (n - 5) times, and 3 cookies + 2 cookies 1 time each.
  # if n is divisable by three, we can eat 3 cookies (n/3) times.
  # if n is divisable by two, we can eat 2 cookies (n/2) times.


  if n < 1:
    return 1
  else:
    original_n = n

    next_n = n 
  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')