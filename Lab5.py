from abc import ABC, abstractmethod


#Інтерфейс Renderer. Базовий клас для різних форматів подання
class Renderer(ABC):

    @abstractmethod
    #Задає метод render, який приймає словник даних і повертає рядок з даними у певному форматі
    def render(self, data: dict) -> str:
        pass


#Різні типи Рендерів:

#Реалізація рендерингу в HTML
class HTML_renderer(Renderer):
    def render(self, data: dict) -> str:
        return "<html><body>" + "".join(f"<p>{k}: {v}</p>" for k, v in data.items()) + "</body></html>"


#Реалізація рендерингу в JSON
class Json_renderer(Renderer):
    def render(self, data: dict) -> str:
        return str(data)


#Реалізація рендерингу в XML
class XML_renderer(Renderer):
    def render(self, data: dict) -> str:
        return "<xml>" + "".join(f"<{k}>{v}</{k}>" for k, v in data.items()) + "</xml>"


#Кожен з класів реалізує метод render


#Абстракція Page.
#Базовий клас для різних типів сторінок, який приймає об'єкт Renderer і задає метод view, що повертає подання сторінки
class Page(ABC):

    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def view(self) -> str:
        #Повертає подання сторінки
        pass


#Різні типи сторінок
class SimplePage(Page):

    def __init__(self, renderer: Renderer, title: str, content: str):
        super().__init__(renderer)
        self.title = title
        self.content = content

    #Має title та content
    def view(self) -> str:
        data = {"title": self.title, "content": self.content}
        return self.renderer.render(data)


#Модель Product для ProductPage, яка містить дані про товар
class Product:

    def __init__(self, product_id: int, name: str, description: str, image_url: str):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.image_url = image_url


#ProductPage приймає об'єкт класу Product
class ProductPage(Page):

    def __init__(self, renderer: Renderer, product: Product):
        super().__init__(renderer)
        self.product = product

    def view(self) -> str:
        data = {
            "id": self.product.product_id,
            "name": self.product.name,
            "description": self.product.description,
            "image_url": self.product.image_url
        }
        return self.renderer.render(data)


#Клієнтський код. Створюються сторінки з різними рендерами, можна побачити,
#як кожна сторінка може використовувати різні формати подання, змінюючи renderer
def main():
    #Створення рендерерів
    html_renderer = HTML_renderer()
    json_renderer = Json_renderer()
    xml_renderer = XML_renderer()

    #Рендерінг SimplePage з різними рендерерами
    simple_page = SimplePage(html_renderer, "Home", "Welcome")
    print("SimplePage (HTML):")
    print(simple_page.view())

    simple_page.renderer = json_renderer
    print("\nSimplePage (JSON):")
    print(simple_page.view())

    #Рендерінг ProductPage з різними рендерерами
    product = Product(1, "Book", "150 pages", "image_url")
    product_page = ProductPage(xml_renderer, product)
    print("\nProductPage (XML):")
    print(product_page.view())

    product_page.renderer = html_renderer
    print("\nProductPage (HTML):")
    print(product_page.view())


if __name__ == "__main__":
    main()
