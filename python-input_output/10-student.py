class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

# Example usage:
if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])  # 'middle_name' is not an attribute

    print(j_student_1)  # {'first_name': 'John', 'last_name': 'Doe', 'age': 23}
    print(j_student_2)  # {'first_name': 'Bob', 'age': 27}
    print(j_student_3)  # {'age': 27}
