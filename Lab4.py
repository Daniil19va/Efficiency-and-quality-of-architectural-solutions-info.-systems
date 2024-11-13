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


#Клас для надсилання повідомлень у Slack
class Slack:
    #Конструктор приймає login, api_key та chat_id, які використовуються для авторизації в Slack
    def __init__(self, login: str, api_key: str, chat_id: str):
        self.login = login
        self.api_key = api_key
        self.chat_id = chat_id

    #Реалізація відправки повідомлення в Slack
    def post_message(self, header: str, content: str) -> None:
        print(f"Sent Slack message to chat '{self.chat_id}' with title '{header}' that says '{content}'.")


#Клас для надсилання SMS
class SMS:
    #Конструктор приймає phone і sender для ідентифікації отримувача і відправника SMS
    def __init__(self, phone: str, sender: str):
        self.phone = phone
        self.sender = sender

    #Реалізація надсилання SMS
    def send_text(self, title: str, text: str) -> None:
        print(f"Sent SMS to '{self.phone}' from '{self.sender}' with title '{title}' that says '{text}'.")


#Адаптер для Slack
class Slack_adapter(Notification):
    def __init__(self, slack: Slack):
        self.slack = slack

    def send(self, title: str, message: str) -> None:
        #Адаптація виклику send до post_message
        self.slack.post_message(title, message)


#Адаптер для SMS
class SMS_adapter(Notification):
    def __init__(self, sms: SMS):
        self.sms = sms

    def send(self, title: str, message: str) -> None:
        #Адаптація виклику send до send_text
        self.sms.send_text(title, message)


#Клієнтський код
#Працює з Notification, незалежно від того, чи це Email, Slack, або SMS, завдяки адаптерам
def main():
    #Відправка email
    email_notifier = EmailNotification("admin@khpi.edu.ua")
    email_notifier.send("Title1", "Test email notification")

    #Відправка повідомлення у Slack через адаптер
    slack = Slack("user_login", "api_key_1", "1")
    slack_notifier = Slack_adapter(slack)
    slack_notifier.send("Title2", "Test Slack notification")

    #Відправка SMS через адаптер
    sms = SMS("+380991234567", "Admin")
    sms_notifier = SMS_adapter(sms)
    sms_notifier.send("Title3", "Test SMS notification")


if __name__ == "__main__":
    main()
#Адаптери Slack_adapter та SMS_adapter реалізують інтерфейс Notification, дозволяючи використовувати метод send
#Навіть якщо Slack і SMS мають інші методи post_message і send_text