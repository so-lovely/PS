import string
def print_rangoli(s):
    sli = list(string.ascii_lowercase[:s])
    sli.reverse()
    dic_ls = {}
    key_ls = [k for k in range(1, s)]
    for i in range(1, 2*s):
        dic_ls[i] = ['-'] * (4*n-3)
    for ke, alphabet in zip(key_ls, sli):
        move_stop(dic_ls, ke, alphabet)
    dic_ls[s][2*s-2] = 'a'
    a = list(dic_ls.values())
    b = a[0:n-1]
    for _ in b:
        print(*_, sep='')
    print(*a[s-1], sep='')
    b.reverse()
    for _ in b:
        print(*_, sep='')

def move_stop(dic_ls,key:int,alphabet:str) -> dict:
    dic_ls[key][(2*n-1)-1] = alphabet
    for cur in range(1, n-key+1):
        rnext = ((2*n-1)+2*cur)-1
        lnext = ((2*n-1)-2*cur)-1
        dic_ls[key+1][rnext] = alphabet
        dic_ls[key+1][lnext] = alphabet
        key += 1





    

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)