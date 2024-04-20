import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


class Ui_MainWindow:

    def __init__(self, master):
        style = ttk.Style()
        style.configure('BW.TLabel',background="#A0AECD",foreground='white',relief='')
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
        self.search_2.configure(style="B")

        self.search_3 = ttk.Button(self.master)
        self.search_3.place(x=636, y=20, width=156, height=25)
        self.search_3.configure(text="Регистрация")
        self.search_3.configure(style="TButton")


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
