# Ask the user for their biological gender
gender = input("Enter your biological gender (female/male): ").strip().lower()

# Ask the user for their hemoglobin value
try:
    hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
except ValueError:
    print("Invalid input for hemoglobin value. Please enter a number.")
    exit()

# Determine the hemoglobin range and status based on gender
if gender == "female":
    if hemoglobin_value < 117:
        status = "low"
    elif 117 <= hemoglobin_value <= 155:
        status = "normal"
    else:
        status = "high"
elif gender == "male":
    if hemoglobin_value < 134:
        status = "low"
    elif 134 <= hemoglobin_value <= 167:
        status = "normal"
    else:
        status = "high"
else:
    print("Invalid biological gender. Please enter 'female' or 'male'.")
    exit()

# Print the result
print(f"Your hemoglobin value is {status}.")