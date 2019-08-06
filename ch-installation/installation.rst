.. include:: ../global.rst

.. _sec-install:

############
Installation
############

For at kunne skrive computerprogrammer i Python
kræves en teksteditor
til at oprette tekstfiler (fyldt med Python-kode).

For at kunne afvikle programmer skrevet i Python 
kræves en såkaldt Python-fortolker.
Fortolkeren er et program som kan læse 
tekstfiler med Python-kode
og udføre de handlinger koden beskriver.

Kombinationen af teksteditor og Python-fortolker,
evt. andre nyttige værktøjer,
kaldes et udviklingsmiljø
eller et *integreret udviklingsmiljø*
(engelsk: Integrated Development Environemnt, IDE)
hvis tilpas mange værktøjer er kombineret i en 
`brugergrænseflade <https://en.wikipedia.org/wiki/Graphical_user_interface>`_.

Her gennemgås installation og opsætning af to forkellige udviklingsmiljøer:

1.  Den officielle Python-fortolker *cPython* og medfølgende
    integeret udviklingsmiljø *IDLE*.

2.  Den oficielle Python-fortolker *cPython* med tredjeparts
    teksteditor/integreret udviklingsmiljø *Atom*.

Begge opsætninger kræver man starter med :ref:`sec-install-python`.

.. seealso::
    :ref:`sec-processing-python-mode` er et komplet integeret udviklingsmiljø
    med fokus på at gøre programmeringsundervisning 
    mere visuel/grafisk/kunstnerisk.

    Du kan evt. erstatte kapitel 
    :ref:`sec-install` og :ref:`sec-first-program-first-error`
    med :ref:`sec-processing-python-mode`.

.. _sec-install-python:

********************************
Installation af Python (og IDLE)
********************************
Python-fortolkeren findes i udgaver til
på både Windows, macOS/OSX og Linux.

Vælg din platform og følg installationsinstruktionerne:

:ref:`sec-install-python-win` 

:ref:`sec-install-python-macos`

:ref:`sec-install-python-linux`

.. note::
    
    Installationsinstruktionerne er skrevet da seneste
    version af Python var 3.7.4.

    Der er dog ingen umiddelbar grund til de ikke skulle gælde
    for fremtidige Python 3.7.5 og 3.8.x.

    Du kan derfor også opleve, at der står ``Python 3.7.3``
    i et screenshot, men teksten og din skærm viser et andet versionsnummer. 


.. _sec-install-python-win:

Windows
=======

#.  Download Python 3.7.3:
    `Windows x86-64 executable installer <https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe>`_


#.  Åbn/kør installationsprogrammet ``python-3.7.3-amd64.exe``.

    .. important::
    
        Sæt flueben ved valgmuligheden ``[ ] Add Python 3.7 to PATH``.
    
    Tryk ``Install Now`` for at starte installationen.

    .. image:: figs/install-python-windows-1.png
        :align: center
        :scale: 100%

#.  Hvis Windows kommer med en UAC-dialog som denne vælges ``Yes`` eller ``Ja``.

    .. image:: figs/install-python-windows-2.png
        :align: center
        :scale: 100%
    
#.  Installationsprogrammet intallerer nu Python-fortolkeren og andre hjælpeprogrammer.

    .. image:: figs/install-python-windows-3.png
        :align: center
        :scale: 100%
    
#.  Klik ``Close`` for at afslutte installationen.
    
    .. image:: figs/install-python-windows-4.png
        :align: center
        :scale: 100%

#.  Nu skal du vælge, om du vil gå igang med at skrive dit første
    program vha. IDLE-udviklingsmiljøet (som følger med cPython):
    :ref:`sec-first-program-idle`.

    Eller om du vil installere og opsætte Atom udviklingsmiljøet:
    :ref:`sec-install-atom`.

    Du kommer hurtigst i gang med at skrive Python-kode
    ved at gå til :ref:`sec-first-program-idle`.
    Til gengæld vil du på et senere tidspunkt formodentligt ønske
    at vende tilbage til afsnittet :ref:`sec-install-atom`.

   


