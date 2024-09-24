if __name__ == '__main__':
    N = int(input())
    L = []
    iter = 0
    zero_arg = ['sort', 'pop', 'reverse']
    while True:
        fun, *seq = input().split()
        seq = list(map(int, seq))
        if fun == 'insert':
            L.insert(seq[0], seq[1])
        if fun == 'remove':
            L.remove(seq[0])
        if fun == 'append':
            L.append(seq[0])
        if fun in zero_arg:
            getattr(L, fun)()
        if fun == 'print':
            print(L)
        iter += 1
        if iter == N:
            break

        

'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''
'''Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
