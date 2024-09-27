def determine_winner(n, arr):
    from collections import Counter

    counts = Counter(arr)

    team_a_support = 0
    team_b_support = 0

    for num, count in counts.items():
        if num % 2 == 0:  
            if count % 2 == 0:
                team_a_support += num * count  
            else:
                team_b_support += num * count  
        else:  
            if count % 2 == 0:
                team_b_support += num * count
            else:
                team_a_support += num * count  

    if team_a_support > team_b_support:
        return f"A {team_a_support}"
    elif team_b_support > team_a_support:
        return f"B {team_b_support}"
    else:
        return "T 0"


n = 6
arr = [1, 2, 2, 3, 4, 4]


result = determine_winner(n, arr)
print(result)  
