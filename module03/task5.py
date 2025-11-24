def get_season(month):
    # Define the seasons in a tuple where each index corresponds to a season
    seasons = ("Winter", "Spring", "Summer", "Autumn")

    # Assign the season based on the month number
    if month in [12, 1, 2]:
        return seasons[0]  # Winter
    elif month in [3, 4, 5]:
        return seasons[1]  # Spring
    elif month in [6, 7, 8]:
        return seasons[2]  # Summer
    elif month in [9, 10, 11]:
        return seasons[3]  # Autumn
    else:
        return None


# Main program
def main():
    # Ask the user to input a month number
    month = int(input("Enter the number of a month (1-12): "))

    # Get the corresponding season
    season = get_season(month)

    # Check if the input is valid and print the season
    if season:
        print(f"The season for month {month} is {season}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")


# Call the main function
main()