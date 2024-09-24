def merge_the_tools(string, k):
    line_num = int(len(string) / k)
    listed_string = list(string)
    store_ls = []
    
    for _ in range(line_num):
        for i in range(k):
            if not listed_string[0] in store_ls:
                poped = listed_string.pop(0)
                store_ls.append(poped)
            else:
                listed_string.remove(listed_string[0])
        print(*store_ls, sep='')
        store_ls.clear()
            



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


#AAABCADDE