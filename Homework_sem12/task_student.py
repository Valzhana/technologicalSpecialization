import csv
from functools import reduce
from pathlib import Path


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError(f'{self.name} must contain only letters and must begin with title letter')
        else:
            setattr(instance, self.name, value)


class Student:
    name = NameDescriptor()
    second_name = NameDescriptor()
    surname = NameDescriptor()
    _subjects = None

    def __init__(self, name: str, patronymic: str, surname: str, subjects_csv: Path):
        self.name = name
        self.second_name = patronymic
        self.surname = surname
        self.subjects = subjects_csv

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, subjects_csv: Path):
        self._subjects = {"subjects": {}}
        with open(subjects_csv, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._subjects["subjects"][row[0]] = {"marks": [], "tests": [], "average_test": None}
        self._subjects["marks_average"] = None
        self._subjects["middle_test"] = None

    def __call__(self, subject: str, number: int, type_value: str = "subject"):
        if subject not in self.subjects["subjects"].keys():
            raise AttributeError("There is no such a subject in the list")
        if type_value == "subject":
            if number < 2 or number > 5:
                raise ValueError("The value of the mark must be from 2 to 5")
            self.subjects["subjects"][subject]["marks"].append(number)
            self.subjects["marks_average"] = self.get_marks_average(self.subjects)
        elif type_value == "test":
            if number < 0 or number > 100:
                raise ValueError("The value of the mark must be from 0 to 100")
            self.subjects["subjects"][subject]["tests"].append(number)
            mid_test = reduce(lambda x, y: x + y, self.subjects["subjects"][subject]["tests"]) / len(
                self.subjects["subjects"][subject]["tests"])
            self.subjects["subjects"][subject]["average_test"] = mid_test
            self.subjects['middle_test'] = self.get_tests_average(self.subjects)

    @staticmethod
    def get_marks_average(subjects: dict) -> float:
        all_marks = []
        [all_marks.extend(subjects["subjects"][name]["marks"]) for name in subjects["subjects"]]
        return reduce(lambda x, y: x + y, all_marks) / len(all_marks)

    @staticmethod
    def get_tests_average(subjects: dict) -> float:
        all_marks = []
        [all_marks.extend(subjects["subjects"][name]["tests"]) for name in subjects["subjects"]]
        return reduce(lambda x, y: x + y, all_marks) / len(all_marks)

    def __repr__(self):
        result = f'Student_name = {self.name} {self.second_name} {self.surname}\n' \
                 f'Average mark in subjects = {self.subjects["marks_average"]}\n' \
                 f'Average mark in tests = {self.subjects["middle_test"]}\n'
        result += "\nMarks:\n"

        for key, value in self.subjects["subjects"].items():
            result += f'{key} = {value["marks"]}\n'
        result += "\nTests:\n"
        for key, value in self.subjects["subjects"].items():
            result += f'{key} = {value["tests"]}, test average = {value["average_test"]}\n'

        return result


if __name__ == '__main__':
    student_1 = Student("Alexey", "Egorovich", "Ivanov", Path('subjects.csv'))
    student_1("english", 3)
    student_1("chemistry", 5)
    student_1("physics", 5)
    student_1("mathematics", 5)
    student_1("mathematics", 35, "test")
    student_1("mathematics", 99, "test")
    student_1("history", 50, "test")
    student_1("history", 4)
    student_1("biology", 4)
    student_1("physics", 40, "test")
    print(student_1)

    student_2 = Student("Ivan", "Petrovich", "Sergeev", Path('subjects.csv'))
    student_2("physics", 4)
    student_2("english", 5)
    student_2("biology", 3)
    student_2("history", 5)
    student_2("history", 40, "test")
    student_2("chemistry", 98, "test")
    student_2("chemistry", 4)
    student_2("mathematics", 3)
    student_2("mathematics", 55, "test")
    student_2("history", 55, "test")
    print(student_2)
