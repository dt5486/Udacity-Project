import os


import jinja2
import webapp2

from google.appengine.ext import ndb

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),autoescape = False)


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
        items = Comments.query().fetch()
        self.render("notes.html", items = items)
        
    def post(self):
        items = self.request.get("words")
        if not items:
            self.response.out.write('<b>Error!!  You must Add some notes.</b>')
        else:
            words = Comments(words=items)
            words.put()  
        items = Comments.query().fetch()
        self.render("notes.html", items = items)
        
class Comments(ndb.Model):
    words = ndb.StringProperty(required=True)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)