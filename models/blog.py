import uuid
import datetime
from models.post import Post
from database import Database

class Blog(object):
    def __init__(self, author, title, description, id=None):
    	self.author = author
    	self.title = title
    	self.description = description
    	# Generate a unique ID, if one doesn't exist
    	self.id = uuid.uuid4().hex if id is None else id


    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date (DDMMYYYY), or leave blank for today: ")
        if date == '':
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%y")
        post = Post(blog_id = self.id,
        	        title = title,
        	        content = content, 
        	        author = self.author,
        	        date = date)
        post.save_post()

    def get_posts(self):
    	return Post.from_blog(self.id)


    def save_post(self):
    	Database.insert(collection = 'blogs', 
    		            data = self.to_json())


    def to_json(self):
    	return {
    	    'id': self.id,
    	    'title': self.title,
    	    'author': self.author,
    	    'description': self.description
    	}

    @classmethod
    def get_post(cls, id):
        blog_data = Database.find_one(collection="blogs", query={'id': id})

        if blog_data is not None:
            return cls(author=blog_data['author'],
                       title=blog_data['title'],
                       description=blog_data['description'],
                       id=blog_data['id'])




















