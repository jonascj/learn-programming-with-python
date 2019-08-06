Learn Programming With Python
=============================

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



Building the book
=================

At the moment contributing requires some knowledge of the command line,
let me know if you find an easy GUI-based method of building and previewing.

Linux / macOS
-------------

1. Get a copy of the source:
```
git clone https://github.com/jonascj/learn-programming-with-python
```

2. Make and activate a Python virtual environment any way you like, e.g.:
```
python -m venv some/where/venv-learn-python
source some/where/venv-learn-python/bin/activate
```

3. Install Sphinx and other tools with pip: 
```
(venv-learn-python) $ cd learn-programming-with-python
(venv-learn-python) $ pip install -r reqs.txt
```

4. Build the book/docs:
```
(venv-learn-python) $ make html
```

6. View the html output by opening ``_build/html/index.html``
in your favorite (hopefully open source and cross-platform) webbrowser.

**Remember** to always activate the virtual environment before
building with ``make html``.

Windows
-------
From the cmd.exe (``[win]``+``[r]``, type ``cmd``, press ``[Enter]`` ):

1. Get a copy of the source:
```
C:\Users\username> git clone https://github.com/jonascj/learn-programming-with-python
```
or download and unpack 
https://github.com/jonascj/learn-programming-with-python/archive/master.zip


2. Create a virtual Python environment for the Sphinx tools:
```
C:\Users\username>python -m venv venv-learn-python
```

3. Activate the virtual environment:
```
C:\Users\username>venv-learn-python\Scripts\activate.bat
```

4. Use pip to install Sphinx and other tools into the virtual environment:
```
(learn-python-venv) C:\Users\username>cd learn-programming-with-python
(learn-python-venv) C:\Users\username\learn-programming-with-python>pip install -r reqs.txt
```

5. Build the book with Sphinx:
```
(learn-python-venv) C:\Users\username\learn-programming-with-python>make.bat html
```

6. View the html output by opening ``_build/html/index.html``
in your favorite (hopefully open source and cross-platform) webbrowser.

**Remember** to always activate the virtual environment before
building with ``make.bat html``.


Hosted builds
=============
https://lærpython.dk 
https://laerpython.dk.


How to contribute
=================
1. Get a copy of the source and get building of the book working:
[Building the book](#building-the-book). 

2. Fork this repo on GitHub

3. Clone your own fork, create a new branch ``git checkout -b [name]``
(replace ``[name]`` with a descriptive name of your branch,
maybe ``update-atom-instructions`` if you contribute some update
of the atom instructions).


4. Make your changes, commit them, push them to your forked repo
in your ``[name]`` branch, e.g. ``git push -u origin [name]``.

5. Make a pull request on GitHub 
(https://help.github.com/en/articles/creating-a-pull-request#changing-the-branch-range-and-destination-repository)
