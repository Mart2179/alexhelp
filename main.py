list = [1, 3, -5, -10]

diffs = []

#current_profit = 0

previous_profit = 0

for i in list:

  current_profit = i

  total = current_profit - previous_profit
  print(total)

  diffs.append(total)

  previous_profit = current_profit


#print(diffs)
