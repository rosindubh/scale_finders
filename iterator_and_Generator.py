# example from 'https://www.tutorialspoint.com/python3/python_loops.htm'
# phil welsby - 10 february 2017


#!usr/bin/python3
import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n): 
         return
      yield a
      print()
      a, b = b, a + b
      counter += 1
f = fibonacci(25) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
