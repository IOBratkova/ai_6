from Classes import Notion, Property, Linguistics, IsA

reservedWords = ['Где', 'Кем', 'Какая']

entities = []  # Cущности
relations = []  # Отношения
propertis = []  # Свойства

# Где находится Неболит?
entities.append(Notion('Неболит'))  # Сущность-понятие больница "Неболит" факт
entities.append(Notion('ул. Князева'))  # Сущность-понятие адрес "Неболит" факт

# Свойство Адрес
adress = Property(entities[entities.index(Notion('Неболит'))],
                  'Адрес',
                  entities[entities.index(Notion('ул. Князева'))])
propertis.append(adress)

# Отношение Адрес
adress = Linguistics(entities[entities.index(Notion('Неболит'))],
                     'находится',
                     entities[entities.index(Notion('ул. Князева'))])
relations.append(adress)

# Специальность - свойство врача
entities.append(Notion('Врач'))
entities.append(Notion('Волкова'))
entities.append(Notion('Кардиолог'))
entities.append(Notion('Новиков'))
entities.append(Notion('Лор'))

# Волкова является врач
doctor1 = IsA(entities[entities.index(Notion('Волкова'))],
              'является',
              entities[entities.index(Notion('Врач'))])
relations.append(doctor1)

# Новиков является врач
doctor2 = IsA(entities[entities.index(Notion('Новиков'))],
              'является',
              entities[entities.index(Notion('Врач'))])
relations.append(doctor2)

# Волкова специальность кардиолог
kardio = Property(entities[entities.index(Notion('Волкова'))],
                  'специальность',
                  entities[entities.index(Notion('Кардиолог'))])
propertis.append(kardio)

# Новиков специальность лор
lor = Property(entities[entities.index(Notion('Новиков'))],
               'специальность',
               entities[entities.index(Notion('Лор'))])
propertis.append(lor)

# Кем является Игорь? Ответ: Администратор
entities.append(Notion('Игорь'))  # Сущность-понятие Игорь (Факт)
entities.append(Notion('Администратор'))  # Cущность-понятие администратор

# Игорь является Администратором
administrator = IsA(entities[entities.index(Notion('Игорь'))],
                    'является',
                    entities[entities.index(Notion('Администратор'))])
relations.append(administrator)

entities.append(Notion('пациент'))  # Сущность-понятие пациент (Факт)

# Кем является Марина? Ответ: пациент
entities.append(Notion('Марина'))  # Сущность-понятие Марина (Факт)
patientMarina = IsA(entities[entities.index(Notion('Марина'))],
                    'является',
                    entities[entities.index(Notion('пациент'))])
relations.append(patientMarina)

# Кем является Костя? Ответ: пациент
entities.append(Notion('Костя'))  # Сущность-понятие Костя (Факт)
patientKostya = IsA(entities[entities.index(Notion('Костя'))],
                    'является',
                    entities[entities.index(Notion('пациент'))])
relations.append(patientKostya)
