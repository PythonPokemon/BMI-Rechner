import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anmelden")
        self.root.geometry("500x350")

        self.username_label = ctk.CTkLabel(master=self.root, text="Benutzername:")
        self.username_label.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

        self.username_entry = ctk.CTkEntry(master=self.root)
        self.username_entry.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

        self.password_label = ctk.CTkLabel(master=self.root, text="Passwort:")
        self.password_label.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

        self.password_entry = ctk.CTkEntry(master=self.root, show="*")
        self.password_entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.login_button = ctk.CTkButton(master=self.root, text="Anmelden", command=self.login)
        self.login_button.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hier können Sie die Anmeldeprüfung implementieren
        if username == "admin" and password == "password":
            print("Anmeldung erfolgreich")
        else:
            print("Anmeldung fehlgeschlagen")

if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginApp(root)
    root.mainloop()
