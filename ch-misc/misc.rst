#######
Diverse
#######

Her er en samling af diverse emner som ikke passer andre steder.
Typisk løsningen på små tekniske opgaver 
eller svar på spørgsmål
som er nyttig flere andre steder i bogen.


.. _sec-os-32-bit-64-bit:

**********************************
32-bit eller 64-bit operativsystem
**********************************

Alle programmer, også operativsystemer som Windows, Linux og macOS,
er bygget til at blive afviklet på en bestemt type hardware,

Hardwaren (mest af alt processoren) siges at have en bestemt arkitektur.
Programmer bygget til afvikling på en arkitektur 
kan typisk ikke afvikles på andre arkitekturer.

Personlige computere benyttes sig typisk af én af to arkitekturer:

* x86, også kaldet 32-bit, i386 eller IA-32.
* x86-64, også kaldet 64-bit eller AMD64.

Et operativsystem bygget til x86-64 (64-bit) udgave kan typisk afvikle programmer 
bygget til både x86 (32-bit) og x86-64 (64-bit).
Et operativsystem bygget i x86 udgave (32-bit) kan kun afvikle programmer
bygget til x86 (32-bit).

Programmer som til tilbydes til download fra f.eks. hjemmesider
tilbydes ofte i en udgave til x86/IA-32 (32-bit) og en til x86-64 (64-bit).

Det er derfor vigtigt at kende typen af sin hardware og sit operativsystem 
så man kan downloade den korrekte version af andre programmer.

.. note:: Dette er kun relevant eller en bekymring ved færdigbyggede
    programmer som downloades fra f.eks. hjemmesider.

    Programmer installeret via en *app store* eller *pakke-manager*
    håndtere dette automatisk.
    


Windows 10 
==========
Om en installation af Windows 10 bygget til 32-bit (x86 / i386 / IA-32)
eller 64-bit (x86-64 / AMD64) afgøres på følgende måde:

.. thumbnail:: figs/win10-da-right-click-start.png 
    :width: 49%
    :class: align-right

.. thumbnail:: figs/win10-en-right-click-start.png 
    :width: 49%
    :class: align-right


Højreklik på ``Start``-ikonet og vælg ``System`` (engelsk: ``System``).

.. thumbnail:: figs/win10-da-system-about.png
    :width: 49%
    :class: align-right

.. thumbnail:: figs/win10-en-system-about.png
    :width: 49%
    :class: align-right

Hvis ikke allerede valgt, vælg punktet ``Om`` (engelsk: ``About``)
fra listen i venstre side af vinduet.

Scroll ned til sektionen ``Enhedsspecifikationer`` (engelsk: ``Device specifications``).

Teksten ``64-bit operativsystem`` indikerer at Windows er bygget til 64-bit / x86-64 / AMD64.
Et 64-bit Windows kan afvikle både 32-bit og 64-bit programmer,
download 64-bit udgaven af programmer hvis de er tilgængelige, 
ellers download 32-bit udgaven.

Teksten ``32-bit operativsystem`` indikerer at Windows er bygget til 32-bit / x86 / IA-32.
Et 32-bit Windows kan kun afvikle 32-bit programmer, download derfor 32-bit versioner af programmer.


macOS og  OS X 
==============
Kort fortalt afgør versionen af macOS / OS X om en Mac-computer
kan afvikle 32-bit programmer, 64-bit programmer eller begge dele.

Find versionen af macOS / OS X på følgende måde:

.. thumbnail:: figs/macos-10.14-da-about-this-mac.png
    :width: 49%
    :class: align-right

.. thumbnail:: figs/macos-10.14-en-about-this-mac.png
    :width: 49%
    :class: align-right

Fra skrivebordet klik på ``Apple``-logoet i øverste venstre hjørne
og vælg ``Om denne Mac`` (engelsk: ``About this Mac``).  

Aflæs versionsnummeret, f.eks. ``Version 10.14.2``.

Siden version 10.7 (udgivet i 2011) har alle versioner af macOS / OS X
understøttet både 32-bit og 64-bit programmer [#wiki-macos-history]_.

Fra og med version 10.15 (udkommer i efteråret 2019) 
understøttes kun 64-bit programmer [#macrumor-32bit]_ [#wiki-macos-10.15]_.

Altså, download og installer 64-bit versioner af programmer,
med mindre du benytter Mac OS X 10.6 eller tidligere.


Linux
=====
Mange Linux-distributioner findes i både x86/i386/IA-32 (32-bit)
og x86-64/AMD64 (64-bit) udgave.

Udgaven af en Linux-distribution
(teknisk set typen udgaven af Linux-distributionens kerne)
findes ved at køre kommandoen ``uname -m`` fra en kommandolinje.
Se kapitlet :ref:`sec-cli` hvis du er i tvivl om hvordan dette gøres.

.. code-block:: sh

    $ uname -m
    x86_64

Hvis outputtet er ``x86_64`` er din Linux-distribution 
bygget til x86-64 (64-bit) og du skal downloade 64-bit udgaver af programmer.

Hvis outputtet ikke indeholder ``64``, men indeholder ``86``,
f.eks. ``i386``, ``i686`` eller ``x86``,
er din Linux-distribution bygget til x86/IA-32 (32-bit)
og du skal downloade 32-bit udgaver af programmer.

.. note::
    Dette er irellevant for programmer installeret
    via din pakke-manager (apt, pacman, yum osv.), 
    den installerer automatisk den rigtige version 
    af programmer/pakker.


.. rubric:: Fodnoter

.. [#wiki-macos-history] https://en.wikipedia.org/wiki/MacOS#Release_history
.. [#macrumor-32bit] https://www.macrumors.com/2018/06/05/mojave-last-macos-release-to-support-32-bit-apps/
.. [#wiki-macos-10.15] https://en.wikipedia.org/wiki/MacOS_Catalina

