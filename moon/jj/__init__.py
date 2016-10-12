from moon import app
from moon.jj.bibtex import render_bib_entry, render_bib_file
from moon.jj.urls import render_parent_breadcrumb
from moon.jj.blog import render_blogs
from moon.jj.people import render_people

app.jinja_env.globals.update(render_parent_breadcrumb=render_parent_breadcrumb)
app.jinja_env.globals.update(render_bib_entry=render_bib_entry)
app.jinja_env.globals.update(render_bib_file=render_bib_file)
app.jinja_env.globals.update(render_blogs=render_blogs)
app.jinja_env.globals.update(render_people=render_people)
