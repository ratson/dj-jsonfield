dj-jsonfield
===================

This is a fork of `django-jsonfield`_.

Why fork
--------

I need to use `django-jsonfield`_ with `jsonfield`_.
Unfortunately, both have been using the same package name ``jsonfield``,
so I have to maintain a fork.

Difference from upstream
~~~~~~~~~~~~~~~~~~~~~~~~~

- Rename package name from ``jsonfield`` to ``dj_jsonfield``.

.. _django-jsonfield: https://bitbucket.org/schinckel/django-jsonfield
.. _jsonfield: https://github.com/bradjasper/django-jsonfield/

Introduction
------------

I had a serious need for a JSON field for django. There were a couple out
there, but none packaged up nicely on bitbucket/github that were usable
with ``pip install -e``.

So I took the code from `David Cramer's blog`_, and packaged it up.

Usage
-----

To use, just install the package, and then use the field::

    from django.db import models
    import dj_jsonfield

    class MyModel(models.Model):
        the_json = dj_jsonfield.JSONField()

You can assign any JSON-encodable object to this field. It will be
JSON-encoded before being stored in the database as a text value and it
will be turned back into a python list/dict/string upon retrieval from the
database.

There is also a ``TypedJSONField``, that allows you to define data types that must be included within each object in the array. More documentation to follow.


Notes
~~~~~

If no ``default`` is provided, and ``null=True`` is not passed in to the
field constructor, then a default of ``{}`` will be used.


Supported django versions
-------------------------

All versions of Django from 1.8 onwards are tested, however, if you are using Postgres, I highly recommend that you consider using the ``django.contrib.postgres`` module's ``JSONField`` instead.

Extras
------

jsonify templatetag
~~~~~~~~~~~~~~~~~~~
This allows you to convert a python data structure into JSON within a template::

    {% load jsonify %}

    <script>
    var foo = {{ bar|jsonify|safe }};
    </script>

Note that you must only use the "safe" filter when you use the jsonify
filter within a <script> tag (which is parsed like a CDATA section).

If you use it in some other places like in an HTML attribute, then
you must not use the safe filter so that its output is properly escaped::

    <div data-foo="{{ bar|jsonify }}">

The above rules are important to avoid XSS attacks with unsafe strings
stored in the converted data structure.

Todo
----------
Allow for passing in a function to use for processing unknown data types.

Convert date/time objects nicely to/from ISO strings (YYYY-mm-dd HH:MM:SS
TZNAME). This is actually a bit tricky, as we don't know if we are expecting
a date/time object. We may parse objects as we go, but there could be
some performance issues with this. I'm tempted to say "only do this on TypedJSONField()"

`History <https://bitbucket.org/schinckel/django-jsonfield#rst-header-history>`_

.. _David Cramer's blog: http://justcramer.com/2009/04/14/cleaning-up-with-json-and-sql/
.. _IanLewis: https://bitbucket.org/IanLewis
