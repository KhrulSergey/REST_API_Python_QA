import app
from unittest import TestCase
from unittest.mock import patch
from models.blog import Blog
from models.post import Post

__author__ = 'Sergey Khrul'

BLOG_TITLE = 'Blog Title'
AUTHOR = 'SAM'
POST_TITLE = 'Post Title'
POST_CONTENT = 'Post Content'


class AppTest(TestCase):

    def setUp(self):
        blog = Blog(title=BLOG_TITLE, author=AUTHOR)
        app.Blogs = {BLOG_TITLE: blog}

    def test_is_menu_print_promt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()

            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_is_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()

                mocked_print_blogs.assert_called()

    def test_is_menu_calls_create_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_create_blog:
                mocked_input.side_effect = ('c', BLOG_TITLE, AUTHOR, 'q')
                app.menu()

                # We can check if method was called
                mocked_create_blog.assert_called()
                # OR we can check the result of method
                # self.assertIsNotNone(app.Blogs['Blog Title'])

    def test_is_menu_calls_print_list_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:

                mocked_input.side_effect = ('c', BLOG_TITLE, AUTHOR, 'q')
                app.menu()

                mocked_print_blogs.assert_called()


    def test_is_menu_calls_ask_read_blog(self):
        with patch('app.ask_read_blog') as mocked_read_blog:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('r', BLOG_TITLE, 'q')
                app.menu()

                mocked_read_blog.assert_called()

    def test_is_menu_calls_ask_create_post(self):
        app.Blogs[BLOG_TITLE].create_post(POST_TITLE, POST_CONTENT)
        with patch('app.ask_create_post') as mocked_create_post:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('p', BLOG_TITLE, POST_TITLE, POST_CONTENT, 'q')
                app.menu()

                mocked_create_post.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()

            mocked_print.assert_called_with('- ' + BLOG_TITLE + ' by ' + AUTHOR + ' (0 posts)')

    def test_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = (BLOG_TITLE, AUTHOR)
            app.ask_create_blog()

            self.assertIsNotNone(app.Blogs.get(BLOG_TITLE))

    def test_ask_read_blog(self):
        blog = app.Blogs[BLOG_TITLE]
        with patch('builtins.input', return_value=BLOG_TITLE):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = app.Blogs[BLOG_TITLE]
        blog.create_post(POST_TITLE, POST_CONTENT)
        with patch('app._print_post_') as mocked_print_post:
                app.print_posts(blog)

                mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post(POST_TITLE, POST_CONTENT)
#         expected_print = '''
# --- Post Title ---
#
# Post Content
#
#     '''
        with patch('builtins.print') as mocked_print:
            app._print_post_(post)

            mocked_print.assert_called_with(app.POST_TEMPLATE.format(POST_TITLE, POST_CONTENT))
            # mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        p = Post(POST_TITLE, POST_CONTENT)
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = (BLOG_TITLE, POST_TITLE, POST_CONTENT)
            app.ask_create_post()

            # self.assertIsNotNone(app.Blogs.get('Blog Title').posts)
            post_in_blog = app.Blogs[BLOG_TITLE].posts[0]
            self.assertEqual(post_in_blog.title, POST_TITLE)
            self.assertEqual(post_in_blog.content, POST_CONTENT)
