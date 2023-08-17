# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При вызове нового экземпляра класса старые данные из ранее созданнных экземпляров сохраняются
# в пару списков-архивов. list-архивы также являются свойствами экземпляра.


class Archive:
    """
    The class stores a pair of parameters: string and number.
    """
    _instance = None

    def __init__(self, text: str, num: int):
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """
        New class instance, when called it creates two archives from previously created instances.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums_archive = []
            cls._instance.text_archive = []
        else:
            cls._instance.nums_archive.append(cls._instance.num)
            cls._instance.text_archive.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        return f'We have text: {self.text} and number: {self.num}\n' \
               f'Archive of text {Archive._instance.text_archive}\n' \
               f'Archive of numbers {Archive._instance.nums_archive}'

    def __repr__(self):
        return f'We have text: {self.text} and number: {self.num}'


if __name__ == '__main__':
    element_1 = Archive('text_1', 12)
    element_2 = Archive('text_2', 10)
    element_3 = Archive('text_3', 5)
    print(Archive._instance.nums_archive)
    print(element_1)
    print(repr(element_1))

    print(element_1.__new__.__doc__)

