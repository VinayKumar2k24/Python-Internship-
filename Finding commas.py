def count_commas(N):
    if N < 1000:
        return 0  

    total_commas = 0

    
    for num in range(10000, N + 1):
        if num >= 10000:
            total_commas += 1  

    return total_commas


N = 5000


result = count_commas(N)
print(result)  
