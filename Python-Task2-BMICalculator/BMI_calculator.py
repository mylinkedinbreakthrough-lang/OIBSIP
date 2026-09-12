print("=" * 40)
print("          BMI CALCULATOR")
print("=" * 40)

try:
    weight_kg = float(input("Enter your weight (kg): "))
    height_m = float(input("Enter your height (m): "))

except ValueError:
    print("Please enter a valid number.")
    exit()

if weight_kg <= 0 or height_m <= 0:
    print("Weight and height must be greater than zero.")
    exit()

bmi = weight_kg / height_m ** 2

print(f"\nBMI: {round(bmi, 2)}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Healthy weight")
elif bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
