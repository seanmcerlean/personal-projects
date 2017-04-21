import abc


class Page():
    def __init__(self, page_elements):
        self.elements = tuple(page_elements)

    def print_page(self):
        printable_text = '\n'.join(self.elements)
        print(printable_text)


class AbstractPageBuilder(object, metaclass=abc.ABCMeta):
    def add_break(self):
        pass

    def add_paragraph(self, text):
        pass

    def create_form(self):
        pass


class MarkupPageBuilder(AbstractPageBuilder):
    def __init__(self):
        self.items = []

    def add_break(self):
        self.items.append('<br/>')

    def add_paragraph(self, text):
        self.items.append(
            '<p>{}</p>'
            .format(text)
        )

    def create_page(self):
        return Page(self.items)


class FormDirector():
    def __init__(self, page_builder):
        self.page_builder = page_builder

    def create_text_page(self):
        self.page_builder.add_paragraph("Some text")
        self.page_builder.add_break()
        self.page_builder.add_paragraph("Some more text")
        return self.page_builder.create_page()


if __name__ == "__main__":
    my_builder = MarkupPageBuilder()
    my_director = FormDirector(my_builder)
    current_page = my_director.create_text_page()
    current_page.print_page()
