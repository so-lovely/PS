a, name_score, stored_list = 0, {}, []
for _ in range(int(input())):
    a = _
    name, score = input(), float(input())
    stored_list.append(score)
    name_score[name] = score
set_list: set = sorted(set(stored_list)) if 2 <= a+1 <= 5 else exit()
second_lowest = list(set_list)[1] if len(set_list) >= 2 else exit()
final = [key for key, value in name_score.items() if value == second_lowest]
print(*sorted(final), sep='\n')