.. _sec-install-python-macos:

macOS og OS X
=============

#.  Download Python 3.7.4:
    `macOS 64-bit installer (10.9+) <https://www.python.org/ftp/python/3.7.4/python-3.7.4-macosx10.9.pkg>`_


#.  Åbn/kør installationsprogrammet ved at dobbeltklikke på ``python-3.7.4-macosx10.9.pkg``.
    Klik ``[Continue]`` for at komme videre med installationen.

    .. thumbnail:: figs/install-python-macos-1.png
        :width: 100%

#.  Klik ``[Continue]`` for at komme videre med installationen.

    .. thumbnail:: figs/install-python-macos-2.png
        :width: 100%
    
#.  Klik ``[Continue]`` for at komme videre med installationen.

    .. thumbnail:: figs/install-python-macos-3.png
        :width: 100%
    
#.  Klik ``[Agree]`` for at komme videre med installationen.

    .. thumbnail:: figs/install-python-macos-4.png
        :width: 100%
    
#.  Klik ``[Install]`` for at starte selve installationen.  

    .. thumbnail:: figs/install-python-macos-5.png
        :width: 100%
    
#.  Måske beder macOS dig indtaste brugernav og password
    for at sikre sig du har ret til at installere programmer på computeren.
    Indtast det brugernavn og password du benytter til login ved opstart
    og klik ``[Install Software]``.

    .. thumbnail:: figs/install-python-macos-6.png
        :width: 100%
    
#.  Vent på installationsprocessen bliver færdig.  

    .. thumbnail:: figs/install-python-macos-7.png
        :width: 100%
    
#.  Afslut installationen ved at klikke ``[Close]``.

    .. thumbnail:: figs/install-python-macos-8.png
        :width: 100%
    
#.  macOS foreslår dig at slette selve installationsfilen,
    dette kan du gøre ved at vælge ``[Move to Trash]``.

    .. thumbnail:: figs/install-python-macos-9.png
        :width: 100%

#.  Nu skal du vælge, om du vil gå igang med at skrive dit første
    program vha. IDLE-udviklingsmiljøet (som følger med cPython):
    :ref:`sec-first-program-idle`.

    Eller om du vil installere og opsætte Atom udviklingsmiljøet:
    :ref:`sec-install-atom`.

    Du kommer hurtigst i gang med at skrive Python-kode
    ved at gå til :ref:`sec-first-program-idle`.
    Til gengæld vil du på et senere tidspunkt formodentligt ønske
    at vende tilbage til afsnittet :ref:`sec-install-atom`.



.. _sec-install-python-linux:

Linux
=====

.. note::
    Linux afsnittet antager et vist kendskab til brug af kommandolinjen,
    se evt. afsnittet :ref:`sec-cli`.



Der findes så mange forskellige distributioner (udgaver) af Linux,
i så mange forskellige versioner, at installation af Python
under Linux må gennemgås generelt og for udvalgte distributioner. 

Generelt
--------

Generelt kommer de fleste Linux distributioner (fra 2016 og frem) 
med Python 3.5 eller nyere præinstalleret. 

Start med at undersøge hvilken version af Python du benytter
med følgende kommando (fra en kommandolinje). 
Outputtet viser Python-fortolkerens vesionsnummer.

.. code-block:: sh

    $ python -V
    Python 3.6.5

Hvis din shell fortæller dig, at du kommandoen ``python`` ikke findes
(``command not found: python`` eller lign.),
eller hvis den rapporterede version er ``2.x.y`` 
kan du prøve kommandoen ``python3 -V`` i stedet for:

.. code-block:: sh

    $ python3 -V
    Python 3.7.4

