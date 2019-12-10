from FunFun import getAnswer

# Вопрос из трех(четырех) слов вводится с вопросительным знаком в конце

# Где находится Неболит?  ул. Князева. + relations
# Какой адрес у Неболит?  ул. Князева. + properties
# Кем является Игорь?     Администратор + relations
# Кем является Марина?     Пациент + relations
# Кем является Костя?     Пациент + relations
# Кем является Волкова? Врач + relations
# Кем является Новиков? Врач + relations
# Какая специальность у Волкова? Кардиолог + properties
# Какая специальность у Новиков? Лор + properties
# Какая дата у Талон237? 02.01.2020 + properties
# Какая дата у Талон217? 03.01.2020 + properties

flag = True
while flag:
    question = input()
    if question == 'exit':
        flag = False
        break
    elif question[len(question)-1] != '?':
        print('Ты спрашиваешь или утверждаешь?')
    else:
        question = question[0: -1]
        question = question.split()
        answer = getAnswer(question)
        print(answer)
