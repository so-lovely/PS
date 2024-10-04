def reduce_subtract(ls):
    new_ls = []
    j = 1
    for i in range(len(ls)-1):
        interval = ls[j] - ls[i]
        new_ls.append(interval)
        j += 1
    return new_ls

def reduce_sum(ls):
    new_ls = []
    j = 1
    for i in range(len(ls)-1):
        interval = ls[j] + ls[i]
        new_ls.append(interval)
        j += 1
    return new_ls

def remove_ls(ls, m, count):
    signal = True
    for i, val in enumerate(ls):
        if len(ls) == 1:
            signal = False
        if m >= val:
            ls.pop(i)
            count += 1
            break
    return ls, count, signal
    
def recursiveStack(erase_ls, m, stack, count):
    #롤러가 지울수있는 간격리스트를 만들때마다 롤러의 수와 같은지 비교하기
    bool_ls = list(map(lambda x: m > x, erase_ls))
    print(bool_ls)
#비교해서 최소한 하나 이상 롤러의 수가 간격보다 더크다면 이전것을 스택에 저장하고 쌓고
#더하기 
    if True in bool_ls:
        stack.append(erase_ls)
        erase_ls = reduce_sum(erase_ls)
        print(stack)
        print(erase_ls)
    # top to bottom 시작
    if len(erase_ls) == 1 and not True in bool_ls:
        return count + len(erase_ls)
    # 최소한 하나 이상의 롤러의 수가 간격보다 큰것이 없다면 이전것에서 
# 롤러의 수가 더 큰 간격을 모두 지우기 그리고 남아있지않다면 pop해서 이전으로 반복
# 단 가장자리의 간격을 지우면 안됨(?)
    signal = True
    while signal:
        if stack:
            erase_ls = stack.pop()
        erase_ls, count, signal = remove_ls(erase_ls, m, count)
    count += 1
    return recursiveStack(erase_ls, m, stack, count)

    
    
def solution(n, m, section):
    count = 0
    stack = []
    bool_ls = []
    signal = False
#간격만들기 간격 = 점과 점사이 거리 -> 간격리스트
    interval_ls = reduce_subtract(section)
    print(interval_ls)
#간격리스트에서 + 2 = 롤러와 같으면 롤러가 지울수있는 간격리스트
    erase_ls = list(map(lambda x: x+2, interval_ls))
    print(erase_ls)
#erase_ls의 엘리먼트가 1개인지 확인
    if len(erase_ls) == 1:
        if n >= erase_ls[0]:
            return 1
        else:
            return 2
    output = recursiveStack(erase_ls, m, stack, count)
    return output

    
