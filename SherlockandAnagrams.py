def sherlockAndAnagrams(s):
    res = 0
    for i in range(1,len(s)):
        dict = {}
        for j in range(len(s)-i+1):
            print(j) 
            sub = "".join(sorted(s[j:j+i]))
            if sub not in dict:
                dict[sub] = 1
            else:
                dict[sub] +=1
                
            res += dict[sub] - 1                
            
    return res

#Driver code
print(sherlockAndAnagrams("abba")) #4
