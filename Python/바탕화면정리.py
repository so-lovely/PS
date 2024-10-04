def solution(wallpaper):
    x = []
    y = []
    for i, line in enumerate(wallpaper):
        while ('#' in line):
            idx = line.index('#')
            x.append(i)
            y.append(idx)
            line = line[:idx] + '.' + line[idx + 1:]
    x_maximum = max(x) + 1
    y_maximum = max(y) + 1
    x_minimum = min(x)
    y_minimum = min(y)
    answer = [x_minimum, y_minimum, x_maximum, y_maximum]
    return answer