
def print_formatted(n):
    width = len(bin(n))-1
    for num in range(1, n+1): 
        print('{0:{width1}{base1}}'.format(num, base1='d', width1=width-1), end='')
        for base in 'oXb':
            print('{0:{width2}{base2}}'.format(num, base2=base, width2=width), end='')
        print()
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)