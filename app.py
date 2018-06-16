__author__ = 'Sergey Khrul'

from models.blog import Blog
from models.post import Post


MENU_PROMPT = 'Enter: \n"c" - to create a blog; \n"l" to list blogs;\n"r" - to read one;\n"p" - to create a post;' \
              '\n"q" - to quit\nChoice: '

POST_TEMPLATE = '''
--- {} --- 

{}

    '''

"""blog_name: Blog object"""
Blogs = dict()


def menu():
    pass
    # Show the user available Blogs
    print_blogs()
    # Let the user make a choice
    selection = input(MENU_PROMPT)
    # Do something with that choice
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)
    # Eventually exit


def print_blogs():
    """Print the available blogs"""
    print("-----Your Blogs-----")
    for key, blog in Blogs.items():  # [(blog_name: Blog), (blog_name: Blog)]
        print("- {}".format(blog))


def ask_create_blog():
    """Create blog in UI"""
    print("----Creating new blog-----")
    title = input("Enter Blog title: ")
    author = input("Enter Blog author: ")

    Blogs[title] = Blog(title, author)


def ask_read_blog():
    """Read (Print) all posts in blog in UI"""
    blog_title = input("Enter Blog title to read: ")
    print_posts(Blogs[blog_title])

    # if len(Blogs) > 0:
    #     is_blog_exist = False
    #     print("----Read blog-----")
    #     post_title = input("Enter Post title: ")
    #     post_content = input("Enter Post content: ")
    #     while not is_blog_exist:
    #         blog_title = input("Enter Blog title to add post: ")
    #         for blog in Blogs:
    #             if blog.title == blog_title:
    #                 is_blog_exist = True
    #                 blog.create_post(post_title, post_content)
    # else:
    #     print("There is no blogs in your account. Please, add One at first")


def print_posts(blog):
    for post in blog.posts:
        _print_post_(post)


def _print_post_(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    """Create post in UI"""
    blog_title = input("Enter Blog title to add a post: ")
    print("----Creating new post-----")
    post_title = input("Enter Post title: ")
    post_content = input("Enter Post content: ")

    Blogs[blog_title].create_post(post_title, post_content)
    # if len(Blogs) > 0:
    #     is_blog_exist = False
    #     print("----Creating new post-----")
    #     post_title = input("Enter Post title: ")
    #     post_content = input("Enter Post content: ")
    #     while not is_blog_exist:
    #         blog_title = input("Enter Blog title to add post: ")
    #         for blog in Blogs:
    #             if blog.title == blog_title:
    #                 is_blog_exist = True
    #                 blog.create_post(post_title, post_content)
    # else:
    #     print("There is no blogs in your account. Please, add One at first")
