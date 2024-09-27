def count_returns_to_start(N, A):
    current_position = 0
    return_count = 0
    
    for move in A:
        current_position += move
        if current_position == 0:
            return_count += 1
            
    return return_count


N = int(input())
A = list(map(int,input().split())) 
result = count_returns_to_start(N, A)
print(result)  
