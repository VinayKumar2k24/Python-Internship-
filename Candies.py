def last_candy_recipient(N, K, A):
    last_child = (A - 1 + K - 1) % N + 1
    return last_child

N, K, A = map(int, input().strip().split())
print(last_candy_recipient(N, K, A))
