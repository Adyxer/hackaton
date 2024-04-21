import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter import PhotoImage
import json
import folium
import requests
from geopy.geocoders import Nominatim


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
        self.abit.place(x=380, y=90, width=245, height=25)
        self.abit.configure(text="Абитуриентам")
        self.abit.configure(style="TButton")

        self.search = ttk.Button(self.master)
        self.search.place(x=680, y=90, width=206, height=30)
        self.search.configure(text="Поиск по ЕГЭ", command=lambda: self.show_abit_info())
        self.search.configure(style="TButton")

        self.label = tk.Label(self.master)
        self.label.place(x=-10, y=-50, width=161, height=181)
        self.img = PhotoImage(file="image\logo.png")
        self.label.configure(image=self.img)

        self.stud = ttk.Button(self.master)
        self.stud.place(x=107, y=90, width=246, height=25)
        self.stud.configure(text="Студентам", command=self.show_student_info)
        self.stud.configure(style="TButton")

        self.search_2 = ttk.Button(self.master)
        self.label_2.configure(background="#A0AECD")
        self.search_2.configure(text="Вход")
        self.search_2.configure(style="TButton")

        self.search_3 = ttk.Button(self.master)
        self.search_3.configure(text="Регистрация")
        self.search_3.configure(style="TButton")

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
        self.root = tk.Toplevel(self.master)
        self.ui = UI_Stud_Info(self.root)

    def show_specialties(self, group):
        self.root = tk.Toplevel(self.master)
        self.ui = SpecialtyInfo(self.root, group)

    def show_abit_info(self):
        self.root = tk.Toplevel(self.master)
        self.ui = UI_Abit_Info(self.root)


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
        self.abit.place(x=290, y=90, width=245, height=25)
        self.abit.configure(text="Абитуриентам", command=lambda: self.show_abit_info())
        self.abit.configure(style="TButton")

        self.search = ttk.Button(master)
        self.search.place(x=590, y=90, width=246, height=25)
        self.search.configure(text="Поиск по ЕГЭ", command=lambda: self.show_abit_info())
        self.search.configure(style="TButton")

        self.label = tk.Label(self.master)
        self.label.place(x=-10, y=-50, width=161, height=181)
        self.img = PhotoImage(file="image/logo.png")
        self.label.configure(image=self.img)

        self.stud = ttk.Button(self.master)
        self.stud.place(x=30, y=90, width=246, height=25)
        self.stud.configure(text="Студентам")
        self.stud.configure(style="TButton")

        self.search_2 = ttk.Button(self.master)
        self.label_2.configure(background="#A0AECD")
        self.search_2.configure(text="Вход")
        self.search_2.configure(style="TButton")

        self.search_3 = ttk.Button(self.master)
        self.search_3.configure(text="Регистрация")
        self.search_3.configure(style="TButton")
        self.subject1_txt = ttk.Label(master)
        self.subject1_txt.configure(text='Выберите предмет ЕГЭ:', background='white')
        self.subject1_txt.place(x=20, y=150)
        self.subject1 = ttk.Combobox(master)
        self.subject1.place(x=280, y=150)

        self.score1_txt = ttk.Label(master)
        self.score1_txt.configure(text='Введите баллы ЕГЭ:', background='white')
        self.score1_txt.place(x=20, y=200)
        self.score1 = tk.Entry(master)
        self.score1.place(x=280, y=200)

        self.subject2_txt = ttk.Label(master)
        self.subject2_txt.configure(text='Выберите предмет ЕГЭ:', background='white')
        self.subject2_txt.place(x=20, y=250)
        self.subject2 = ttk.Combobox(master)
        self.subject2.place(x=280, y=250)

        self.score2_txt = ttk.Label(master)
        self.score2_txt.configure(text='Введите баллы ЕГЭ:', background='white')
        self.score2_txt.place(x=20, y=300)
        self.score2 = tk.Entry(master)
        self.score2.place(x=280, y=300)

        self.subject3_txt = ttk.Label(master)
        self.subject3_txt.configure(text='Выберите предмет ЕГЭ:', background='white')
        self.subject3_txt.place(x=20, y=350)
        self.subject3 = ttk.Combobox(master)
        self.subject3.place(x=280, y=350)

        self.score3_txt = ttk.Label(master)
        self.score3_txt.configure(text='Введите баллы ЕГЭ:', background='white')
        self.score3_txt.place(x=20, y=400)
        self.score3 = tk.Entry(master)
        self.score3.place(x=280, y=400)

        self.calculate_btn = ttk.Button(master, text="Вычислить", command=self.calculate_score)
        self.calculate_btn.place(x=150, y=450)

        self.total_score_label = ttk.Label(master, text="Сумма баллов:")
        self.total_score_label.place(x=20, y=500)

        self.total_score_value = ttk.Label(master, text="")
        self.total_score_value.place(x=150, y=500)

        self.available_specialties_label = ttk.Label(master, text="Возможные специальности:")
        self.available_specialties_label.place(x=520, y=150)

        self.available_specialties_value = tk.Text(master, height=15, width=35)
        self.available_specialties_value.place(x=520, y=180)

        self.load_subjects()

    def load_subjects(self):
        subjects = set()
        with open('priem.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                subjects.add(item["Предмет 1"])
                subjects.add(item["Предмет 2"])
                subjects.add(item["Предмет 3"])

        self.subject1['values'] = list(subjects)
        self.subject2['values'] = list(subjects)
        self.subject3['values'] = list(subjects)

    def calculate_score(self):
        subject1 = self.subject1.get()
        score1 = int(self.score1.get())
        subject2 = self.subject2.get()
        score2 = int(self.score2.get())
        subject3 = self.subject3.get()
        score3 = int(self.score3.get())

        if score1 > 100 or score2 > 100 or score3 > 100:
            print("Некорректные баллы!\n")
        elif subject1 == subject2 or subject1 == subject3 or subject2 == subject3:
            print("Вы можете выбрать один и тот же предмет только один раз!")
        else:
            total_score = score1 + score2 + score3
            self.total_score_value.configure(text=str(total_score))
            self.find_specialties(subject1, subject2, subject3, total_score)

    def find_specialties(self, subject1, subject2, subject3, total_score):
        available_specialties = []
        with open('priem.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                if total_score >= item["Балл"]:
                    subjects = [item["Предмет 1"], item["Предмет 2"], item["Предмет 3"]]
                    if self.match_subjects(subjects, [subject1, subject2, subject3]):
                        available_specialties.append(item["Направление"])

        if available_specialties:
            self.available_specialties_value.delete('1.0', tk.END)
            for specialty in available_specialties:
                self.available_specialties_value.insert(tk.END, specialty + '\n')
        else:
            self.available_specialties_value.delete('1.0', tk.END)
            self.available_specialties_value.insert(tk.END, "Нет специальностей подходящих под введённые данные")

    def show_student_info(self):
        self.root = tk.Toplevel(self.master)
        self.ui = UI_Stud_Info(self.root)

    def show_abit_info(self):
        self.root = tk.Toplevel(self.master)
        self.ui = UI_Abit_Info(self.root)

    def match_subjects(self, subjects, chosen_subjects):
        return set(subjects) == set(chosen_subjects)

    def show_map(self):
        user_location = self.get_user_location()
        vehicles_data = self.get_vehicles_near_user(user_location, radius=2000)
        self.plot_vehicles_on_map(user_location, vehicles_data)

    def get_user_location(self):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode("Saint Petersburg")
        return location.latitude, location.longitude

    def get_vehicles_near_user(self, user_location, radius=1000):
        user_latitude, user_longitude = user_location
        url = f"https://api.um.warszawa.pl/api/action/wsstore_get/?id=2c4f8e9b-7c7c-44f8-a825-bdf781254622&lat={user_latitude}&lng={user_longitude}&apikey=3647c929-5ef9-408e-a423-342a47499a36&dist={radius}"
        response = requests.get(url)
        return response.json()

    def plot_vehicles_on_map(self, user_location, vehicles_data):
        map_osm = folium.Map(location=user_location, zoom_start=15)
        for vehicle in vehicles_data:
            lat = vehicle['lat']
            lon = vehicle['lon']
            popup = f"Line: {vehicle['Line']}, Brigade: {vehicle['Brigade']}"
            folium.Marker([lat, lon], popup=popup).add_to(map_osm)
        map_osm.save("map.html")
        webbrowser.open("map.html")


class UI_Stud_Info:

    def __init__(self, master):
        self.master = master
        self.master.geometry("859x600")
        self.master.configure(background="#FFFFFF")
        self.master.title("StudHelp")
        self.label_2 = tk.Label(master)
        self.label_2.place(x=5, y=0, width=900, height=131)
        self.label_2.configure(background="#A0AECD")

        self.abit = ttk.Button(master)
        self.abit.place(x=290, y=90, width=245, height=25)
        self.abit.configure(text="Абитуриентам")
        self.abit.configure(style="TButton")

        self.search = ttk.Button(master)
        self.search.place(x=590, y=90, width=246, height=25)
        self.search.configure(text="Поиск по ЕГЭ", command=lambda: self.show_abit_info())
        self.search.configure(style="TButton")

        self.label = tk.Label(self.master)
        self.label.place(x=-10, y=-50, width=161, height=181)
        self.img = PhotoImage(file="image/logo.png")
        self.label.configure(image=self.img)
        self.stud = ttk.Button(self.master)
        self.stud.place(x=30, y=90, width=246, height=25)
        self.stud.configure(text="Студентам")
        self.stud.configure(style="TButton")
        self.search_2 = ttk.Button(self.master)
        self.label_2.configure(background="#A0AECD")
        self.search_2.configure(text="Вход")
        self.search_2.configure(style="BW.TLabel")

        self.search_3 = ttk.Button(self.master)
        self.search_3.configure(text="Регистрация")
        self.search_3.configure(style="TButton")

        def show_student_info(self):
            print("")

        def show_abit_info(self):
            self.root = tk.Toplevel(self.master)
            self.ui = UI_Abit_Info(self.root)


def main():
    root = tk.Tk()
    ui = Ui_MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()