from Classes import Notion, Property, Linguistics, IsA, Event, KeyWords, PartOf

reservedWords = ['Где', 'Кем', 'Какая', 'Какой', 'Кто']

entities = []  # Cущности
relations = []  # Отношения
propertis = []  # Свойства
keyWords = []

# Где находится Неболит?
entities.append(Notion('Неболит'))  # Сущность-понятие больница "Неболит" факт
entities.append(Notion('ул. Князева'))  # Сущность-понятие адрес "Неболит" факт
entities.append(Notion('адрес'))

# Свойство Адрес
adress = Property(entities[entities.index(Notion('Неболит'))],
                  entities[entities.index(Notion('адрес'))],
                  entities[entities.index(Notion('ул. Князева'))])
propertis.append(adress)

# Отношение Адрес
keyWords.append(KeyWords('находится'))
adress = Linguistics(entities[entities.index(Notion('Неболит'))],
                     keyWords[keyWords.index(KeyWords('находится'))],
                     entities[entities.index(Notion('ул. Князева'))])
relations.append(adress)

# Специальность - свойство врача
entities.append(Notion('Врач'))
entities.append(Notion('Волкова'))
entities.append(Notion('Кардиолог'))
entities.append(Notion('Новиков'))
entities.append(Notion('Лор'))

# Волкова является врач
keyWords.append(KeyWords('является'))
doctor1 = IsA(entities[entities.index(Notion('Волкова'))],
              keyWords[keyWords.index(KeyWords('является'))],
              entities[entities.index(Notion('Врач'))])
relations.append(doctor1)

# Новиков является врач
doctor2 = IsA(entities[entities.index(Notion('Новиков'))],
              keyWords[keyWords.index(KeyWords('является'))],
              entities[entities.index(Notion('Врач'))])
relations.append(doctor2)

entities.append(Notion('специальность'))

# Волкова специальность кардиолог
kardio = Property(entities[entities.index(Notion('Волкова'))],
                  entities[entities.index(Notion('специальность'))],
                  entities[entities.index(Notion('Кардиолог'))])
propertis.append(kardio)

# Новиков специальность лор
lor = Property(entities[entities.index(Notion('Новиков'))],
               entities[entities.index(Notion('специальность'))],
               entities[entities.index(Notion('Лор'))])
propertis.append(lor)

# Кем является Игорь? Ответ: Администратор
entities.append(Notion('Игорь'))  # Сущность-понятие Игорь (Факт)
entities.append(Notion('Администратор'))  # Cущность-понятие администратор

# Игорь является Администратором
administrator = IsA(entities[entities.index(Notion('Игорь'))],
                    keyWords[keyWords.index(KeyWords('является'))],
                    entities[entities.index(Notion('Администратор'))])
relations.append(administrator)

entities.append(Notion('пациент'))  # Сущность-понятие пациент (Факт)

# Кем является Марина? Ответ: пациент
entities.append(Notion('Марина'))  # Сущность-понятие Марина (Факт)
patientMarina = IsA(entities[entities.index(Notion('Марина'))],
                    keyWords[keyWords.index(KeyWords('является'))],
                    entities[entities.index(Notion('пациент'))])
relations.append(patientMarina)

# Кем является Костя? Ответ: пациент
entities.append(Notion('Костя'))  # Сущность-понятие Костя (Факт)
patientKostya = IsA(entities[entities.index(Notion('Костя'))],
                    keyWords[keyWords.index(KeyWords('является'))],
                    entities[entities.index(Notion('пациент'))])
relations.append(patientKostya)

# талон 237
entities.append(Notion('дата'))

entities.append(Event('Талон237'))
entities.append(Notion('02.01.2020'))
date = Property(entities[entities.index(Event('Талон237'))],
                entities[entities.index(Notion('дата'))],
                entities[entities.index(Notion('02.01.2020'))])
propertis.append(date)

# талон 217
entities.append(Event('Талон217'))
entities.append(Notion('03.01.2020'))
date2 = Property(entities[entities.index(Event('Талон217'))],
                 entities[entities.index(Notion('дата'))],
                 entities[entities.index(Notion('03.01.2020'))])
propertis.append(date2)


# кто взял талон
keyWords.append(KeyWords('получил'))
talonKostya = PartOf(entities[entities.index(Event('Талон237'))],
                     keyWords[keyWords.index(KeyWords('получил'))],
                     entities[entities.index(Notion('Костя'))])
relations.append(talonKostya)

talonMarina = PartOf(entities[entities.index(Event('Талон217'))],
                     keyWords[keyWords.index(KeyWords('получил'))],
                     entities[entities.index(Notion('Марина'))])
relations.append(talonMarina)