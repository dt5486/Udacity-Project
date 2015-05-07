import os


import jinja2
import webapp2

from google.appengine.ext import db

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),autoescape = True)

class Comment(db.Model):
    content = db.StringProperty(multiline=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        items = self.request.get_all("words")
        if items and not items[0]:
            del items[0]
        self.render("notes.html", items = items)
        
    def post(self):
        self.comment = Comment(content=self.request.get('words'))
        

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)