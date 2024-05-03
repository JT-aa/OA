def min_subsequences(source, target):
    
    n = len(source)
    
    curr = 0
    ans = 0
    
    for char in target:
        if char not in source:
            return -1
        while curr < n and source[curr] != char:
            curr += 1
            
        if curr == n:
            ans += 1
            curr = 0
            while curr < n and source[curr] != char:
                curr += 1
                
    return ans + 1
    
# Test cases
print(min_subsequences("abc", "abcbc"))   # Output: 2
print(min_subsequences("abc", "acdbc"))   # Output: -1
print(min_subsequences("xyz", "xzyxz"))   # Output: 3
            
        
        
        