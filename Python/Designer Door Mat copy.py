a,b = map(int, input().split())
#b: isplaceholder cause of problem arg is not needed...
k = int((a-1)/2)
temp = []
for i in range(k):
    cstr:str = '.|.' * ((2*i)+1)
    temp.append(cstr.center(6*k+3, '-'))
    print(temp[i])
print('WELCOME'.center(6*k+3, '-'))
temp.reverse()
print(*temp, sep='\n')




