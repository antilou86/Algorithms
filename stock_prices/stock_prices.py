#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #receive an array of prices.check each price for max
  max_num = sorted(prices)[-1]
  #find the location of the highest price in the array. 
  sell_index = prices.index(max_num)
  #isolate everything prior to the highest sell price. (it is possible this will be empty.)
  previous_prices = prices[:sell_index]
  #this grabs everything after the highest price (in case the first item is the highest.)
  next_prices = prices[(sell_index+1):]
  #profit starts at zero. buy subtracts minimum from profit. sell adds maximum to profit.
  #check the length of the previous_prices array. if empty => buy at the sell price and sell at the next highest.
  if len(previous_prices) < 1:
    new_max = sorted(next_prices)[-1]
    new_index = next_prices.index(new_max)
    new_previous = next_prices[:new_index]
    new_next = next_prices[new_index + 1:]
    if len(new_previous) < 1:
      return 0 - prices[0] + prices[1]
    else:
      profit = 0 - sorted(new_previous)[0] + new_max
      return profit
  else:
    profit = 0 - sorted(previous_prices)[0] + max_num
    return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))