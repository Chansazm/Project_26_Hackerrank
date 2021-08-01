from collections import defaultdict

def FreQuery(quries):
    res = []
    Freq = defaultdict(int)
    
    for x in quries:
        if x[0] == 1:
            #insert x in the data structure
            Freq[x[1]] += 1
        elif x[0] == 2:
            #Delete one occurence of y from your data structure, if present.
            if x[1] in Freq and x[1] > 0:
                Freq[x[1]] -= 1
        else:
            #Check if any integer is present whose frequency is exactly . If yes, print 1 else 0
            res.append(1 if x[1] in set(Freq.values()) else 0)
    return res
      
#Driver function 
input = [(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)]
print(FreQuery(input))
#output = [1,0]