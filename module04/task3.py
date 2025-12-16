def list(numbers):
    return sum(numbers)
numbers = []
n = int(input("How many numbers?"))
for i in range(n):
    num = int(input("Enter a number:"))
    numbers.append(num)
result = list(numbers)
print("Sum:", result)
