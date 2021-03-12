string_value = input('Enter string value\n')

print(
    f'String {string_value} is a palindrome'
    if string_value[::-1] == string_value
    else f'String {string_value} is not a palindrome'
)
