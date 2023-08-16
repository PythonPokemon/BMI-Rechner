def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Untergewicht"
    elif 18.5 <= bmi < 24.9:
        return "Normalgewicht"
    elif 25 <= bmi < 29.9:
        return "Übergewicht"
    else:
        return "Adipositas (Fettleibigkeit)"

def get_bmi_explanation(bmi):
    if bmi < 16:
        return "Sie haben starkes Untergewicht."
    elif 16 <= bmi < 17:
        return "Sie haben mäßiges Untergewicht."
    elif 17 <= bmi < 18.5:
        return "Sie haben leichtes Untergewicht."
    elif 18.5 <= bmi < 25:
        return "Ihr Gewicht liegt im normalen Bereich."
    elif 25 <= bmi < 30:
        return "Sie haben leichtes Übergewicht."
    elif 30 <= bmi < 35:
        return "Sie haben Adipositas Grad I (Fettleibigkeit)."
    elif 35 <= bmi < 40:
        return "Sie haben Adipositas Grad II (schwere Fettleibigkeit)."
    else:
        return "Sie haben Adipositas Grad III (sehr schwere Fettleibigkeit)."

def main():
    print("Willkommen zum BMI-Rechner!")
    weight = float(input("Bitte geben Sie Ihr Gewicht in Kilogramm ein: "))
    height = float(input("Bitte geben Sie Ihre Größe in Zentimetern ein: "))
    gender = input("Bitte geben Sie Ihr Geschlecht (m/w) ein: ")
    age = int(input("Bitte geben Sie Ihr Alter ein: "))
    
    bmi = calculate_bmi(weight, height)
    print("Ihr BMI beträgt:", round(bmi, 2))
    
    bmi_category = get_bmi_category(bmi)
    print("Sie haben", bmi_category)
    
    bmi_explanation = get_bmi_explanation(bmi)
    print(bmi_explanation)

if __name__ == "__main__":
    main()
