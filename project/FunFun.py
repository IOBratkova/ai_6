from Basic import reservedWords, relations, entities, propertis
from Classes import Notion

def getAnswer(question):
    if question[0] in reservedWords:
        if question[2] == 'у':
            return superSearch(question[1], question[3], propertis)
            # return searchProperty(list)
        else:
            return superSearch(question[1], question[2], relations)
            # return searchRelation(list)
    else:
        return 'Вопрос начинается не с зарезервированного слова'


def superSearch(word1, word2, list):
    for element in list:
        if element.name.name == word1:
            fN = Notion(element.first.name)
            try:
                findex = entities.index(fN)
                if word2 != fN.name:
                    continue
            except IndexError:
                return 'Не найдено совпадений среди понятий.'
            else:
                sN = Notion(element.second.name)
                try:
                    sindex = entities.index(sN)
                except IndexError:
                    return 'Как это понимать вообще?'
                else:
                    return entities[sindex]
    return 'Не могу ответить на вопрос, ведь я не понимаю, о чем Вы'
