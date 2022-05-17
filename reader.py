def tup(file):
    ret = []
    for el in file:
        el = str(el).rstrip('\n')
        el = el[1:-1]
        cur = []
        for num in el.split(", "):
            num = float(num)
            num = int(num)
            cur.append(num)
        if cur not in ret: ret.append(tuple(cur))
    if ret == []: ret = [(0, 0, 0)]
    return ret