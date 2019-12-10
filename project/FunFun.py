from Basic import reservedWords, relations, entities, properties
from Classes import Notion


def getAnswer(question):
    if question[0] in reservedWords:
        if question[2] == 'у':
            return superSearch(question[1], question[3], properties)
        else:
            return superSearch(question[1], question[2], relations)
    else:
        return 'Вопрос начинается не с зарезервированного слова'


def superSearch(word1, word2, arrayOfInformation):
    for element in arrayOfInformation:
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
                    return 'Не найдено совпадений среди понятий'
                else:
                    return entities[sindex]
    return 'Не найдена информация по Вашему вопросу'
