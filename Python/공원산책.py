def solution(park, routes):
    # ex ["E 2","S 2","W 1"] -> {'E': 2, 'S': 2, 'W': 1}
    cmds = [(route.split(" ")[0],int(route.split(" ")[1])) for route in routes]
    current_location = find_S(park)
    
    for cmd in cmds:
        if check_route(current_location, cmd, park) == True:
            current_location = move(current_location, cmd)
    
    return current_location
        
    
def find_S(park):
    for i, row in enumerate(park):
        if 'S' in row:  
            return [i, row.index('S')]  

            

def check_route(current_location, direction, park) -> bool:
    x1, y1 = current_location
    a, b = direction
    h, w = len(park), len(park[0]) 

    if a == 'E':
        if y1 + b >= w:
            return False
       
        if 'X' in park[x1][y1+1:y1 + b + 1]:
            return False

    elif a == 'W': 
        if y1 - b < 0:
            return False
        if 'X' in park[x1][y1 - b:y1]:
            return False

    elif a == 'S': 
        if x1 + b >= h:
            return False
        for i in range(1, b + 1):
            if park[x1 + i][y1] == 'X':
                return False

    elif a == 'N': 
        if x1 - b < 0:
            return False
        for i in range(1, b + 1):
            if park[x1 - i][y1] == 'X':
                return False

    return True


def move(cur_loc, cmd):
    a, b = cmd
    if a == 'E':
        cur_loc[1] += b
        return cur_loc
    elif a == 'W':
        cur_loc[1] -= b
        return cur_loc
    elif a == 'N':
        cur_loc[0] -= b
        return cur_loc
    elif a == 'S':
        cur_loc[0] += b
        return cur_loc
        
    



    
