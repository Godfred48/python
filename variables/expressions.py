#converting temperature from Fahrenhiet to degree Celcius
print("=" * 50)
fahrenhiet = float(input("Enter current temperature(Fahrenhiet): "))

celcius = fahrenhiet - 32 * 5/6
print(f"The temperature in Celcius is {celcius:.1f} degrees.")
print()
print("=" * 50)