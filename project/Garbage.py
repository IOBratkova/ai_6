from Basic import reservedWords, relations, entities, propertis
from Classes import Notion

# Какая специальность у Новиков
def searchProperty(list):
    for pr in propertis:
        if pr.name == list[1]:
            fN = Notion(pr.first.name)
            try:
                findex = entities.index(fN)
                if list[3] != fN.name:
                    continue
            except IndexError:
                return 'Слишком сложный вопрос, правда.'
            else:
                sN = Notion(pr.second.name)
                try:
                    sindex = entities.index(sN)
                except IndexError:
                    return 'Как это понимать вообще?'
                else:
                    return entities[sindex]
    return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'

def searchRelation(list):
    # Цикл по отношениям
    for relation in relations:
        # Если слово из отношений совпадает со вторым словом вопроса
        if relation.name == list[1]:
            firstNotion = Notion(relation.first.name)  # Неболит, Игорь
            try:
                firstindex = entities.index(firstNotion)  # Ищем совпадение среди сущностей
                # Если понятие из вопроса не равно найденному перввому понятию известных отношений, ищем дальше
                if list[2] != firstNotion.name:
                    continue
            except IndexError:  # индекс не входит в список элементов
                return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'
            else:
                secondNotion = Notion(relation.second.name)  # Берем второе слово ул. Князева, Администратор
                try:
                    secondindex = entities.index(secondNotion)  # ищем второй индекс
                except IndexError:
                    return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'
                else:
                    return entities[entities.index(secondNotion)]
    return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'
