import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import json
import sqlite3
from passlib.hash import pbkdf2_sha256


class Ui_MainWindow:

    def __init__(self, master):
        style = ttk.Style()
        style.configure('BW.TLabel', compound='bottom', background="#A0AECD", foreground='white', relief='ridge')
        self.master = master
        self.master.geometry("859x600")
        self.master.configure(background="#FFFFFF")
        self.master.title("MainWindow")

        self.label_2 = tk.Label(self.master)
        self.label_2.place(x=10, y=0, width=900, height=131)
        self.label_2.configure(background="#A0AECD")

        self.abit = ttk.Button(self.master)
        self.abit.place(x=380, y=90, width=245, height=16)
        self.abit.configure(text="Абитуриентам", command=lambda: self.show_abit_info())
        self.abit.configure(style="BW.TLabel")

        self.search = ttk.Button(self.master)
        self.search.place(x=680, y=90, width=246, height=30)
        self.search.configure(text="Поиск по ЕГЭ", command=self.show_student_info)
        self.search.configure(style="BW.TLabel")

        self.label = tk.Label(self.master)
        self.label.place(x=-10, y=-50, width=161, height=181)
        self.img = PhotoImage(file="image\logo.png")
        self.label.configure(image=self.img)

        self.stud = ttk.Button(self.master)
        self.stud.place(x=107, y=90, width=246, height=16)
        self.stud.configure(text="Студентам", command=self.show_student_info)
        self.stud.configure(style="BW.TLabel")

        self.login_button = ttk.Button(self.master)
        self.login_button.place(x=482, y=20, width=157, height=25)
        self.login_button.configure(text="Вход", command=self.show_login)
        self.login_button.configure(style="BW.TLabel")

        self.register_button = ttk.Button(self.master)
        self.register_button.place(x=636, y=20, width=156, height=25)
        self.register_button.configure(text="Регистрация", command=self.show_register)
        self.register_button.configure(style="BW.TLabel")

        self.pushButton = ttk.Button(self.master)
        self.pushButton.place(x=5, y=150, width=271, height=181)
        self.pushButton.configure(text="Электроника и наноэлектроника", style="TButton",
                                  command=lambda: self.show_specialties("Электроника и наноэлектроника"))

        self.pushButton_2 = ttk.Button(self.master)
        self.pushButton_2.place(x=290, y=150, width=271, height=181)
        self.pushButton_2.configure(text="Радиоэлектронные системы и комплексы", style="TButton",
                                    command=lambda: self.show_specialties("Радиоэлектронные системы и комплексы"))

        self.pushButton_4 = ttk.Button(self.master)
        self.pushButton_4.place(x=580, y=150, width=287, height=181)
        self.pushButton_4.configure(text="Информационные системы и технологии", style="TButton",
                                    command=lambda: self.show_specialties("Информационные системы и технологии"))

        self.pushButton_3 = ttk.Button(self.master)
        self.pushButton_3.place(x=290, y=360, width=271, height=181)
        self.pushButton_3.configure(text="Компьютерная безопасность", style="TButton",
                                    command=lambda: self.show_specialties("Компьютерная безопасность"))

        self.pushButton_5 = ttk.Button(self.master)
        self.pushButton_5.place(x=580, y=360, width=287, height=181)
        self.pushButton_5.configure(text="Инноватика", style="TButton",
                                    command=lambda: self.show_specialties("Инноватика"))

        self.pushButton_6 = ttk.Button(self.master)
        self.pushButton_6.place(x=5, y=360, width=287, height=181)
        self.pushButton_6.configure(text="Реклама и связи с общественностью", style="TButton",
                                    command=lambda: self.show_specialties("Реклама и связи с общественностью"))

    def show_student_info(self):
        print("Information for Students")

    def show_abit_info(self):
        self.root = tk.Toplevel(self.master)
        self.ui = UI_Abit_Info(self.root)

    def show_specialties(self, group):
        self.root = tk.Toplevel(self.master)
        self.ui = SpecialtyInfo(self.root, group)

    def show_login(self):
        self.root = tk.Toplevel(self.master)
        self.ui = Login(self.root)

    def show_register(self):
        self.root = tk.Toplevel(self.master)
        self.ui = Register(self.root)


