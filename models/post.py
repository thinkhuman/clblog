import uuid
import datetime
from database import Database

class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
    	self.blog_id = blog_id
    	self.title = title
    	self.content = content
    	self.author = author
    	# Generate a unique ID, if one doesn't exist
    	self.id = uuid.uuid4().hex if id is None else id 
    	self.date_created = date

    def save_post(self):
    	Database.insert(collection = 'posts', 
    		            data = self.to_json())

    def to_json(self):
    	return {
    	    'id': self.id,
    	    'blog_id': self.blog_id,
    	    'title': self.title,
    	    'content': self.content,
    	    'author': self.author,
    	    'date_created': self.date_created
    	}

    @classmethod
    def find_post(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(author=post_data['author'],
                   title=post_data['title'],
                   blog_id=post_data['blog_id'],
                   date=post_data["date_created"],
                   content=post_data['content'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(id):
    	return [post for post in Database.find_one(collection='posts', query={'blog_id': id})]