Bogen her antager generelt du benytter verion 3.5 eller nyere,
så hvis du har version 3.5.x, 3.6.x eller 3.7.x kan du gennemgå 
det meste af bogen uden at opgradere.

Dog kommer de fleste Linux distributioner 
desværre **ikke** med IDLE installeret.
Du kan forsøge at starte IDLE med kommandoen ``idle`` eller ``idle3``
eller ved søge efter programmet ``idle`` via din grafiske brugerflade.

Hvis IDLE ikke er installeret kan du enten forsøge at installere
den via din distributions pakke-manager. eller gå videre 
til :ref:`sec-install-atom` og benytte Atom i stedet for IDLE.


Ubuntu
------
Ubuntu 16.04 indeholder Python 3.5.1, Ubuntu 18.04 Python 3.6.7,
og Ubuntu 19.04 Python 3.7.3 (som kommandoen ``python3``).

Ubuntu indeholder dog ikke teksteditoren/udviklingsmiljøet IDLE.
Det kan installeres med følgende kommando:

.. code-block:: sh

    $ sudo apt install idle3
    <output skipped>
    Do you want to continue? [Y/n] y
    <output skipped>

Ubuntu indeholder heller ikke et grafikbibliotek kaldet *tkinter*
som bruges af Python til forskellige grafiske opgaver.
Det kan installeres med følgende kommando:

.. code-block:: sh

    $ sudo apt install python3-tk
    <output skipped>
    Do you want to continue? [Y/n] y
    <output skipped>




I Ubuntu 16.04 og 18.04 kan du installere nyere Python versioner på følgende:

#. Tilføj en såkaldt såkaldt *Personal Package Archive* (PPA).
   Tryk ``[Enter]`` når du bliver spurgt om du vil
   fortsætte eller ej.

    .. code-block:: sh

        $ sudo apt update
        $ sudo add-apt-repository ppa:deadsnakes/ppa
        <output skipped>
        press [ENTER] to continue or Ctrl-c to cancel adding it.
        <output skipped>

#. Opdater Ubuntus pakkeliste:

    .. code-block:: sh

        $ sudo apt update
        <output skipped>

#. Installer f.eks. Python 3.7 med følgende kommando.
   Tryk ``y`` (for yes) efterfulgt af ``[Enter]``
   når du bliver spurgt om du vil fortsætte.
   
    .. code-block:: sh

        $ sudo apt install python3.7
        <output skipped>
        Do you want to continue? [Y/n] y
        <output skipped>


    ``sudo apt install python3.8`` vil ligeledes installere Python 3.8
    (pt. betaversion).

#. Installer den tilsvarende version af idle med f.eks.
   ``sudo apt install idle-python3.8``.
 
    


.. _sec-install-atom:

********************
Installation af Atom
********************

Atom er en multi-platform teksteditor
med mulighed for installation af pakker/plugins
til at udvide dens funktionalitet.  
Den egner sig godt til at skrive Python kode.

Vælg din platform og følg installationsinstruktionerne:

:ref:`sec-install-atom-win` 

:ref:`sec-install-atom-macos`

:ref:`sec-install-atom-linux`

.. note::
    
    Installationsinstruktionerne er skrevet da seneste
    version af Atom var 1.39.1. 

    Der er dog ingen umiddelbar grund til de ikke skulle gælde
    for fremtidige Atom versioner (1.40.0 osv.) 

    Du kan derfor også opleve, at der står ``Atom 1.39.1``
    på et screenshot, men teksten og din skærm viser et andet vesionsnummer.

.. _sec-install-atom-win:

Windows
=======


#.  Download nyeste Atom installationsprogram fra https://atom.io
    (siden burde gerne forslå den korrekte version for Windows)

    `Atom 1.39.1 Windows 64-bit direkte link <https://github.com/atom/atom/releases/download/v1.39.1/AtomSetup-x64.exe>`_

    `Atom 1.39.1 Windows 32-bit direkte link <https://github.com/atom/atom/releases/download/v1.39.1/AtomSetup.exe>`_

    Se afsnittet :ref:`sec-os-32-bit-64-bit`
    hvis du er i tvivl om du skal vælge 32-bit eller 64-bit udgaven.

