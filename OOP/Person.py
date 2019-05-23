from abc import ABCMeta, abstractmethod     #Used in Polymorfism

class Person(object):# <-----Convention parent class Object
    """Constructor of the class"""
    def __init__(self, name, age, job=None, pay=0):
        self.name = name
        self.job = job      #self.job --> public
        self.age = age      #self._age --> protected
        self.__pay = pay      #self.__pay --> private

    def __repr__(self):
        return """
        Name:%s
        Job: %s
        Age: %d
        Pay: %d""" %(self.name,self.job,self.age,self.__pay)

    def setPay(self,newpayment):
        self.__pay = newpayment

    def getPay(self):
        return self.__pay

    @abstractmethod
    def saySometing(self):
        pass

def main():
    Jorge = Person(name="Jorge Castillo Jiménez", job='Database Administrator', age=20, pay=40000)
    print(Jorge)

if __name__ == '__main__':
    main()