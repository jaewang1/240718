class person:
    def __init__(self, n, a, p):
        self.name = n
        self.age = a
        self.phone = p
    def print_info(self):
        print("이름: ", self.name,
              "\n나이: ", self.age,
              "\n연락처: ", self.phone)

my_person = person("이재왕", "27", "010-****-****")
my_person.print_info()


