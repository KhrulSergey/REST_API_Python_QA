from unittest import TestCase
from models.post import Post

__author__ = 'Sergey Khrul'


class PostTest(TestCase):
    def test_create_post(self):
        p = Post(title='Test', content='Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)

    def test_json_post(self):
        p = Post(title='Test', content='Test content')
        expected = {'title': 'Test', 'content': 'Test content'}

        self.assertDictEqual(expected, p.json())