class SpecialtyInfo:
    def __init__(self, master, group):
        self.master = master
        self.master.geometry("600x400")
        self.master.configure(background="#FFFFFF")
        self.master.title(group)

        self.label = tk.Label(self.master)
        self.label.place(x=10, y=10, width=580, height=50)
        self.label.configure(background="#A0AECD", text=group, font=("Arial", 16, "bold"), anchor="center", pady=10)

        self.description_text = tk.Text(self.master)
        self.description_text.place(x=10, y=70, width=580, height=280)
        self.description_text.configure(font=("Arial", 12), wrap="word", state="disabled")

        self.load_specialties(group)

    def load_specialties(self, group):
        with open('priem.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                if item['Конкурсн. группа'] == group:
                    description = f"Специальность: {item['Направление']}\n" \
                                  f"Количество мест: Бюджет - {item['КЦП_Б']}, Коммерция - {item['КЦП_К']}\n" \
                                  f"Минимальный балл: {item['Балл']}\n" \
                                  f"Цена обучения: {item['Цена']} руб.\n\n"
                    self.description_text.configure(state="normal")
                    self.description_text.insert("end", description)
                    self.description_text.configure(state="disabled")


class UI_Abit_Info:
    def __init__(self, master):
        self.master = master
        self.master.geometry("859x600")
        self.master.configure(background="#FFFFFF")
        self.master.title("AbiturHelp")
        self.label_2 = tk.Label(master)
        self.label_2.place(x=5, y=0, width=900, height=131)
        self.label_2.configure(background="#A0AECD")

        self.abit = ttk.Button(master)
        self.abit.place(x=290, y=90, width=245, height=16)
        self.abit.configure(text="Абитуриентам", command=lambda: self.show_abit_info())
        self.abit.configure(style="TButton")

        self.search = ttk.Button(master)
        self.search.place(x=590, y=90, width=246, height=25)
        self.search.configure(text="Поиск по ЕГЭ")
        self.search.configure(style="TButton")

        self.label = tk.Label(self.master)
        self.label.place(x=-10, y=-50, width=161, height=181)
        self.img = PhotoImage(file="image/logo.png")
        self.label.configure(image=self.img)

        self.stud = ttk.Button(self.master)
        self.stud.place(x=30, y=90, width=246, height=16)
        self.stud.configure(text="Студентам")
        self.stud.configure(style="TButton")

        self.login_button = ttk.Button(self.master)
        self.login_button.place(x=482, y=20, width=157, height=25)
        self.login_button.configure(text="Вход", command=self.show_login)
        self.login_button.configure(style="BW.TLabel")

        self.register_button = ttk.Button(self.master)
        self.register_button.place(x=636, y=20, width=156, height=25)
        self.register_button.configure(text="Регистрация", command=self.show_register)
        self.register_button.configure(style="BW.TLabel")

    def show_login(self):
        self.root = tk.Toplevel(self.master)
        self.ui = Login(self.root)

    def show_register(self):
        self.root = tk.Toplevel(self.master)
        self.ui = Register(self.root)


class Login:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.configure(background="#FFFFFF")
        self.master.title("Login")

        self.label = tk.Label(self.master)
        self.label.place(x=10, y=10, width=150, height=25)
        self.label.configure(text="Username:")
        self.label.configure(anchor="w")

        self.username_entry = ttk.Entry(self.master)
        self.username_entry.place(x=170, y=10, width=200, height=25)

        self.label_2 = tk.Label(self.master)
        self.label_2.place(x=10, y=50, width=150, height=25)
        self.label_2.configure(text="Password:")
        self.label_2.configure(anchor="w")

        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.place(x=170, y=50, width=200, height=25)

        self.login_button = ttk.Button(self.master)
        self.login_button.place(x=150, y=100, width=100, height=30)
        self.login_button.configure(text="Login", command=self.login)

        self.master.bind("<Return>", self.login)

    def login(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()
        if user:
            if pbkdf2_sha256.verify(password, user[2]):
                messagebox.showinfo("Success", f"Logged in as {username}")
            else:
                messagebox.showerror("Error", "Invalid username or password!")
        else:
            messagebox.showerror("Error", "Invalid username or password!")
        self.master.destroy()


class Register:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.configure(background="#FFFFFF")
        self.master.title("Register")

        self.label = tk.Label(self.master)
        self.label.place(x=10, y=10, width=150, height=25)
        self.label.configure(text="Username:")
        self.label.configure(anchor="w")

        self.username_entry = ttk.Entry(self.master)
        self.username_entry.place(x=170, y=10, width=200, height=25)

        self.label_2 = tk.Label(self.master)
        self.label_2.place(x=10, y=50, width=150, height=25)
        self.label_2.configure(text="Password:")
        self.label_2.configure(anchor="w")

        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.place(x=170, y=50, width=200, height=25)

        self.label_3 = tk.Label(self.master)
        self.label_3.place(x=10, y=90, width=150, height=25)
        self.label_3.configure(text="Confirm Password:")
        self.label_3.configure(anchor="w")

        self.confirm_password_entry = ttk.Entry(self.master, show="*")
        self.confirm_password_entry.place(x=170, y=90, width=200, height=25)

        self.register_button = ttk.Button(self.master)
        self.register_button.place(x=150, y=140, width=100, height=30)
        self.register_button.configure(text="Register", command=self.register)

        self.master.bind("<Return>", self.register)

    def register(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if password == confirm_password:
            hashed_password = pbkdf2_sha256.hash(password)
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User registered successfully!")
            self.master.destroy()
        else:
            messagebox.showerror("Error", "Passwords do not match!")


def main():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, 
                      username TEXT, 
                      password TEXT)''')
    conn.commit()
    conn.close()

    root = tk.Tk()
    ui = Ui_MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
