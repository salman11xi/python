lst = [5,6,7,2,1,3]
for j in range(0,6):
    for i in range(0,5):
         if lst[i] > lst[i+1]:
             swap = lst[i]
             lst[i] = lst[i+1]
             lst[i+1] = swap
print(lst)
             