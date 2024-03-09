import re

'''
class Field:
    """
    Objects of the class allow to do:
    - keep contact data: some value.
    Field have got the following attribute(s): a value.
    Objects of the class is can processed as a parent for items of the Record object.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
'''


class Name:
    """
    Objects of the class allow to do:
    - keep contact name: as specific value for Field .
    Field have got the following attribute(s): a value.
    Objects of the class is can processed as a specific item of the Record object.
    """

    def __init__(self, value: str):
        # super().__init__(self)
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        print(type(new_value))
        print(new_value)

        if re.search(r"^[a-zA-Z0-9]+$", new_value):
            print(type(new_value))
            print('---------------------------',new_value)
            self.__value = new_value
        else:
            print("Name can't be empty and must contains characters only")


a = Name("ggg")
print(a.value)

b = Name('rr-rr')
print(b.value)