Django Inline Formset Example
=============================

The Django Inline Formset Example project is an example of how to use Django's
`inlineformset_factory <https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#inline-formsets>`_.
It was originally inspired by Nick Lang's `post <http://lab305.com/news/2012/jul/19/django-inline-formset-underscore/>`_ that demonstrated how to use
the ``inlineformset_factory``.

Setup Instructions
------------------

Before you begin make sure you've setup and installed `Virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_.

Create a directory for your new Django site. ::

$ cd ~/Sites

In the same directory run the following command to setup a virtualenv for your new site. ::

$ mkvirtualenv --no-site-packages --distribute inlineformset-example

Clone the ``inlineformset-example`` example. ::

$ git clone https://github.com/epicserve/inlineformset-example.git

Install the base requirements and development requirements. ::

$ cd inlineformset-example
$ pip install -r config/requirements/dev.txt

Add the `DJANGO_PROJECT_ROOT` to your Python path. ::

$ add2virtualenv .

Set your ``DJANGO_SETTINGS_MODULE`` environment variable (You'll need to do this everytime you work on this project). ::

$ export DJANGO_SETTINGS_MODULE=config.settings.development

Setup your database::

$ django-admin.py syncdb
$ django-admin.py migrate

At this point your base site should be setup and you can now run your dev server. ::

$ django-admin.py runserver
