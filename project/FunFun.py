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
        if list[1] == lin.name: # совпадает с лингвистик-нейм
            tmpNotion = Notion(lin.first.name)
            index = searchIndexInEntity(entities, tmpNotion)
            if index == -1:
                return 'Не могу ответить на Ваш вопрос'
            else:
                tmpNotion = Notion(lin.second.name)
                return entities[entities.index(tmpNotion)]

# properties, x неболит ХадресХ князева было бы хорошо сделать это
def searchIndexInProperty(first, second):
    for el in propertis:
        if el.first == first and el.second == second:
            return propertis.index(el)
        else:
            return -1

# entities, ling
def searchIndexInEntity(enti, noti):
    for el in enti:
        if el.name == noti.name:
            return enti.index(noti)
        else:
            return -1
