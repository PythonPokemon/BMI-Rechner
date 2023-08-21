import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI-Rechner")
        self.root.geometry("500x500")

        self.weight_label = ctk.CTkLabel(master=self.root, text="Gewicht (kg):")
        self.weight_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.weight_entry = ctk.CTkEntry(master=self.root)
        self.weight_entry.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)

        self.height_label = ctk.CTkLabel(master=self.root, text="Größe (cm):")
        self.height_label.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

        self.height_entry = ctk.CTkEntry(master=self.root)
        self.height_entry.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

        self.gender_label = ctk.CTkLabel(master=self.root, text="Geschlecht (m/w):")
        self.gender_label.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        self.gender_entry = ctk.CTkEntry(master=self.root)
        self.gender_entry.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        self.age_label = ctk.CTkLabel(master=self.root, text="Alter:")
        self.age_label.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

        self.age_entry = ctk.CTkEntry(master=self.root)
        self.age_entry.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.calculate_button = ctk.CTkButton(master=self.root, text="BMI berechnen", command=self.calculate_bmi)
        self.calculate_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        self.result_label = ctk.CTkLabel(master=self.root, text="")
        self.result_label.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

    def calculate_bmi(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get()) / 100
        gender = self.gender_entry.get().lower()
        age = int(self.age_entry.get())

        bmi = self.calculate_bmi_value(weight, height)
        bmi_category = self.get_bmi_category(bmi)
        bmi_explanation = self.get_bmi_explanation(bmi)

        result_text = f"Ihr BMI beträgt: {bmi:.2f}\nKategorie: {bmi_category}\nErklärung: {bmi_explanation}"
        self.result_label.config(text=result_text)

    def calculate_bmi_value(self, weight, height):
        height_in_meters = height
        bmi = weight / (height_in_meters ** 2)
        return bmi

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Untergewicht"
        elif 18.5 <= bmi < 24.9:
            return "Normalgewicht"
        elif 25 <= bmi < 29.9:
            return "Übergewicht"
        else:
            return "Adipositas (Fettleibigkeit)"

    def get_bmi_explanation(self, bmi):
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

if __name__ == "__main__":
    root = ctk.CTk()
    app = BMICalculatorApp(root)
    root.mainloop()
