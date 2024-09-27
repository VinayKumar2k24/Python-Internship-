def total_chocolates_for_A(chocolates):
    total_chocolates_A = 0
    
    for jar in chocolates:
        total_chocolates_A += jar // 3
        
        if jar % 3 >= 1:
            total_chocolates_A += 1
            
    return total_chocolates_A
jar=int(input())
chocolates=list(map(int,input(). split ()))
print(total_chocolates_for_A(chocolates))
