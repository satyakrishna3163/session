def sortedMerge(ls1, ls2, res, n, m):
    ls1.sort()
    ls2.sort()
    i, j, k = 0, 0, 0
    while (i < n and j < m):
        if (ls1[i] <= ls2[j]):
            res[k] = ls1[i]
            i += 1
            k += 1
        else:
            res[k] = ls2[j]
            j += 1
            k += 1
             
    while (i < n):
        res[k] = ls1[i]
        i += 1
        k += 1
         
    while (j < m):
        res[k] = ls2[j]
        j += 1
        k += 1
ls1= [10,20,40,60,80,100]
ls2 = [11,22,33,44,55,66]
n = len(ls1)
m = len(ls2)
res = [0 for i in range(n + m)]
sortedMerge(ls1, ls2, res, n, m)
print ("unSorted merged list :")
for i in range(n + m):
    print(res[i],end=" ")