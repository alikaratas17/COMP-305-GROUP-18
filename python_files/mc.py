from parser import Parser
from Outputer import Outputer
import random

def calculate_orders(s):
  sums = [(i,s[i]) for i in range(len(s))]
  sums = sorted(sums,key=lambda y: y[1],reverse=True)
  orders = [0]*len(sums)
  o = len(sums)
  orders[sums[0][0]] = o
  o -=1
  for i in range(1,len(sums)):
    if sums[i][1] < sums[i-1][1]:
     orders[sums[i][0]] = o
    else:
      orders[sums[i][0]] = orders[sums[i-1][0]]
    o -=1
  return orders


filename = "./../inputs/baby_comp_4.txt"
parser = Parser(filename)
players = []
parser.readDataNew(players)
playerCount = parser.getPlayerCount()
roundCount = parser.getRoundCount()

for i in range(playerCount):
  players[i] = sorted(players[i],reverse=True)

sums = [sum(player) for player in players]


numbersFile = "./../numbersMC.txt"
try:
  with open(numbersFile,"r") as f:
    lines = f.readlines()
    l_values = [int(x) for x in lines[0].split(",")]
except:
  s = set()
  for y in players:
    for i in y:
      s.add(i)
  l_values = sorted(list(s),reverse = True)

outputFile = "./../outputs/outputMC.txt"

try:
  with open(outputFile,"r") as f:
    min_orders =[0]*playerCount
    i = 0
    for line in f:
      o = int(line)
      min_orders[i] = o
      i+=1
except:
  min_orders = calculate_orders(sums)

k = [0]*playerCount
old_l_value = l_values.pop(0)
l_value = old_l_value
for i in range(playerCount):
  current = players[i]
  sums[i] += (k[i] * (l_value - old_l_value))
  dv = 0
  if k[i] < roundCount:
    while current[k[i]] >= l_value:
      dv -= (current[k[i]] - l_value)
      k[i]+=1
      if k[i]==roundCount:
        break
  sums[i] += dv
orders = calculate_orders(sums)
for i in range(playerCount):
  min_orders[i] = min(min_orders[i],orders[i])

p = 1/roundCount
index = 0
length =len(l_values)

while index < length:
  if random.uniform(0,1)>=p:
    index+=1
    continue

  l_value = l_values.pop(index)
  length-=1
  for i in range(playerCount):
    current = players[i]
    sums[i] += (k[i] * (l_value - old_l_value))
    dv = 0
    if k[i] < roundCount:
      while current[k[i]] >= l_value:
        dv -= (current[k[i]] - l_value)
        k[i]+=1
        if k[i]==roundCount:
          break
    sums[i] += dv
  orders = calculate_orders(sums)
  for i in range(playerCount):
    min_orders[i] = min(min_orders[i],orders[i])
  old_l_value = l_value

outputer = Outputer(outputFile)
outputer.output(min_orders)
with open(numbersFile,"w") as f:
  f.write(str(l_values.pop(0)))
  for n in l_values:
    f.write(","+str(n))