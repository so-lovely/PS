a = [1,2,3]
for i,val in enumerate(a):
    if val == 1:
        a.remove(val)
    print(i, val)