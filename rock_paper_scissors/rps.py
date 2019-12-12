#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    #defines a play/move
    plays = ["rock", "paper", "scissors"]
    #establishes an array to return the outcomes
    outcomes = []
    #helper function for recursion.
    def helper_func(n, result = []):
      #ends the recursive loop if we've completed all rounds, push the result into the outcome array
      if n==0:
        return outcomes.append(result)
      #for each possible choice within the play, run the helper function with one less round, and the last set of plays concatonated onto the result array
      for play in plays:
        helper_func(n-1, result + [play])
    #intiates the recursive loop
    helper_func(n)
    #returns the end result
    return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')