
#####################    instance and class variable #####################
# class Employee :
#     increment = 1.5 # class variable
#     # Class variables are declared inside a class but outside of any function.
#     def __init__(self,fname,salary):
        # Instance variables are declared inside the constructor which is the __init__method.
        # self.fname = fname # instance variable
        # self.salary = salary # instance variable
        # self.increment = 1.4 # instance variable
    # def increase(self):
        # self.salary = int(self.salary*self.increment) # Ans:: 6160
#         self.salary = int(self.salary*Employee.increment) # Ans:: 6600
#         print(self.salary)
# harry = Employee('harry',4400)
# print(harry.increase())


#########  @staticmethod ###############
# class Student:
#     name = 'unknown' # class attribute
    # def __init__(self):
    #     self.age = 20  # instance attribute
    # @staticmethod
    # def tostring():
        # print('name=',name,'age=',self.age)  # Above, the Student class declares the tostring() method as a static method using the @staticmethod decorator. Note that it cannot have self or cls parameter.
#         print('hello world')

# Student.tostring()    #if you want to print class or instance variable in tostring() it will give you error.


#########  @classmethod ###########
# class Student:
#     name = 'unknown' # class attribute
    # def __init__(self):
    #     self.age = 20  # instance attribute

    # @classmethod
    # def tostring(cls):
        # print('Student Class Attributes: name=',cls.name,', age=', cls.age) # The class method can only access class attributes, but not the instance attributes. It will raise an error if trying to access the instance attribute in the class method.
#         print('Student Class Attributes: name=',cls.name)

# Student.tostring() #calling class method