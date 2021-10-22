def unique_in_order(iterable):
    
    lst = []
    if iterable:
        for i in range(len(iterable)):
            try:
                if iterable[i + 1] != iterable[i]:
                    lst.append(iterable[i])
            except:
                pass
        lst.append(iterable[-1])

    return lst