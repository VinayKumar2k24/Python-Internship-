def max_problems_solved(N, P):
    remaining_time = 240 - P
    
    time_spent = 0
    count = 0
    
    for i in range(1, N + 1):
        time_to_solve = 5 * i
        
        if time_spent + time_to_solve > remaining_time:
            break
        
        time_spent += time_to_solve
        count += 1
    
    return count
N=int(input())
P=int(input())
result=max_problems_solved(N,P)
print(result)
