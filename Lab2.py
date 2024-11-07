from abc import ABC, abstractmethod
#ABC(Abstract Base Class) - використовується для створення абстрактних класів, які не можна безпосередньо використовувати для створення об'єкта
#abstractmethod - застосовується для оголошення методів, які обов'язково мають бути реалізовані в дочірніх класах
#ABC і abstractmethod забезпечують єдиний шаблон для всіх класів соціальних мереж і фабрик

#Абстрактний клас соціальної мережі. Це базовий клас, що визначає, які методи повинні мати всі класи соціальних мереж
#Містить два абстрактні методи
class Social_network(ABC):
    @abstractmethod
    #__init__ приймає дані для автентифікації користувача
    def __init__(self, user, password):
        pass

    @abstractmethod
    #post_message — метод для публікації повідомлення.Кожна мережа реалізовує його по-своєму
    def post_message(self, message):
        pass


#Реалізація Facebook
class Facebook(Social_network):
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def post_message(self, message):
        print(f"Публікація на Фейсбук: {message}")
        return True


#Реалізація LinkedIn
class LinkedIn(Social_network):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def post_message(self, message):
        print(f"Публікація на LinkedIn: {message}")
        return True
#Ці класи реалізують методи, визначені в Social_network
#Вони приймають параметри для автентифікації користувача та виводять повідомлення для імітації публікації


#Абстрактний клас для фабричного методу.Він визначає метод create_network, що має реалізувати кожен підклас
class Social_network_creator(ABC):
    @abstractmethod
    #create_network створює об'єкти соціальних мереж, дозволяючи приховати логіку створення
    def create_network(self, *args):
        pass


#Конкретні реалізації
class Facebook_creator(Social_network_creator):
    def create_network(self, login, password):
        return Facebook(login, password)


class LinkedIn_creator(Social_network_creator):
    def create_network(self, email, password):
        return LinkedIn(email, password)
#Ці класи реалізують метод create_network, створюючи об'єкти відповідних соціальних мереж


# Приклад використання
if __name__ == "__main__":
    facebook = Facebook_creator().create_network("user", "password")
    facebook.post_message("Тестова публікація на Фейсбук")

    linkedin = LinkedIn_creator().create_network("user@khpi.edu.ua", "password")
    linkedin.post_message("Тестова публікація на LinkedIn")
#Створюються об'єкти Facebook і LinkedIn через відповідні фабрики та викликається метод post_message, щоб імітувати публікацію