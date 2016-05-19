NetiNeti
========

``netineti`` package is a scientific name discovery tool which uses Naive
Bayes classifier to distinguish between scientific names and other words in
texts. The tool is performing the best with English texts, and the worst with
Italian or Spanish texts. You can read more about ``netineti`` in
`Akella et al. 2012 <http://bit.ly/1Nsfwkh>`_.

Usage
-----

Python scripts Usage
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from neti.neti_neti_trainer import NetiNetiTrainer
    from neti.neti_neti import NetiNeti

    print "Running NetiNeti Training, it might take a while..."

    nnt = NetiNetiTrainer()
    nn = NetiNeti(nnt)

    print nn.find_names("A frog-killing fungus known as Batrachochytrium
    dendrobatidis, or Bd, has already led to the decline of more than 200
    amphibian species including the now extinct-in-the-wild Panamanian
    golden frog.")

RESTful API Usage
~~~~~~~~~~~~~~~~~

Run service with

.. code:: bash

    neti_server

2. Access API like this:

.. code::

    http://localhost:4567/find?type=url&input=http://www.bacterio.cict.fr/d/desulfotomaculum.html

or

.. code::

    http://localhost:4567/find?type=text&input=%22Mus%20musculus%22

RESTful API with Docker
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    docker run -d -p 0.0.0.0:6384:6384 --name netineti gnames/netineti

Files
-----

====================================== =========================================
Files                                  Descriptions
====================================== =========================================
``README.rst``                         this file
``netineti/data/black_list.txt``       "black list" for pre filtering, common words to decrease number of false positives
``netineti/data/white_list.txt``       big training list, run by default
``netineti/data/no_names.txt``         training text w/o scientific names for negative examples
``netineti/data/names_in_context.txt`` training list of names and these names in a context of a sentence.
``netineti/data/test.txt``              American Seashells book (with scientific names) for testing purposes
``netineti/finder.py``               Machine Learning based approach to find scientific names
``netineti/helper.py``        miscellaneous helper functions
``netineti/trainer.py``       Scientific Name classifier -- given a name-like string it accepts or rejects it as a scientific name
====================================== =========================================

Development and Testing
-----------------------

We recommend to use `Docker <https://docs.docker.com/engine/installation/>`_
and `Docker Compose <https://docs.docker.com/compose/install/>`_ to isolate
``netineti`` dependencies from your home system.

Build application's image (needs to be done only if a new gem or new
Ubuntu package are added)

```
docker-compose build

```

Start Docker Compose

```
docker-compose up

```
Run all tests in another terminal window

```
docker-compose run app nosetests -s
```

``netineti`` repository is mapped to its docker container in development
mode, so when you develop new features on host machine all the changes will be
automatically updated in the Docker container as well.
