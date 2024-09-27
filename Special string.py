def min_ascii_distance(A, S):
    total_distance = 0
    found_all = True
    
    for char_a in A:
        min_distance = float('inf')
        for char_s in S:
            distance = abs(ord(char_a) - ord(char_s))
            if distance < min_distance:
                min_distance = distance
        
        if min_distance != 0:
            found_all = False
            total_distance += min_distance
    
    return total_distance if not found_all else 0

A = "abcd"
S = "xyz"


result = min_ascii_distance(A, S)
print(result)  
