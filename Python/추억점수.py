def solution(name, yearning, photo):
    dic = {name[i]: yearning[i] for i in range(len(name))}
    
    result = []
    for group in photo:
        total_yearning = sum(dic.get(person, 0) for person in group)
        result.append(total_yearning)
    
    return result
