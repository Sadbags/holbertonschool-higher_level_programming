#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_student: {self.is_student}")

    def serialize(self, filename):
        """ serialize the object to a file """

        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except:
            print("An error ocurred while serializing object")

    @classmethod
    def deserialize(cls, filename):
        """ deserialize the object """

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except:
            print("An error ocurred while deserialization: {e}")
            return None

    if __name__ == "__main__":
        from task_01_pickle import CustomObject

        # Create an instance of CustomObject
        obj = CustomObject(name="John", age=25, is_student=True)
        print("Original Object:")
        obj.display()

        # Serialize the object
        obj.serialize("object.pkl")

        # Deserialize the object into a new instance
        new_obj = CustomObject.deserialize("object.pkl")
        print("\nDeserialized Object:")
        new_obj.display()
