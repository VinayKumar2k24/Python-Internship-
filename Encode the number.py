def encode_number(N):
    str_N = str(N)
    encoded_str = ""
    
    for digit in str_N:
        squared_digit = int(digit) ** 2  
        encoded_str += str(squared_digit)  
    
    encoded_value = int(encoded_str)
    
    return encoded_value


N = int(input())

result = encode_number(N)
print(result)