#.  Dobbeltklik på den downloadede installationsfil 
    (``AtomSetup-x64.exe`` eller ``AtomSetup.exe``)
    for at starte installationen.
    
    Der er ingen mulighed for at tilpasse installationen,
    den går bare direkte i gang.

    .. thumbnail:: figs/atom-win10-install.png
        :width: 60%
        :align: center

#.  Atom automatisk når installationen er udført.
    
    Gå videre til afsnittet :ref:`sec-install-atom-packages`
    for at få installeret udvidelsespakker til Atom.


.. _sec-install-atom-macos:

macOS og OS X
=============

#.  Download nyeste Atom installationsprogram fra https://atom.io
    (siden burde gerne forslå den korrekte version for Windows)

    `Atom 1.39.1 macOS direkte link <https://github.com/atom/atom/releases/download/v1.39.1/atom-mac.zip>`_

    Find filen i Finder, 
    højest sandsynligt under ``Overførsler`` (engelsk: ``Downloads``).

#.  Afhængigt af din browser og opsætning
    vil du enten finde en zip-fil som skal pakkes ud
    eller en app-mappe: 

    * ``atom-mac.zip`` (evt. uden ``.zip``-endelsen)

      #. Dobbeltklik på zip-filen for at pakke den ud.

      #. Dobbeltklik på den resulterende ``Atom.app``-mappe
         (evt. uden ``.app``-endelsen) for at starte programmet.


    * ``Atom.app`` (evt. uden ``.app``-endelsen)

      #. Dobbeltklik på den allerede udpakkede ``atom.app``-mappe
         (evt. uden ``.app``-endelsen) for at starte programmet.


    .. thumbnail:: figs/atom-macos-da-install.png
        :width: 48%
        :class: align-left
    
    .. thumbnail:: figs/atom-macos-en-install.png
        :width: 48%
        :class: align-left


#.

    Da programmet Atom er downloadet fra en hjemmeside
    og ikke installeret via App Store,
    spørger macOS højest sandsynligt om du er sikker på
    du vil starte programmet. 

    Vælg at åbne programmet ved at klikke ``[Åbn]`` (engelsk: ``[Open]``)
    i dialogboksen.

#.  Gå videre til afsnittet :ref:`sec-install-atom-packages`
    for at få installeret udvidelsespakker til Atom.


.. _sec-install-atom-linux:

Linux
=====

.. note::
    Linux afsnittet antager et vist kendskab til brug af kommandolinjen,
    se evt. afsnittet :ref:`sec-cli`.

Der flere måder at installere Atom på i Linux. 

#.  Følg Atoms egen installationsvejledning
    til brug af din Linux distributions pakkemanager:
    `Installing Atom on Linux <https://flight-manual.atom.io/getting-started/sections/installing-atom/#installing-atom-on-linux>`_

#.  Download 
    `atom-amd64.tar.gz 1.39.1 (64-bit) <https://github.com/atom/atom/releases/download/v1.39.1/atom-amd64.tar.gz>`_

    Udpak arkivet og kør programmet ``atom`` fra den udpakkede mappe:

    .. code-block:: sh

        $ tar zxvf atom-amd64.tar.gz
        $ cd atom-amd64/
        $ cd atom-1.39.1-amd64
        $ ./atom
        
    Denne metode er også dokumenteret i Atoms egen installationsvejledning her:
    `Installing Atom - Portable Mode <https://flight-manual.atom.io/getting-started/sections/installing-atom/#portable-mode>`_

Gå videre til afsnittet :ref:`sec-install-atom-packages`
for at få installeret udvidelsespakker til Atom.

.. _sec-install-atom-packages:

Pakker til Atom
===============

