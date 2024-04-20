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



