from collections import UserDict

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

class Name(Field):
    """
    Objects of the class allow to do:
    - keep contact name: as specific value for Field .

    Field have got the following attribute(s): a value.

    Objects of the class is can processed as a specific item of the Record object.
    """
    def __init__(self, value: str):
        super().__init__(self)
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value.isalnum() and len(new_value) > 0:
            self.__value = new_value
        else:
            print("Name can't be empty!")


class Phone(Field):
    """
    Objects of the class allow to do:
    - keep contact phone number: as specific value for Field .

    Field have got the following attribute(s): a value.

    Objects of the class is can processed as a specific item of the Record object.
    """
    def __init__(self, value: str):
        super().__init__(self)
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value.isdigit() and len(new_value) == 10:
            self.__value = new_value
        else:
            print("Only ten digit for phone numder")


class Record:
    '''
    Objects of the class allow to do:
    - keep contact data: a name, a list of phone numbers, a birthday, etc.
    - find and return object 'phone',
    - add new object 'phone',
    - delete object 'phone'.

    Records have got the following attributes: a name as object, a list of phone number objects.

    Objects of the class is can processed as item of AddressBook object.
    '''
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone: str):
        '''
        Recieve a 'phone' string.
        Return from the list a Phone class object with value is 'phone' string.
        '''
        for p in self.phones:
            if phone == p.value:
                return p
        
    def add_phone(self, new_phone: str):
        '''
        Recieve a 'phone' string.
        Add to the list a Phone class object with value is 'new_phone' string.
        Print message with confirmation.
        '''
        if self.find_phone(new_phone):
            print(f'{self.name} have got the {new_phone} phone already.')
        else:
            self.phones.append(Phone(new_phone))
            print(f'{new_phone} is added for {self.name} already.')

    def edit_phone(self, old_phone: str, new_phone: str):
        '''
        Recieve a 'old_phone' string.
        Remove from the list a Phone class object with value is 'old_phone' string and 
        add to the list a Phone class object with value is 'new_phone' string.
        Print message with confirmation.
        '''
        if old_phone == new_phone:
            print(f'{old_phone} is equal to {new_phone}.')
        else:
            phone = self.find_phone(old_phone)
            if phone:
                self.phones.remove(phone)
                self.phones.append(Phone(new_phone))
                print(f'{old_phone} is changed to {new_phone} for {self.name}.')
            else:
                print(f'{self.name} haven\'t got the {new_phone} phone number.')
        
    def remove_phone(self, del_phone: str):
        '''
        Recieve a 'del_phone' string.
        Remove from the list a Phone class object with value is 'del_phone' string.
        Print message with confirmation.
        '''
        phone = self.find_phone(del_phone)
        if phone:
            self.phones.remove(phone)
            print(f'{del_phone} is removed the {self.name}.')
        else:
            print(f'{self.name}\'s haven\'t got the {del_phone} phone number.')  
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones).rstrip('; ')}"

class AddressBook(UserDict):
    '''
    Objects of the class allow to do:
    - keep records with contact data,
    - find and return record as object,
    - add new records,
    - delete record as object.

    Records keep as items of a dict. Dict's keys are a name of the record, dict's values are the record as the object.

    Objects of the class are can processed as separate objects to downloading/saving to a disk, for copying, etc.
    '''

    def find(self, name: str):
        '''
        Recieve a 'name' string.
        Return from the dict a Record class object with key is 'name' string.
        '''
        if name in self.data:
            return self.data[name]

    def delete(self, del_name: str):
        '''
        Recieve a 'del_name' string.
        Remove from the dict a Record class object with key is 'del_name' string.
        Print message with confirmation.
        '''
        record = self.find(del_name)
        if record:
            del record
            print(f'Contact {del_name} is deleted.')
        else:
            print(f'Sorry, but {del_name} is not in your contact book yet. ((')
        
    def add_record(self, new_name: object):
        '''
        Recieve a 'new_name' string.
        Remove from the dict a Record class object with key is 'del_name' string.
        Print message with confirmation.
        '''
        record = self.find(new_name.name)
        if record:
            print(f'Sorry, but {record.name} is in your contact book already. ((')
        else:
            self.data[new_name.name] = new_name
            print(f'Contact {new_name.name} is added.')
