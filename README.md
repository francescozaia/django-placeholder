Django Placeholder image service
================================

The Placeholder image service from CHAPTER 2 of the book [Lightweight Django - Using REST, Websockets, and Backbone](http://shop.oreilly.com/product/0636920032502.do) By Julia Elman, Mark Lavin

I just cleaned up the code to be in a more typical Django structure, maybe it can be useful to someone learning Django.

Create a [virtualenv](http://virtualenv.readthedocs.org/en/latest/). On a mac, run:

    pip install virtualenv
    virtualenv env
    source env/bin/activate

On the newly-created environment, ensure to have all the required dependencies:

    pip install django
    pip install pillow

Run:

    python manage.py runserver