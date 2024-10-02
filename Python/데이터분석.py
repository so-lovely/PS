def solution(data, ext, val_ext, sort_by):
    columns = ['code','date','maximum','remain']
    for i, column in enumerate(columns):
        if column == ext:
            num = i
    for i, column in enumerate(columns):
        if column == sort_by:
            num2 = i
    ls = list(filter(lambda x: x[num] < val_ext, data))
    ls.sort(key=lambda x: x[num2])
    return ls