if __name__ == '__main__':
    weightPounds = int(input("Enter your weight in pounds: "))
    heightInches = int(input("Enter your height in inches: "))

    weightKg = int(input("Enter your weight in kilograms: "))
    heightM = int(input("Enter your height in meters: "))

    BMIPPerInchesSquare = (weightPounds * 703) / (heightInches * heightInches)
    bmi_per = weightKg / (heightM * heightM)
    print("Your Body Mass Index: %.2f  %.2f%n", BMIPPerInchesSquare, bmi_per)
    print("BMI Categories:\n" +
          "Underweight = <18.5\n" +
          "Normal weight = 18.5–24.9\n" +
          "Overweight = 25–29.9\n" +
          "Obesity = BMI of 30 or greater\n");
