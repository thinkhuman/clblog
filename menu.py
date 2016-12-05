from database import Database
from models.blog import Blog

class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back, {}.".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_posts(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input('Enter blog title: ')
        description = input("Enter blog description: ")
        blog = Blog(author = self.user, title = title, description = description)
        blog.save_post()
        self.user_blog = blog


    def run_menu(self):
        read_or_write = input('Do you want to (R)ead, or (W)rite blogs? ')
        if read_or_write.lower() == 'r':
            self._list_blogs()
            self._view_blog()

        elif read_or_write.lower() == "w":
            self.user_blog.new_post()
        else:
            print("Thanks for blogging.")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query = {})
        
        if blogs is not None:
            for blog in blogs:
                print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_choice = input("Enter the ID of the blog you want to read: ")
        blog = Blog.get_post(blog_choice)
        posts = blog.get_posts()
        if posts is not None:
            for post in posts:
                print("Date: {}, Title: {}\n\n{}".format(post['date_created'], post['title'], post['content']))


