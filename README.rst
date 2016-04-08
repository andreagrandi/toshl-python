toshl-python |License MIT|
==========================

|Travis-CI Status|
|PyPI version|

.. |PyPI version| image:: https://badge.fury.io/py/toshl.svg
   :target: https://badge.fury.io/py/toshl

Python client library for Toshl API

Getting started with the library
--------------------------------

| To use the library, you first need to obtain a **token** from Toshl
  API.
| Once you have a token you need to import the library and create an
  instance of the client:

::

    from toshl.client import ToshlClient
    client = ToshlClient('xxx-xxxxx-xxx-xxxxxx-xxxxxx-xxx-xxxxxx')

Every resource exposes the following **methods**:

-  list()
-  search()
-  get()
-  create()
-  update()
-  delete()

To use each resource you will need to create an instance of them,
passing the client as parameter in the constructor.

**Note:** at the moment not all the methods and not all the resources
have been implemented.

Here you can find a couple of examples, but for the complete
documentation you can have a look at the official website
https://developer.toshl.com/docs/

Accounts
~~~~~~~~

::

    from toshl.client import ToshlClient, Account

    client = ToshlClient('xxx-xxxxx-xxx-xxxxxx-xxxxxx-xxx-xxxxxx')
    account = Account(client)

    # list all accounts
    account.list()

    # search for a specific account
    account.search('Test Account')

Categories
~~~~~~~~~~

::

    from toshl.client import ToshlClient, Category

    client = ToshlClient('xxx-xxxxx-xxx-xxxxxx-xxxxxx-xxx-xxxxxx')
    category = Category(client)

    # list all categories
    category.list()

    # search for a specific category
    category.search('Test Category')

Entries
~~~~~~~

::

    from toshl.client import ToshlClient, Entry

    client = ToshlClient('xxx-xxxxx-xxx-xxxxxx-xxxxxx-xxx-xxxxxx')
    entry = Entry(client)

    # create an Entry
    json_payload = {
        'amount': -123.68,
        'currency': {
            'code': 'GBP'
        },
        'date': '2016-04-07',
        'account': 'abcd1234',
        'category': 'category-001'
    }

    response = entry.create(json_payload)

Copyright Note
--------------

| **Toshl** and its logos, design, text, graphics, and other files, and
  the selection arrangement and organization thereof, are owned by
  Toshl.
| This is a 3rd party code and I’m not affiliated nor I work for Toshl.

.. |License MIT| image:: https://go-shields.herokuapp.com/license-MIT-blue.png
.. |Travis-CI Status| image:: https://secure.travis-ci.org/andreagrandi/toshl-python.png?branch=master
   :target: http://travis-ci.org/#!/andreagrandi/toshl-python
