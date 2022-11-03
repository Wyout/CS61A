from os import remove


class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, staff):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)
    
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)
    
class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student
        
    def assist(self, student):
        student.understanding += 1

#-------------------------------------------------------------------------
class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items = []
        self.size = 0

    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
    """
        self.items.append(item)
        self.size += 1

    def pop(self):
        """ Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        min_item = min(self.items)
        print(min_item)
        count_min = self.items.count(min_item)
        for _ in range(count_min):
            self.items.remove(min_item)
        self.size -= count_min