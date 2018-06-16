from unittest import TestCase
from models.blog import Blog
from models.post import Post

__author__ = 'Sergey Khrul'


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog(title='Test', author='Maki')
        post_list = [
            Post("Post title", "Post content"),
            Post("Post title2", "Post content2"),
            ]
        b.posts = post_list
        self.assertEqual('Test', b.title)
        self.assertEqual('Maki', b.author)
        self.assertListEqual(post_list, b.posts)

    # def test_repr(self):
    #     b = Blog(title='Test', author='Test Author')
    #     b2 = Blog(title='My Dairy', author='Rolf', posts=['test'])
    #     b3 = Blog(title='My Day', author='Ken', posts=['test', 'probe'])
    #     self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
    #     self.assertEqual(b2.__repr__(), 'My Dairy by Rolf (1 post)')
    #     self.assertEqual(b3.__repr__(), 'My Day by Ken (2 posts)')
