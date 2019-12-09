from FunFun import getAnswer

# Вопрос из трех слов вводится с вопросительным знаком в конце

# Где находится Неболит?  ул. Князева. +
# Кем является Игорь?     Администратор +
# Кем является Марина?     Администратор +
# Кем является Костя?     Администратор +

flag = True
while flag:
    # ввели вопрос
    question = input()
    # если exit, то выходим
    if question == 'exit':
        flag = False
        break
    elif question[len(question)-1] != '?':
        print('Ты спрашиваешь или утверждаешь?')
    else:
        question = question[0: -1]
        # иначе сплитим строку
        question = question.split()
        #  просим ответ
        answer = getAnswer(question)
        # печатаем ответ
        print(answer)
