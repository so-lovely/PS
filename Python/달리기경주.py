def solution(players, callings):
    for calling in callings:
        for i, player in enumerate(players):
            if player == calling:
                players = swap(players, i-1, i)
                break
            
    return players

def swap(ls, num1, num2):
    temp = ls[num1]
    ls[num1] = ls[num2]
    ls[num2] = temp
    return ls
    