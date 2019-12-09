from Classes import Notion, Property, Linguistics, IsA

reservedWords = ['Где', 'Кем']

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

#Кем является Игорь?
entities.append(Notion('Игорь'))  # Сущность-понятие Игорь (Факт)
entities.append(Notion('Администратор')) #Cущность-понятие администратор

# Игорь является Администратором
administrator = IsA(entities[entities.index(Notion('Игорь'))],
                    'является',
                    entities[entities.index(Notion('Администратор'))])

relations.append(administrator)