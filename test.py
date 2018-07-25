def findminandman(L):
    max = L[1]
    min = L[1]
    for i in L:
        if max < i:
            max = i
        elif min > i:
            min = i
    return max,min
