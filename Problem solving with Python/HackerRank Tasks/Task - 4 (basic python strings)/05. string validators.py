s = input()
for check in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
    print(any({getattr(char, check)() for char in s}))
