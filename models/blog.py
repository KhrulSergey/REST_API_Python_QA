from models.post import Post

__author__ = 'Sergey Khrul'

PRINT_FORMAT = '{title} by {author} ({post_number} post{multi_posts})'

class Blog:

    def __init__(self, title="", author=""):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return PRINT_FORMAT.format(title=self.title, author=self.author, post_number=len(self.posts),
                                   multi_posts='s' if len(self.posts) != 1 else '')

    def create_post(self, title='', content=''):
        new_post = Post(title, content)
        self.posts.append(new_post)

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }
