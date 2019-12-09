from Basic import reservedWords, relations, entities, propertis
from Classes import Notion, Property

# Где находится Неболит
def getAnswer(list):
    if list[0] in reservedWords:
        res = searchRelation(list) # Где находится Неболит

        return res
    else:
        return 'Ответ на главный вопрос Жизни, Вселенной и Всего остального - 42. Что-нибудь еще?'

# ПОиск отношения среди спискаотношений
def searchRelation(list):
    for lin in relations:
        if list[1] == lin.name: # ищем второе слово среди слов в отношениях
            tmpNotion = Notion(lin.first.name)
            index = searchIndexInEntity(entities, tmpNotion)
            if index == -1:
                return 'Не могу ответить на Ваш вопрос'
            else:
                tmpNotion = Notion(lin.second.name)
                #tmpProp = searchIndexInProperty(lin.first.name, lin.second.name)
                #res = propertis[tmpProp]
                #return res.name + " " + res.first.name + " - " + res.second.name
                return entities[entities.index(tmpNotion)]

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
        if el.name == noti.name:
            return enti.index(noti)
        else:
            return -1
