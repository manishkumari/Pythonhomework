GRAMS_PER_LOT =13.3
LOTS_PER_POUND =32
POUNDS_PER_TALENT =20

talent = float(input("enter talents:\n"))
pounds =float(input("enter pounds:\n"))
lots = float(input("enter lost:\n"))


grams_from_talents = talent * POUNDS_PER_TALENT * LOTS_PER_POUND * GRAMS_PER_LOT
grams_from_pounds = pounds * LOTS_PER_POUND * GRAMS_PER_LOT
grams_from_lots = lots * GRAMS_PER_LOT

total_grams = grams_from_talents + grams_from_pounds + grams_from_lots

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units")
print(f"{kilograms} kilograms and {grams:2f} grams.")