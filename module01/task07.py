import random
digit1 = random.randint(0,9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0,9)

code_3_digit = f"{digit1}{digit2}{digit3}"

digit4 = random.randint(1,6)
digit5 = random.randint(1,6)
digit6 = random.randint(1,6)
digit7 = random.randint(1,6)

code_4_digit = f"{digit4}{digit5}{digit6}{digit7}"

print("Generated combination codes:")
print(f"3-digit code (0-9):{code_3_digit}")
print(f"4-digit code (1-6):{code_4_digit}")