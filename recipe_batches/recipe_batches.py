#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #initialize an empty array
  batches = []
  #if you dont have enough ingredients, you fail. return zero
  if len(ingredients) < len(recipe):
    batches.append(0)
  #if you have enough ingredients check each ingredient on hand against the recipe
  else:
    for i in ingredients:
      for r in recipe:
        #if the values match up...
        if i == r:
          #...see how many batches can be made
          x = ingredients[i] // recipe[r]
          #push the number of single ingredient batches into the array.
          batches.append(x)
  #sort the resulting array and return the lowest number of batches you can make.
  return sorted(batches)[0]

      

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))