from Basic import reservedWords, relations, entities, propertis
from Classes import Notion

# Где находится Неболит
# Кем является Игорь
def getAnswer(list):
    if list[0] in reservedWords:
        res = searchRelation(list) # Где, кем
        return res
    else:
        return 'Ответ на главный вопрос Жизни, Вселенной и Всего остального - 42. Что-нибудь еще?'

def searchRelation(list):
    #Цикл по отношениям
    for relation in relations:
        #Если слово из отношений совпадает со вторым словом вопроса
        if relation.name == list[1]:
            firstNotion = Notion(relation.first.name) #Неболит, Игорь
            try:
                firstindex = entities.index(firstNotion)   #Ищем совпадение среди сущностей
            except IndexError: #индекс не входит в список элементов
                return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'
            else:
                secondNotion = Notion(relation.second.name) #Берем второе слово ул. Князева, Администратор
                try:
                    secondindex = entities.index(secondNotion) #ищем второй индекс
                except IndexError:
                    return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'
                else:
                    return entities[entities.index(secondNotion)]


# properties, работает, закомменчено выше (23-25) думаю, как оно будет работать для другого
def searchIndexInProperty(first, second):
    for prop in propertis:
        f = prop.first.name
        s = prop.second.name
        if f == first and s == second:
            return propertis.index(prop)
        else:
            return -1

# entities, ling
def searchIndexInEntity(enti, noti):
    for el in enti:
        print(el.name,'el.name')
        if el.name == noti.name:
            return enti.index(noti)
        else:
            return -1
