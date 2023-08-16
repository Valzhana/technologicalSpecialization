# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


from Practice_sem10.task_6 import Fish, Bird, Cat


class AnimalFactory:
    def __init__(self, name_class_animal):
        self.name_class_animal = name_class_animal

    def get_new_animal(self, *args):
        return self.name_class_animal(*args)


if __name__ == '__main__':

    factory_fish = AnimalFactory(Fish)
    my_fish = factory_fish.get_new_animal('Fish', 'Flipper', 'blue', 1.5, 88.7)
    print(my_fish.__str__())

    factory_bird = AnimalFactory(Bird)
    my_bird = factory_bird.get_new_animal('Bird', 'Keisha', 'green', 46.0, 'Africa')
    print(my_bird.__str__())

    factory_cat = AnimalFactory(Cat)
    my_bird = factory_cat.get_new_animal('Cat', 'Luna', 'white', 467.0, False)
    print(my_bird.__str__())
