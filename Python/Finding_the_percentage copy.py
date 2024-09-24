if __name__ == '__main__':
    n = int(float(input()))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        score = list(map(float, line))
        student_marks[name] = score
        for l in line:
            if 0 <= float(l) <= 100:
                pass
            else:
                pass

    query_name = input()
    for key in student_marks.keys():
        if query_name == key:
            print("{:.2f}".format(sum(student_marks[key])/3))
        else:
            pass