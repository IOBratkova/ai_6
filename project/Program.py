from FunFun import getAnswer

# Примеры вопросов и ожидаемых ответов:
# Где находится Неболит?  ул. Городская, д. 75. + relations
# Какой адрес у Неболит?  ул. Городская, д. 75. + properties
# Кем является Игорь?     Администратор + relations
# Кем является Марина?     Пациент + relations
# Кем является Костя?     Пациент + relations
# Кем является Волкова? Врач + relations
# Кем является Новиков? Врач + relations
# Какая специальность у Волкова? Кардиолог + properties
# Какая специальность у Новиков? Лор + properties
# Какая дата у Талон237? 02.01.2020 + properties
# Какая дата у Талон217? 03.01.2020 + properties
# Кто получил Талон237? Костя relations +
# Кто получил Талон217? Марина relations +
# Пасхалка: Ты знаешь ответ на главный вопрос Жизни, Вселенной и всего Остального? 42.

flag = True
while flag:
    question = input()
    if question == 'exit':
        flag = False
        break
    elif question[len(question)-1] != '?':
        print('Ты спрашиваешь или утверждаешь? (вопрос должен заканчиваться знаком вопроса)')
    elif question == 'Ты знаешь ответ на главный вопрос Жизни, Вселенной и всего Остального?':
        print('42. Что-нибудь еще?')
    else:
        question = question[0: -1]
        question = question.split()
        answer = getAnswer(question)
        print(answer)
