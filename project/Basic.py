from Classes import Notion, Property, Linguistics

reservedWords = ['Где']

entities = []  # Cущности
relations = []  # Отношения
propertis = []  # Свойства

entities.append(Notion('Неболит'))  # Сущность-понятие больница "Неболит"
entities.append(Notion('ул. Князева'))  # Сущность-понятие больница "Неболит"

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
