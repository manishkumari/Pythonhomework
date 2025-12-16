def even (numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = even (numbers)
print("Original list:", numbers)
print("Without odd numbers:", result)
