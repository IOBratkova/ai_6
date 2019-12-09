# ================ Классы-сущности ====================

# Класс Понятие
class Notion:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return other.name == self.name

    def display_info(self):
        print(self.name)

    def __str__(self):
        return self.name


# Класс Событие
class Event:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return other.name == self.name

    def display_info(self):
        print(self.name)


# Класс Свойство
class Property:
    def __init__(self, first, name, second):
        self.first = first
        self.name = name
        self.second = second

    def __eq__(self, other):
        return self.name == other.name \
               and self.second == other.second \
               and self.first == other.first

    def display_info(self):
        print(self.first.name + " " + self.name + " " + self.second.name)

# ================ Классы-отношения ====================
class IsA:
    #
    def __init__(self, first, second, name):
        self.name = name
        self.first = first
        self.second = second


class PartOf:
    def __init__(self, first, second, name):
        self.name = name
        self.first = first
        self.second = second


class Logic:
    def __init__(self, first, second, name):
        self.name = name
        self.first = first
        self.second = second


class Linguistics:
    # first, например, НЕБОЛИТ
    # name, например, НАХОДИТСЯ
    # second, например УЛ КНЯЗЕВА
    def __init__(self, first, name, second ):
        self.name = name
        self.first = first
        self.second = second

    def __eq__(self, other):
        return other.name == self.name and self.second == other.second and self.first == other.first


class Quantifer:
    def __init__(self, first, second, name):
        self.name = name
        self.first = first
        self.second = second
