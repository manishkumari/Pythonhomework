def city_list():
    cities = []  # Create an empty list to store city names

    # Ask the user for five city names using a for loop
    for i in range(5):
        city = input(f"Enter the name of city {i + 1}: ")
        cities.append(city)  # Add each city to the list

    print("\nThe cities you entered are:")

    # Print the city names one by one using a for/in loop
    for city in cities:
        print(city)


# Run the program
city_list()