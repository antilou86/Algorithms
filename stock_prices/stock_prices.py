#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #receive an array of prices.
  #check each price for max and each for minimum
  minimum_buy = sorted(prices)[0]
  max_sell = sorted(prices)[-1]
  print("sorted array: ", sorted(prices))
  #profit starts at zero. buy subtracts minimum from profit. sell adds maximum to profit.
  profit = 0 - minimum_buy + max_sell
  
  return profit
  

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))