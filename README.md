Learning Programming With Python
================================

This is a personal project to write a small tutorial / reference book
for various Python teaching activities.

At the moment it is written in Danish, because my current target group
is Danish high-school students.

It is however intended as a general introduction to programming and Python, 
along with varioius other technical topics pertaining to writing
programs in the real world.

So it is my intention to translate it to English.
At the moment you could say I am translating it from English to Danish.
It is much easier to write techinical texts in English
because so many technical terms are being coined first in English.


Cross-platform and open source
==============================

The aim is to only use open source and cross-platform (Linux, macOS and Windows)
components in the book (editors, interpreters, other tools).
Obviously macOS and Windows users will be using proprietary software 
because of their operating systems.

I am personally very fond of Linux for all tasks,
except playing games distributed for Windows,
but I understand that Linux isn't for everyone.
So I'm trying to write for all three major platforms.

In theory only the initial installation and configuration 
of development environment should be platform dependent.
Afterwards Python should be mostly platform independent.

The book itself is also meant to be open source,
written in reStructured text for Sphinx (http://www.sphinx-doc.org/),
source files licenced under GPL-3.0 (see the LICENSE file).



Build the docs
==============

To build the docs on Linux

1. ``git clone https://github.com/jonascj/learn-programming-with-python``

2. Make and activate a Python virtual environment,
e.g. ``python -m venv some/where/venvs/learn-python``
followed by ``source some/where/venvs/learn-python/bin/activate``.

3. ``cd learn-programming-with-python``

4. ``pip install -r reqs.txt``

5. make html 

6. View the html output by opening ``_build/html/index.html``
in your favorite (hopefully open source and cross-platform) webbrowser.


Hosted builds
=============
At any moment the current version will be hosted at 
https://lærpython.dk and https://laerpython.dk.


How to contribute
=================

I will happily accept contributions of writing or other material for the book.

The goal is to make it easy to contribute, 
especialy for the users of the book.

Already there is a lot of text, URLs and screenshots to keep in sync,
and whom better to help keeping them up to date than the users.
