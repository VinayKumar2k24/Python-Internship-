def next_prime(N):
  num = N + 1

  
  while True:
    
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        is_prime = False
        break

    
    if is_prime:
      return num

    
    num += 1

N = int(input())

result = next_prime(N)


print(result)
