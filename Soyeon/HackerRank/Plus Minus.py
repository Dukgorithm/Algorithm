def plusMinus(arr):
    p = [0, 0, 0]

    for n in arr:
        if n > 0:
            p[0]+=1
        elif n<0:
            p[1]+=1
        else:
            p[2]+=1
    for pn in p:
        print(pn/sum(p))