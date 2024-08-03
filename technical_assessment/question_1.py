
def modify_list(lst):
    length = len(lst)
    res = []
    for i in range(length):
        ele = lst[i]
        next_index = i + 1
        if i == length - 1:
            next_index = 0
        ele = ele * i + lst[next_index]
        res.append(ele)
    return res


sample_list = [4]
print(modify_list(sample_list))
