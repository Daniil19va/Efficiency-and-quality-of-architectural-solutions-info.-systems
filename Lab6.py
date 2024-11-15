from abc import ABC, abstractmethod


#Інтерфейс Downloader. Містить метод download, який завантажує файл за вказаним URL
class Downloader(ABC):

    @abstractmethod
    def download(self, url: str) -> str:
        pass


#Клас SimpleDownloader. Це реалізація інтерфейсу Downloader, яка завантажує файли
class SimpleDownloader(Downloader):

    def download(self, url: str) -> str:
        print(f"Завантаження даних з {url}")
        return f"Дані завантажені з {url}"


#Клас-проксі CachedDownloader.Це реалізація інтерфейсу Downloader, що додає кешування
class CachedDownloader(Downloader):

    def __init__(self, downloader: Downloader):
        self.downloader = downloader
        self.cache = {}

    def download(self, url: str) -> str:
        #Дані повертаються, якщо вони є в кеші
        if url in self.cache:
            print(f"Повернення кешованих даних для {url}")
            return self.cache[url]
        #Якщо даних немає в кеші, вони завантажуються і додаються
        data = self.downloader.download(url)
        self.cache[url] = data
        return data


#Клієнтський код:
def main():
    #Використання SimpleDownloader (без кешування). Кожне завантаження відбувається повторно
    simple_downloader = SimpleDownloader()
    print("Без кешування:")
    print(simple_downloader.download("https://lab6.khpi/file1"))
    print(simple_downloader.download("https://lab6.khpi/file1"))

    #Використання CachedDownloader (з кешуванням).
    #Використовується кеш для завантажених вже URL, що дозволяє уникати повторного завантаження
    cached_downloader = CachedDownloader(simple_downloader)
    print("\nЗ кешуванням:")
    print(cached_downloader.download("https://lab6.khpi/file1"))
    print(cached_downloader.download("https://lab6.khpi/file1"))
    print(cached_downloader.download("https://lab6.khpi/file2"))


if __name__ == "__main__":
    main()

#CachedDownloader додає кешування без змін у класі SimpleDownloader, дотримуючись принципу відкритості-закритості