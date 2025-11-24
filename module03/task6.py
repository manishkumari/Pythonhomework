def main():
    names = set()  # Initialize an empty set to store unique names

    while True:
        # Ask the user to enter a name
        name = input("Enter a name (or press Enter to finish): ").strip()

        # Check if the user entered an empty string to stop the loop
        if name == "":
            break

        # If the name is already in the set, it's an existing name
        if name in names:
            print("Existing name")
        else:
            # If the name is not in the set, add it and print "New name"
            names.add(name)
            print("New name")

    # Print all the names, one per line
    print("\nList of names entered:")
    for name in names:
        print(name)


# Call the main function
main()