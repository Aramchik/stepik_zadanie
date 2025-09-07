from faker import Faker

# Класс Base в него помещяем наш драйвер, метод для сравнения, а так же faker
class Base():

    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker("ru_RU")
        self.name = self.fake.first_name_male()
        self.last_namef = self.fake.last_name_male()
        self.phone_number = self.fake.phone_number()
        self.mailf = self.fake.email()

# Создаем функцию для сравнения 
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result


# Создаем наш faker
    def faker_name(self):
        fake = Faker("en_US")
        name = fake.first_name()
        


