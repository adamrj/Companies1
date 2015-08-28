Intro to CRUD
=============

In this challenge we're going to be building a classic **CRUD** app.

**CRUD** stands for **C**reate - **R**ead - **U**pdate - **D**elete.

For some context, we're going to building a site that simply lists our companies.

#### Your database

Make a Company model that holds a company `name`, `phone number`, and `email address` for a company.

Make sure not to forget to include your postgres settings in `settings.py` and to create the db.

Migrate your db and we're good to start.

#### Notes

Check out our TWO `urls.py` files. `project/urls.py` routes all requests to `/companies` to the `urls.py` file in the companies module. The advantage to this is it lets our app be entirely modular - we can take this app out of this project and put it in another one with minimal work.

Also take a look at the [static folder](https://docs.djangoproject.com/en/dev/howto/static-files/), and the link to the css file inside in our template. If you want to include images, css, javascript files, etc. this is how you do it. The settings for this are of course in settings.py.

#### Create

Make a new route, `/create`, that has a form and will insert a new company into the database.
Your form should look something like this:
```html
<form name="companies" action="/create" method="POST">
	{% csrf_token %}
	<input name="name" type="text">
	...
</form>
```
The post route that the form hits should save the company and redirect back to the main page.

#### Read

In the template and the view function write the necessary code to show a list of all the companies. Make every company a link to a new page that displays their information.

Go back to [Django docs on URLs](https://docs.djangoproject.com/en/dev/topics/http/urls/#named-groups) to accomplish this. You'll need to use the named groups.

It should look something like this:
```py
url(r'^(?P<company_id>[0-9]+)/$', views.company),
```
Make sure you know what this regex is doing!

The template will need a loop to display all the companies. Something like this:
```html
{% for company in companies %}
	<p>{{ company.name }}</p>
{% endfor %}
```
#### Update

Make an update route that takes the company info and populates a form with the info.

You're going to want to load all the company info from the database, and pass it to the template.

In the template, you're going to want something like:
```html
<form name="companies" action="/update" method="POST">
	{% csrf_token %}
	<input name="name" type="text" value="{{company_name}}">
	...
</form>
```
On submit, update the company and redirect to the company's individual page. Put a link to this route on the main page next to each company or on the company's individual page.

#### Delete

Finally, make a route that deletes a company from the database. You don't really need a new page for this - just a route and a redirect. Put the button on the company's individual page.

#### Bonus - the Admin

After you've created a few companies, follow this bit of the [Django Tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial02/) and connect to your built in admin backend. This is kind of a bonus feature in Django that could definitely make your life a little easier. Play around and take a look at its functionality.

#### Resources

[HTTP Methods for Restful Services](http://www.restapitutorial.com/lessons/httpmethods.html)
