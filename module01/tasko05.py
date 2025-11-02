num1 = int(input("enter the first integer:"))
num2 = int(input("enter the second integer:"))
num3 = int(input("enter the third integer:"))

sum_result = num1 + num2 + num3

product_result = num1 * num2 * num3

average_result =sum_result / 3

print("\n--- Results ---")
print(f"sum:{sum_result}")
print(f"product:{product_result}")
print(f"average:{average_result:.2f}")#format average to two decimals