Atom er som udgangspunkt en simpel teksteditor
og dens avancerede funktionalitet kommer fra
(udvidelses)pakker.

Atom kommer med en enkelt Python-relateret pakke prænstalleret,
(``language-python`` som giver Python 
`syntax highlighting <https://en.wikipedia.org/wiki/Syntax_highlighting>`_),dd
men der skal installeres nogle flere pakker for at få Atom
til bedre at understøtte Python-programmering.

.. note::
    Skærmbillederne viser Atom 1.39.1 i Ubuntu 18.04,
    men eneste forskel mellem Windows, Linux og macOS
    er dekorationen af vinduerne
    (udseende af kanter, skygger og knapper til
    at lukke, minimere og maksimere vinduer).
    

#.  Første gang du åbner Atom vises forskellige velkomstindhold.
   
    Fjern fluebenet ved ``Show Welcome Guide when opening Atom``
    og luk fanebladene ``[Welcome]`` og ``[Welcome Guide]``.

    .. thumbnail:: figs/atom-first-start-ubuntu1804.png
         :width: 80%
         :align: center

#.  Fanebladet ``[Telemetry Consent]`` er nu åben.
    Her beder Atom om lov til at indsamle anonyme data 
    omkring din brug af Atom. 
    
    Vælg hvorvidt du ønsker at bidrage til Atom
    ved at dele dine brugsdata.
    Du kan læse her hvilke data der indsamles: 
    https://atom.io/packages/metrics.

    Fanebladet lukker når du har foretaget en valg.
    Du kan altid ændre det senere.

    .. thumbnail:: figs/atom-first-start-telemetry-ubuntu1804.png
         :width: 80%
         :align: center
 
#.  Brug nu genvejen ``ctrl``\ +\ ``,`` (Windows og Linux) 
    eller ``⌘``\ +\ ``,`` (macOS) 
    til at åbne Atoms ``Settings`` (indstillinger).

    Under ``Settings`` vælges underpunktet ``+ Install`` i venstre side.

    I inputfeltet i toppen af skærmen skrives navnet på den pakke
    der skal søges efter.

    Start med at søge efter ``autocomplete-python`` og tryk på ``[Install]``
    når den er fundet.


    .. thumbnail:: figs/atom-package-install1-ubuntu1804.png
         :width: 80%
         :align: center

#.  ``[Install]]``-knappen blinker mens installationen står på. 

    .. thumbnail:: figs/atom-package-install2-ubuntu1804.png
         :width: 80%
         :align: center
 

#.  Pakken ``autocomplete-python`` åbner, når den er færdiginstalleret,
    et vindue som tilbyder at tilføje en ekstra service
    fra https://kite.com.

    Det anbefales at fravælge denne service ved at trykke ``Dismiss``.
    Kite opsamler som standard en lang række data omkring din kode
    og brug af Atom. Noget af dataopsamlingen kan dog slås fra.
    
    .. thumbnail:: figs/atom-package-install3-ubuntu1804.png
         :width: 80%
         :align: center

#.  Pakken ``autocomplete-python`` er nu færdiginstalleret,
    dette kan ses ved der vises en ``[Settings]``-, ``[Uninstall]``-
    og ``[Disable]``-knap.

    .. thumbnail:: figs/atom-package-install4-ubuntu1804.png
         :width: 80%
         :align: center

#.  Installer på samme følgende pakker:

    * ``atom-python-run``
    
    * ``script`` 


#.  Når du har installeret alle pakkerne 
    (``autocomplete-python``, ``atom-python-run`` og ``script``)
    bør de vises under ``Settings`` > ``Packages``.

    Det er her du kan ændre pakkernes indstillinger,
    hvis du skulle få brug for det.

    .. thumbnail:: figs/atom-package-install5-ubuntu1804.png
         :width: 80%
         :align: center


#.  Du er nu klar til at gå til afsnittet :ref:`sec-first-program-atom`.


