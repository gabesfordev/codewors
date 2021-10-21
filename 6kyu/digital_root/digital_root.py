def digital_root(n):
    n = str(n)
    lst = []

    for i in n:
        lst.append(int(i))

    result_int = sum(lst)
    result_str = str(result_int)
    if len(result_str) <=1:
        return result_int
    else:
        return digital_root(result_int)

