#Клас Storage_manager створений для забезпечення того, що об'єкт сховища єдиний для кожного користувача
class Storage_manager:
    _instances = {}

    def __new__(cls, user_id):
        if user_id not in cls._instances:
            cls._instances[user_id] = super(Storage_manager, cls).__new__(cls)
        return cls._instances[user_id]

    #__new__ це метод, який перевіряє, чи існує екземпляр Storage_manager для конкретного user_id вже
    #Якщо немає, створюється новий екземпляр і зберігається в _instances словнику

    def __init__(self, user_id):
        self.user_id = user_id
        self.current_storage = None

    #__init__ у цьому методі зберігається user_id і задається значення None для current_storage
    #Current_storage вказує тип сховища, до якого підключений користувач

    def connect_to_storage(self, storage_type):
    #Метод для підключення користувача до певного сховища та встановлення його як current_storage (Local чи Amazon S3)
    #storage_type це тип сховища, до якого підключається користувач
        self.current_storage = storage_type
        print(f"User {self.user_id} connected to {storage_type} storage.")

    def list_files(self):
    #Метод для відображення файлів у поточному сховищі
    #Повертає список файлів у сховищі.
        pass

    def upload_file(self, file_path):
    #Метод для завантаження файлу у сховище
    #file_path це шлях до файлу, що завантажується
    #Повертає bool значення - успіх операції
        pass

    def download_file(self, file_name, download_path):
    #Метод для завантаження файлу з сховища
    #file_name - ім'я файлу для завантаження
    #download_path це шлях для збереження завантаженого файлу
    #Повертає успіх операції bool
        pass


#Базовий клас, який визначає інтерфейс для взаємодії зі сховищем
class Storage:
    def list_files(self):
    #Метод для отримання списку файлів у сховищі
    #Повертає список файлів у сховищі
        pass

    def upload_file(self, file_path):
    #Метод для завантаження файлу у сховище
    #file_path - шлях до файлу
    #Повертає bool - успіх операції
        pass

    def download_file(self, file_name, download_path):
    #Метод для завантаження файлу з сховища.
    #Повертає успіх операції bool
        pass


#Клас для локального сховища
class Local_storage(Storage):
    pass


#Клас для сховища Amazon S3
class Amazon_S3_storage(Storage):
    pass
#Local_storage і Amazon_S3_storage - це класи, що наслідують Storage
#Вони можуть реалізовувати методи для роботи з локальним сховищем або Amazon S3 відповідно


#Приклад
if __name__ == "__main__":
    user1 = Storage_manager("user19")
    user1.connect_to_storage("Local")

    user2 = Storage_manager("user22")
    user2.connect_to_storage("Amazon S3")

    #Перевірка, що один і той самий об'єкт використовується для одного користувача
    user1_again = Storage_manager("user19")
    print(user1 is user1_again)
    #Результат True

#Коли викликається user1_again = Storage_manager("user19") створюється об’єкт user1_again,
# але замість нового екземпляра повертається той самий об'єкт user1, оскільки вже існує об'єкт для user_id = "user19".
#В результаті print(user1 is user1_again) повертає True,
#що підтверджує, що один і той самий об'єкт використовується для одного користувача.