import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import json
import sqlite3

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

        self.search_2 = ttk.Button(self.master)
        self.search_2.place(x=482, y=20, width=157, height=25, )
        self.label_2.configure(background="#A0AECD")
        self.search_2.configure(text="Вход")
        self.search_2.configure(style="BW.TLabel")

        self.search_3 = ttk.Button(self.master)
        self.search_3.place(x=636, y=20, width=156, height=25)
        self.search_3.configure(text="Регистрация")
        self.search_3.configure(style="BW.TLabel")

        self.pushButton = ttk.Button(self.master)
        self.pushButton.place(x=5, y=150, width=271, height=181)
        self.pushButton.configure(text="Электроника и наноэлектроника", style="TButton", command=lambda: self.show_specialties("Электроника и наноэлектроника"))

        self.pushButton_2 = ttk.Button(self.master)
        self.pushButton_2.place(x=290, y=150, width=271, height=181)
        self.pushButton_2.configure(text="Радиоэлектронные системы и комплексы", style="TButton", command=lambda: self.show_specialties("Радиоэлектронные системы и комплексы"))

        self.pushButton_4 = ttk.Button(self.master)
        self.pushButton_4.place(x=580, y=150, width=287, height=181)
        self.pushButton_4.configure(text="Информационные системы и технологии", style="TButton", command=lambda: self.show_specialties("Информационные системы и технологии"))

        self.pushButton_3 = ttk.Button(self.master)
        self.pushButton_3.place(x=290, y=360, width=271, height=181)
        self.pushButton_3.configure(text="Компьютерная безопасность", style="TButton", command=lambda: self.show_specialties("Компьютерная безопасность"))

        self.pushButton_5 = ttk.Button(self.master)
        self.pushButton_5.place(x=580, y=360, width=287, height=181)
        self.pushButton_5.configure(text="Инноватика", style="TButton", command=lambda: self.show_specialties("Инноватика"))

        self.pushButton_6 = ttk.Button(self.master)
        self.pushButton_6.place(x=5, y=360, width=287, height=181)
        self.pushButton_6.configure(text="Реклама и связи с общественностью", style="TButton", command=lambda: self.show_specialties("Реклама и связи с общественностью"))

    def show_student_info(self):
        print("Information for Students")

    def show_abit_info(self):
        self.root = tk.Toplevel(self.master)
        self.ui = UI_Abit_Info(self.root)

    def show_specialties(self, group):
        self.root = tk.Toplevel(self.master)
        self.ui = SpecialtyInfo(self.root, group)


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

        self.search_2 = ttk.Button(self.master)
        self.search_2.place(x=482, y=20, width=157, height=25, )
        self.label_2.configure(background="#A0AECD")
        self.search_2.configure(text="Вход")
        self.search_2.configure(style="BW.TLabel")

        self.search_3 = ttk.Button(self.master)
        self.search_3.place(x=636, y=20, width=156, height=25)
        self.search_3.configure(text="Регистрация")
        self.search_3.configure(style="TButton")
        self.score1_txt = ttk.Label(master)
        self.score1_txt.configure(text='Enter your score on first subject:', background='white')
        self.score1_txt.place(x=20, y=200)
        self.score1 = tk.Entry(master)
        self.score1.place(x=280, y=200)
        self.score2_txt = ttk.Label(master)
        self.score2_txt.configure(text='Enter your score on the second subject:', background='white')
        self.score2_txt.place(x=20, y=300)
        self.score2 = tk.Entry(master)
        self.score2.place(x=280, y=300)
        self.score3.configure(text='Enter your score on the third subject:', background='white')
        self.score3.place(x=20, y=300)
        self.score3_txt = tk.Entry(master)
        self.score3_txt.place(x=280, y=300)
        def get_name():
            return self.name.get()

import json
def calculate_score(score1,score2,score3):
    if score1 > 100 or score2 > 100 or score3 > 100:
            print("Incorrect data! Try again!\n")
    else:
        return score1+score2+score3

def show_abit_info():
    root = tk.Toplevel()
    ui = UI_Abit_Info(root)
    root.mainloop()


def main():
    root = tk.Tk()
    ui = Ui_MainWindow(root)
    file1 = open('priem.json', 'r', encoding='utf-8')
    json_data = file1.read()
    data = json.loads(json_data)
    dest = []
    p_b = []
    k_g = []
    p_k = []
    price = []
    min_score = 50
    score = []
    subjects = []
    konk_b = []
    konk_k = []
    print(data)
    root.mainloop()


if __name__ == "__main__":
    main()
