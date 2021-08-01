def counttriplets(arr,r):
    Before = {}
    After = {}
    count = 0
    for v in arr:
        if v in After:
            After[v] += 1
        else:
            After[v] = 1
        
    for v in arr:
        After[v] -= 1
        if v%r == 0 and v//r in Before and v * r in After:
            count += Before[v//r]*After[v*r]
        if v in Before:
            Before[v] += 1
        else:
            Before[v] = 1
    return count
        
        
arr = [1 ,2 ,2 ,4]
print(counttriplets(arr,2))
