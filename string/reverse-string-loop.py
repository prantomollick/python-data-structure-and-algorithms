def reverseStringLoop(input_str):
    reverse_str = ''
    for char in input_str[::-1]:
        reverse_str += char
    
    return reverse_str


print(reverseStringLoop("Hello Python"))
    