from abc import ABC, abstractmethod


#Інтерфейс Notification. Інтерфейс для всіх типів сповіщень, містить метод send, який приймає заголовок і сповіщення
class Notification(ABC):
    @abstractmethod
    #Відправляє сповіщення
    def send(self, title: str, message: str) -> None:
        pass


#Клас EmailNotification.Реалізує метод send для надсилання email
class EmailNotification(Notification):
    #Конструктор приймає адресу admin_email і зберігає її для надсилання повідомлень
    def __init__(self, admin_email: str):
        self.admin_email = admin_email

    #Реалізація надсилання email
    def send(self, title: str, message: str) -> None:
        print(f"Sent email with title '{title}' to '{self.admin_email}' that says '{message}'.")


#Slack_Notification
class Slack_Notification(Notification):
    #Конструктор приймає login, api_key та chat_id, які використовуються для авторизації в Slack
    def __init__(self, login: str, api_key: str, chat_id: str):
        self.login = login
        self.api_key = api_key
        self.chat_id = chat_id

    #Реалізація відправки повідомлення в Slack
    def send(self, title: str, message: str) -> None:
        print(f"Sent Slack message to chat '{self.chat_id}' with title '{title}' that says '{message}'.")


#SMS_Notification
class SMS_Notification(Notification):
    #Конструктор приймає phone і sender для ідентифікації отримувача і відправника SMS
    def __init__(self, phone: str, sender: str):
        self.phone = phone
        self.sender = sender

    #Реалізація надсилання SMS
    def send(self, title: str, message: str) -> None:
        print(f"Sent SMS to '{self.phone}' from '{self.sender}' with title '{title}' that says '{message}'.")


#Клієнтський код
#Функція main створює екземпляри для кожного типу сповіщення і викликає метод send
def main():
    #Відправка email
    email_notifier = EmailNotification("admin@khpi.edu.ua")
    email_notifier.send("Title1", "Test email notification")

    #Відправка повідомлення у Slack
    slack_notifier = Slack_Notification("user_login", "api_key_1", "1")
    slack_notifier.send("Title2", "Test Slack notification")

    #Відправка SMS
    sms_notifier = SMS_Notification("+380991234567", "Admin")
    sms_notifier.send("Title3", "Test SMS notification")


if __name__ == "__main__":
    main()
#Завдяки використанню інтерфейсу Notification, клієнтський код може працювати з будь-яким типом сповіщення без змін