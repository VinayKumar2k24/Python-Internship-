def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


a, b = map(int, input().split())


gcd_value = gcd(a, b)
lcm_value = lcm(a, b)

print(gcd_value)
print(lcm_value)
