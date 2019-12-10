from Classes import Notion, Property, Linguistics, IsA, Event, KeyWords, PartOf

# Зарезервированные слова, с которых должен начинаться вопрос
reservedWords = ['Где', 'Кем', 'Какая', 'Какой', 'Кто']

entities = []  # Сущности
relations = []  # Отношения
properties = []  # Свойства
keyWords = []  # Ключевые слова для отношений

# Сущности ==============================================================
entities.append(Notion('адрес'))
entities.append(Notion('дата'))
entities.append(Notion('Врач'))
entities.append(Notion('специальность'))
entities.append(Notion('Лор'))
entities.append(Notion('Кардиолог'))
entities.append(Notion('Администратор'))
entities.append(Notion('пациент'))
entities.append(Notion('Неболит'))
entities.append(Notion('ул. Городская, д. 75'))
entities.append(Notion('Волкова'))
entities.append(Notion('Новиков'))
entities.append(Notion('Игорь'))
entities.append(Notion('Марина'))
entities.append(Notion('Костя'))
entities.append(Notion('03.01.2020'))
entities.append(Notion('02.01.2020'))

# События ==============================================================
entities.append(Event('Талон237'))
entities.append(Event('Талон217'))

# Ключевые слова отношений =============================================
keyWords.append(KeyWords('находится'))
keyWords.append(KeyWords('является'))
keyWords.append(KeyWords('получил'))

# Свойства =============================================================
# Свойство Адрес (Неболит - АДРЕС - ул. Городская, д. 75)
addressProperty = Property(entities[entities.index(Notion('Неболит'))],
                           entities[entities.index(Notion('адрес'))],
                           entities[entities.index(Notion('ул. Городская, д. 75'))])
properties.append(addressProperty)

# Свойство Специальность (Волкова - СПЕЦИАЛЬНОСТЬ - Кардиолог)
card = Property(entities[entities.index(Notion('Волкова'))],
                entities[entities.index(Notion('специальность'))],
                entities[entities.index(Notion('Кардиолог'))])
properties.append(card)

# Свойство Специальность (Новиков - СПЕЦИАЛЬНОСТЬ - Лор)
lor = Property(entities[entities.index(Notion('Новиков'))],
               entities[entities.index(Notion('специальность'))],
               entities[entities.index(Notion('Лор'))])
properties.append(lor)

# Свойство Дата (Талон237 - ДАТА - 02.01.2020)
date = Property(entities[entities.index(Event('Талон237'))],
                entities[entities.index(Notion('дата'))],
                entities[entities.index(Notion('02.01.2020'))])
properties.append(date)

# Свойство Дата (Талон217 - ДАТА - 03.01.2020)
date2 = Property(entities[entities.index(Event('Талон217'))],
                 entities[entities.index(Notion('дата'))],
                 entities[entities.index(Notion('03.01.2020'))])
properties.append(date2)

# Отношения ==============================================================
# Отношение Неболит находится ул. Князева
addressRelation = Linguistics(entities[entities.index(Notion('Неболит'))],
                              keyWords[keyWords.index(KeyWords('находится'))],
                              entities[entities.index(Notion('ул. Городская, д. 75'))])
relations.append(addressRelation)

# Отношение Волкова является врач
doctorRelation1 = IsA(entities[entities.index(Notion('Волкова'))],
                      keyWords[keyWords.index(KeyWords('является'))],
                      entities[entities.index(Notion('Врач'))])
relations.append(doctorRelation1)

# Отношение Новиков является врач
doctorRelation2 = IsA(entities[entities.index(Notion('Новиков'))],
                      keyWords[keyWords.index(KeyWords('является'))],
                      entities[entities.index(Notion('Врач'))])
relations.append(doctorRelation2)

# Отношение Игорь является администратор
administrator = IsA(entities[entities.index(Notion('Игорь'))],
                    keyWords[keyWords.index(KeyWords('является'))],
                    entities[entities.index(Notion('Администратор'))])
relations.append(administrator)

# Отношение Марина является пациент
patientMarina = IsA(entities[entities.index(Notion('Марина'))],
                    keyWords[keyWords.index(KeyWords('является'))],
                    entities[entities.index(Notion('пациент'))])
relations.append(patientMarina)

# Отношение Костя является пациент
patientKostya = IsA(entities[entities.index(Notion('Костя'))],
                    keyWords[keyWords.index(KeyWords('является'))],
                    entities[entities.index(Notion('пациент'))])
relations.append(patientKostya)

# Отношение Костя получил Талон237
talonKostya = Linguistics(entities[entities.index(Event('Талон237'))],
                     keyWords[keyWords.index(KeyWords('получил'))],
                     entities[entities.index(Notion('Костя'))])
relations.append(talonKostya)

# Отношение Марина получил Талон237
talonMarina = Linguistics(entities[entities.index(Event('Талон217'))],
                     keyWords[keyWords.index(KeyWords('получил'))],
                     entities[entities.index(Notion('Марина'))])
relations.append(talonMarina)
