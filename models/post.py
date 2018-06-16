__author__ = 'Sergey Khrul'

PRINT_FORMAT = '[Title: {title}, Content: {content}'

class Post:

    def __init__(self, title="", content=""):
        self.title = title
        self.content = content

    def __repr__(self):
        return PRINT_FORMAT.format(title=self.title, content=self.content)

    def get(self, title="Title of post", content="Content of post"):
        self.title = title
        self.content = content

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }
