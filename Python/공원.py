def solution(mats, park):
    width = len(park[0])
    height = len(park)
    mats.sort(reverse=True)
    for mat in mats:
        ok = move(mat, park, width, height)
        if ok:
            return mat
    answer = -1
    return answer
    
def move(mat, park, width, height):
    do_width = width - mat + 1
    do_height = height - mat + 1
    
    if do_width <= 0 or do_height <= 0:
        return False
    
    for hw in range(do_height):
        for gw in range(do_width):
            if square_search(park, mat, hw, gw):
                return True
            
    return False
            
            
            
        
def square_search(park, mat, hw, gw):
    for i in range(mat):
        for j in range(mat):
            if park[i+hw][j+gw] != '-1':
                return False
            
    return True
                        
    
    