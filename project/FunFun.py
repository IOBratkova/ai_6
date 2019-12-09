from Basic import reservedWords, relations, entities, propertis
from Classes import Notion

def getAnswer(list):
    if list[0] in reservedWords:
        if list[2] == 'у':
            return superSearch(list[1], list[3], propertis)
            # return searchProperty(list)
        else:
            return superSearch(list[1], list[2], relations)
            # return searchRelation(list)
    else:
        return 'Ответ на главный вопрос Жизни, Вселенной и Всего Остального - 42. Что-нибудь еще?'


def superSearch(word1, word2, list):
    for element in list:
        if element.name == word1:
            fN = Notion(element.first.name)
            try:
                findex = entities.index(fN)
                if word2 != fN.name:
                    continue
            except IndexError:
                return 'Слишком сложный вопрос, правда.'
            else:
                sN = Notion(element.second.name)
                try:
                    sindex = entities.index(sN)
                except IndexError:
                    return 'Как это понимать вообще?'
                else:
                    return entities[sindex]
    return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'
