from unittest import TestCase
from models.blog import Blog

__author__ = 'Sergey Khrul'


class IntegrationBlogTest(TestCase):
    def test_create_post(self):
        b = Blog(author="Test Author")
        b.create_post("Post title", "Post content")
        b.create_post("Post title2", "Post content2")
        self.assertEqual(len(b.posts), 2)
        self.assertEqual(b.posts[0].title, "Post title")
        self.assertEqual(b.posts[0].content, "Post content")

    def test_json(self):
        b = Blog(title='Test', author='Maki')
        b.create_post("Post title", "Post content")
        b.create_post("Post title2", "Post content2")
        post_list = [
            {'title': "Post title", 'content': "Post content"},
            {'title': "Post title2", 'content': "Post content2"}
        ]
        expected = {'title': 'Test', 'author': 'Maki', 'posts': post_list}
        self.assertDictEqual(expected, b.json())

    def test_json_no_posts(self):
        b = Blog(title='Test', author='Maki')
        expected = {'title': 'Test', 'author': 'Maki', 'posts': []}
        self.assertDictEqual(expected, b.json())
