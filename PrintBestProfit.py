indices = [7,1,14,2,6,9,0,14,2,1]
l = len(indices)
newlist = []
n = 0
for i in indices:
    m = max(indices[n:l])
    profit = m - i
    newlist.append(profit)
    n += 1

print(max(newlist))
