from parser import Parser
from Outputer import Outputer
def solve(filename):
  parser = Parser(filename)
  l = []
  parser.readData(l)
  s = set()
  for x,y in l:
    for i in y:
      s.add(i)
  numbers = sorted(list(s),reverse = True)
  min_orders = calculate_orders(l)
  round_count = parser.getRoundCount()
  for i in range(len(l)):
    l[i] = (l[i][0],sorted(l[i][1],reverse=True))
  new_max = numbers[1]
  for num in numbers[1:]:
    if num > new_max:
      continue
    #update with new num value
    m = round_count
    for i in range(len(l)):
      j=0
      while j < round_count:
        if l[i][1][j] > num:
          l[i][1][j] = num
          j+=1
          continue
        break
      m = min(j,m)
    if m > 0:
      new_max = -1
      round_count -=m
      for i in range(parser.getPlayerCount()):
        for k in range(m):
          l[i][1].pop(0)
        new_max = max(l[i][1][0],new_max)
    #calculate min orders
    orders = calculate_orders(l)
    for i in range(parser.getPlayerCount()):
      min_orders[i] = min(min_orders[i],orders[i])
  return min_orders

def calculate_orders(l):
  sums = [(x[0],sum(x[1])) for x in l]
  sums = sorted(sums,key=lambda y: y[1],reverse=True)
  orders = [0]*len(l)
  o = len(l)
  orders[sums[0][0]] = o
  o -=1
  for i in range(1,len(sums)):
    if sums[i][1] < sums[i-1][1]:
     orders[sums[i][0]] = o
    else:
      orders[sums[i][0]] = orders[sums[i-1][0]]
    o -=1
  return orders
      







l= solve("./../inputs/baby_comp_2.txt")
o = Outputer("./output3.txt")
o.output(l)
