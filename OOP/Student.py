from Person import Person


class Student(Person):
    name= ''
    id = 0

    def __init__(self,id,name,):
        self.name = name
        self.id = id
        super().__init__(self.name,16)

    def saySometing(self):
        print("I'm a student")


def main():
    John = Student(1,"Jhon Smith")
    print("        "+ str(John.id))
    print(John)
    John.saySometing()

if __name__ == '__main__':
    main()