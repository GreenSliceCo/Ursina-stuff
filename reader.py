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
        ret.append(tuple(cur))
    return ret