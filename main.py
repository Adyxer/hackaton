import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


class Ui_MainWindow:

    def __init__(self, master):
        style = ttk.Style()
        style.configure('BW.TLabel',compound='bottom',background="#A0AECD",foreground='white',relief='ridge')
        self.master = master
        self.master.geometry("859x600")
        self.master.configure(background="#FFFFFF")
        self.master.title("MainWindow")

        self.label_2 = tk.Label(self.master)
        self.label_2.place(x=10, y=0, width=900, height=131)
        self.label_2.configure(background="#A0AECD")

        self.abit = ttk.Button(self.master)
        self.abit.place(x=380, y=90, width=245, height=16)
        self.abit.configure(text="Абитуриентам", command=lambda: show_abit_info())
        self.abit.configure(style="BW.TLabel")

        self.search = ttk.Button(self.master)
        self.search.place(x=680, y=90, width=246, height=30)
        self.search.configure(text="Поиск по ЕГЭ",command=self.show_student_info)
        self.search.configure(style="BW.TLabel")
        print(self.search.state())

        self.label = tk.Label(self.master)
        self.label.place(x=-10, y=-50, width=161, height=181)
        self.img = PhotoImage(file="image\logo.png")
        self.label.configure(image=self.img)
        self.stud = ttk.Button(self.master)
        self.stud.place(x=107, y=90, width=246, height=16)
        self.stud.configure(text="Студентам", command=self.show_student_info())
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
        self.pushButton.configure(text="Экономика и финансы", style="TButton")

        self.pushButton_2 = ttk.Button(self.master)
        self.pushButton_2.place(x=290, y=150, width=271, height=181)
        self.pushButton_2.configure(text="Документоведение", style="TButton")

        self.pushButton_4 = ttk.Button(self.master)
        self.pushButton_4.place(x=580, y=150, width=287, height=181)
        self.pushButton_4.configure(text="Информатика и телекоммуникации", style="TButton")

        self.pushButton_3 = ttk.Button(self.master)
        self.pushButton_3.place(x=290, y=360, width=271, height=181)
        self.pushButton_3.configure(text="Инженерия и технологии", style="TButton")

        self.pushButton_5 = ttk.Button(self.master)
        self.pushButton_5.place(x=580, y=360, width=287, height=181)
        self.pushButton_5.configure(text="Бизнес и менеджмент", style="TButton")

        self.pushButton_6 = ttk.Button(self.master)
        self.pushButton_6.place(x=5, y=360, width=287, height=181)
        self.pushButton_6.configure(text="Право и государственное управление", style="TButton")

    def show_student_info(self):
        print("Information for Students")


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
        self.abit.configure(text="Абитуриентам", command=lambda: show_abit_info())
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
        self.name_txt=ttk.Label(master)
        self.name_txt.configure(text='Enter your score on first subject:',background='white')
        self.name_txt.place(x=20,y=200)
        self.name=tk.Entry(master)
        self.name.place(x=280,y=200)
        self.name_txt = ttk.Label(master)
        self.name_txt.configure(text='Enter your score on the second subject:', background='white')
        self.name_txt.place(x=20, y=300)
        self.name = tk.Entry(master)
        self.name.place(x=280, y=300)
        self.name_txt.configure(text='Enter your score on the third subject:', background='white')
        self.name_txt.place(x=20, y=300)
        self.name = tk.Entry(master)
        self.name.place(x=280, y=300)
        def get_name():
            return self.name.get()

import json
def enter_score():
    score_str = input("Введите баллы за предметы(через запятую):\n")
    score_input = score_str.strip().split(',')
    x = False
    n = 0
    for j in range(0, len(score_input)):
        score_input[j] = int(score_input[j])
    if score_input[0] > 100 or score_input[1] > 100 or score_input[2] > 100:
            print("Incorrect data! Try again!\n")
            enter_score()
    else:
        return score_input
file1=open('priem.json','r', encoding='utf-8')
json_data = file1.read()
data = json.loads(json_data)
dest=[]
p_b=[]
k_g=[]
p_k=[]
price=[]
min_score=50
score=[]
subjects=[]
konk_b=[]
konk_k=[]
print(data)

subjects_input=input("Введите предметы (через запятую):")
score_input=enter_score()

subjects_input=subjects_input.strip().split(',')
print(subjects_input)
print(score_input)
total_score=0
for i in score_input:
    total_score+=int(i)
for i in data:
    subjects_temp=[]
    for j in i:
        if j=="Направление":
            dest.append(i[j])
        if j=="Конкурсн. группа":
            k_g.append(i[j])
        if j=="КПЦ_Б":
            p_b.append(i[j])
        if j == "КПЦ_К":
            p_k.append(i[j])
        if j=="Цена":
            price.append(i[j])
        if j in ['Предмет 1','Предмет 2','Предмет 3']:
            subjects_temp.append(i[j])
            if j=='Предмет 3':
                subjects.append(subjects_temp)
                subjects_temp=[]
        if j=="Балл":
            score.append(i[j])
        if j=="Конкурс_Б":
            konk_b.append(i[j])
        if j=="Конкурс_К":
            konk_k.append(i[j])
def show_abit_info():
    root = tk.Toplevel()
    ui = UI_Abit_Info(root)
    root.mainloop()


def main():
    root = tk.Tk()
    ui = Ui_MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
