lst = [5,6,7,2,1,3]
for j in range(0,10):
    for i in range(0,9):
         if lst[i] > lst[i+1]:
             swap = lst[i]
             lst[i] = lst[i+1]
             lst[i+1] = swap
print(lst)