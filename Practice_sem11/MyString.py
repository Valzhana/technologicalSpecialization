# Создайте класс Моя строка, где будут доступны все возможности str,
# дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyString(str):
    """
    A new class that inherits from the string class and also contains additional information
    """
    def __new__(cls, text: str, author: str):
        """
        Creating a new class instance with parameters 'text', 'author' and 'time'
        """
        print('New started')
        instance = super().__new__(cls, text)
        instance.auther = author
        instance.time = time.time()
        return instance

    def __str__(self):
        """
        Output to the console of an object instance with all parameters
        """
        return f'{super().__str__()} created by: {self.auther} at {self.time}'

    def __repr__(self):
        return f'{super().__str__()} {self.auther} {self.time}'


if __name__ == '__main__':

    example_1 = MyString('text_1', 'name_1')
    example_2 = MyString('text_2', 'name_2')

    print(example_1)
    print(example_2)

    print(repr(example_1))
    print(repr(example_2))
    print(MyString.__new__.__doc__)
