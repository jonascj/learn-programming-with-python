.. include:: global.rst

############################
Lær programmering med Python
############################

.. image:: figs/python-logo-master-v3-TM.png
    :align: center
    :scale: 100%
    :target: https://python.org/

**********************
Hvad er programmering?
**********************

Computerprogrammering er en process eller disciplin
som handler om at designe og bygge computerprogrammer.

Et computerprogram er en samling af instruktioner
som løser en specifik opgave
når de udføres af en computer.
Eksempler på instruktioner kunne være:

* Tegn et kvadrat på skærmen
* Skriv tekst på skærmen
* Vent på der trykkes på en tast på tastaturet
* Afspil lyd
* Send data (tekst, billeder, tal osv.) over netværket til en anden computer
* Tjek om to værdier er ens
* Udregn et regnestykke

Alle computerprogrammer består af instruktioner
som disse i passende rækkefølge;
computerspil,
webbrowsere, tekstbehandlingsprogrammer
osv.

En sådan samling af instruktioner
kaldes for et programs *kildekode* eller blot *kode*.
Kildekode skrives af en programmør
i et menneskelæseligt programmeringssprog,
f.eks. *Python*.

******
Python
******

*Python* [#python-name]_ er
et af verdens mest populære programmeringssprog [#python-popularity]_.
Alment kendte programmer eller services som bruger Python i stort omfang
inkluderer:

* Spotifys serverdel er skrevet primært i Python [#spotify-use-python]_.
    .. image:: figs/Spotify_logo_with_text.svg.png
        :scale: 50%
        :target: https://en.wikipedia.org/wiki/Spotify


* Instagrams website er skrevet i Python
  (frameworket `Django <https://www.djangoproject.com/>`_)
  [#instagram-use-python]_.

    .. image:: figs/Instagram_logo.svg.png
        :scale: 50%
        :target: https://en.wikipedia.org/wiki/Instagram


* Dropbox er skrevet primært i Python [#dropbox-use-python]_.

    .. image:: figs/Dropbox_logo_2017.svg.png
        :scale: 50%
        :target: https://en.wikipedia.org/wiki/Dropbox_(service)

Python bruges til dataanalyse, webservices, automatisering af diverse opgaver,
Machine Learning, spil og uddannelse [#python-usage]_.


..  lol literalinclude:: hello.py
    :caption: Du er lol :download:`hello.py <hello.py>`


****************************
Lær programmering med Python
****************************

Formålet med bogen her er at lære dig
at programmere en computer vha. Python.
Det antages, at du aldrig har skrevet og bygget computerprogrammer før.
Bogen begynder således helt fra bunden.
Det antages dog, at du har et vist kendskab til din egen computer.

Bogen kan læses ved at læse
de nummererede kapitler i numerisk rækkefølge.
Steder hvor det kan give mening at sprige rundt i bogen
vil være markerede.

Visse opgaver løses forskelligt i Windows, macOS og Linux.
Derfor indeholder flere kapitler afsnit målrettet
hvert af de tre operativsystemer.

Bogen indeholder også en række appendikser
der vil blive henvist til relevante steder.
Det er typisk løsningen på tekniske opgaver
som ikke direkte er relateret til Python-programmering.


.. toctree::
    :caption: Indhold
    :numbered: 3
    :maxdepth: 3

    ch-installation/installation
    ch-first-program-first-error/first-program-first-error
    ch-informal-introduction/informal-introduction
    ch-processing-python-mode/processing-python-mode


.. toctree::
    :caption: Udvalgte emner
    :numbered: 3
    :maxdepth: 3

    ch-database/database


.. toctree::
    :caption: Appendiks
    :numbered: 3
    :maxdepth: 3

    ch-os-misc/os-misc
    ch-os-cli/os-cli
    ch-git/git
    ch-os-filesystem-hierarchy/os-filesystem-hierarchy
    ch-editor-atom/editor-atom
    ch-editor-idle/editor-idle


.. rubric:: Fodnoter

.. [#python-name] Navnet Python kommer af Monty Python
    og skal derfor udtales som python (slægt af slanger) udtales
    på engelsk.

.. [#python-popularity]
    https://stackoverflow.blog/2017/09/06/incredible-growth-python/

.. [#spotify-use-python]
    https://labs.spotify.com/2013/03/20/how-we-use-python-at-spotify/

.. [#instagram-use-python]
    https://www.youtube.com/watch?v=hnpzNAPiC0E

.. [#dropbox-use-python]
    https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/

.. [#python-usage]
    https://www.jetbrains.com/research/python-developers-survey-2018/#types-of-development
