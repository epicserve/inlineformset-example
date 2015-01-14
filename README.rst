Django Inline Formset Example
=============================

The Django Inline Formset Example project is an example of how to use Django's
`inlineformset_factory <https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#inline-formsets>`_.
It was originally inspired by Nick Lang's `post <http://lab305.com/news/2012/jul/19/django-inline-formset-underscore/>`_ that demonstrated how to use
the ``inlineformset_factory``.

Setup Instructions
------------------

::

    $ cd ~/Sites
    $ curl -LOk https://github.com/epicserve/inlineformset-example/archive/django_1.7.zip && unzip django_1.7
    $ mv inlineformset-example-django_1.7 inlineformset-example
    $ cd inlineformset-example
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r config/requirements/dev.txt
    $ ./manage.py migrate
    $ ./manage.py runserver

