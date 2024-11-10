from abc import ABC, abstractmethod


#Інтерфейс Query_builder_interface. Це абстрактний базовий клас.
#Містить оголошення методів для побудови SQL-запитів.
#Кожен метод у цьому інтерфейсі визначається за допомогою @abstractmethod, тобто є абстрактним.
#Це означає, що його потрібно реалізувати в класах-нащадках.
class Query_builder_interface(ABC):

    @abstractmethod
    #Вибирає таблицю та стовпці
    def select(self, table: str, fields: list[str]) -> None:
        pass

    @abstractmethod
    #Додає умову
    def where(self, condition: str) -> None:
        pass

    @abstractmethod
    #Задає обмеження кількості результатів
    def limit(self, num: int) -> None:
        pass

    @abstractmethod
    #Повертає кінцевий SQL-запит як рядок
    def getSQL(self) -> str:
        pass


#Клас PostgreSQL_Query_builder. Це реалізація Query_builder_interface для PostgreSQL.
class PostgreSQL_Query_builder(Query_builder_interface):

    def __init__(self):
        self._query = ""

    def select(self, table: str, fields: list[str]) -> None:
        fields_str = ", ".join(fields)
        self._query = f"SELECT {fields_str} FROM {table}"

    def where(self, condition: str) -> None:
        self._query += f" WHERE {condition}"

    def limit(self, num: int) -> None:
        self._query += f" LIMIT {num}"

    def getSQL(self) -> str:
        return self._query


#Клас MySQL_Query_builder. Це Реалізація Query_builder_interface для MySQL.
class MySQL_Query_builder(Query_builder_interface):

    def __init__(self):
        self._query = ""

    def select(self, table: str, fields: list[str]) -> None:
        fields_str = ", ".join(fields)
        self._query = f"SELECT {fields_str} FROM {table}"

    def where(self, condition: str) -> None:
        self._query += f" WHERE {condition}"

    def limit(self, num: int) -> None:
        self._query += f" LIMIT {num}"

    def getSQL(self) -> str:
        return self._query


#Це клієнтська функція.
#Вона демонструє, як використовувати PostgreSQL_Query_builder та MySQL_Query_builder для побудови SQL-запитів.
def main():
    #Використання PostgreSQL_Query_builder
    pg_builder = PostgreSQL_Query_builder()
    pg_builder.select("users", ["id", "name", "email"])
    pg_builder.where("id > 19")
    pg_builder.limit(12)
    print("PostgreSQL Query:", pg_builder.getSQL())

    #Використання MySQL_Query_builder
    mysql_builder = MySQL_Query_builder()
    mysql_builder.select("users", ["id", "name", "email"])
    mysql_builder.where("id > 17")
    mysql_builder.limit(15)
    print("MySQL Query:", mysql_builder.getSQL())


if __name__ == "__main__":
    main()
#Патерн "Будівельник" структурує побудову запитів, дозволяючи клієнтському коду працювати з будь-якою реалізацією
#Query_builder_interface не змінюючи основний код.