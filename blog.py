from models.blog import Blog
from models.post import Post
from database import Database
from menu import Menu

Database.initialize()
menu = Menu()
menu.run_menu()