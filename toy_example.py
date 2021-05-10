"""
This is a toy example to understand how sample output 2 in pdf was generated
Trying l = 6:1 and keeping the minimum for each of the players
"""
numbers = [
(0,[3, 1, 2, 2]),
(1,[4, 3, 2, 2]),
(2,[6, 6, 3, 2]),
(3,[7, 3, 4, 3]),
(4,[3, 4, 2, 4]),
(5,[2, 3, 3, 5])
]
sums = sorted([(sum(x[1]),x[0]) for x in numbers])
orders = [0]*6
last = sums[-1]
o = 6
orders[last[1]] = o
for i in range(len(sums)-2,-1,-1):
  o -= 1
  current = sums[i]
  if current[0] == sums[i+1][0]:
    orders[current[1]] = orders[sums[i+1][1]]
  else:
    orders[current[1]] = o
#print(orders)
best_orders = orders.copy()
l = 6
changed = False
while l > 0:
    
  for i in range(6):
    for j in range(4):
      if numbers[i][1][j] > l:
        changed = True
        numbers[i][1][j]=l
  l -= 1
  sums = sorted([(sum(x[1]),x[0]) for x in numbers])
  orders = [0]*6
  last = sums[-1]
  o = 6
  orders[last[1]] = o
  for i in range(len(sums)-2,-1,-1):
    o -= 1
    current = sums[i]
    if current[0] == sums[i+1][0]:
      orders[current[1]] = orders[sums[i+1][1]]
    else:
      orders[current[1]] = o
  for i in range(6):
    best_orders[i]=min(orders[i],best_orders[i])
print(best_orders)
"""
l = 6
best_orders = []

for i in range(len(numbers)):
  print(sum(numbers[i]))
  """
