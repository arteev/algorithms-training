

def mul(x, y):
    d1 = list(map(int,reversed(str(x))))
    d2 = list(map(int,reversed(str(y))))
    if len(d2)>len(d1):
        d1, d2 = d2, d1
    m = []
    zeros = 0
    for dy in d2:
        n = []
        ext_n = 0

        for dx in d1:
            k = dy * dx + ext_n
            n.insert(0,k % 10)
            ext_n = k // 10
        if ext_n:
            n.insert(0,ext_n)
            
        if zeros>0:
            n = n + [0]*zeros
        zeros += 1
        m.append(n)

    r= sum(map(int, ((''.join(map(str,b))) for b in m)))    
    return r