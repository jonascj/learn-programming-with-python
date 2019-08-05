.. include:: ../global.rst

.. _sec-install-processing:

##########################
Installation af Processing
##########################


*******
Windows
*******
#. 

    Download Processing 32-bit eller 64-bit til Windows fra 
    https://processing.org/download/
    eller brug de direkte link længere nede.
    
    Læs afsnittet :ref:`sec-os-32-bit-64-bit` 
    hvis du er i tvivl om hvilken version du skal vælge.
    
    `Processing Windows 64-bit direkte link. 
    <http://download.processing.org/processing-3.5.3-windows64.zip>`_
    
    `Processing Windows 32-bit direkte link. 
    <http://download.processing.org/processing-3.5.3-windows32.zip>`_
    
    
    Gem filen ved at vælge ``Gem fil`` (engelsk: ``Save File``) i 
    webbrowserens download dialogboks.

    .. thumbnail:: figs/processing-win10-da-save-as.png
        :width: 48%
        :class: align-left
    
    .. thumbnail:: figs/processing-win10-en-save-as.png
        :width: 48%
        :class: align-left

#. 

    Åbn mappen ``Overførsler`` (engelsk: ``Downloads``)  
    i Stifinder (engelsk: Explorer).
    
    Højreklik på den downloadede zip-fil og vælg ``Udpak alle...`` 
    (engelsk: ``Extract All...``)
    
    .. thumbnail:: figs/processing-win10-da-explorer-right-click-zip.png
        :width: 49%
        :class: align-left 
    
    .. thumbnail:: figs/processing-win10-en-explorer-right-click-zip.png
        :width: 49%
        :class: align-left

#. 

    Fjern evt. fluebenet ved valgmuligheden ``[ ] Vis filerne ...``
    (engelsk: ``[ ] Show extracted ...``), 
    for at undgå der åbnes en ny mappe.
    
    Vælg evt. et andet sted til udpakning ved at trykke ``Gennemse``
    (engelsk: ``Browse``),
    ellers pakkes filerne ud i den mappe hvor zip-filen er placeret.
    
    Start udpakningen ved at trykke ``Pak ud`` (engelsk: ``Extract``).
    
    
    .. thumbnail:: figs/processing-win10-da-extract-all.png
        :width: 49%
        :class: align-left 
    
    .. thumbnail:: figs/processing-win10-en-extract-all.png
        :width: 49%
        :class: align-left

#.

    Når udpakningen er færdig vil der være  
    den downloadede fil ``processing-3.5.3-windows32.zip``
    (eller ``processing-3.5.3-windows64.zip``)
    og en mappe med sammen navn, men uden ``.zip``-endelsen.
    
    Åbn mappen.
    
    .. thumbnail:: figs/processing-win10-da-explorer-unpacked-folder1.png
        :width: 49%
        :class: align-left 
    
    .. thumbnail:: figs/processing-win10-en-explorer-unpacked-folder1.png
        :width: 49%
        :class: align-left


#. 
   
    Mappen indeholder en enkelt anden mappe; åbn den.
    
    
    .. thumbnail:: figs/processing-win10-da-explorer-unpacked-folder2.png
        :width: 49%
        :class: align-left 
    
    
    .. thumbnail:: figs/processing-win10-en-explorer-unpacked-folder2.png
        :width: 49%
        :class: align-left


#.

    Processing startes nu ved at dobbeltklikke på filen ``processing.exe``.
    
    
    .. thumbnail:: figs/processing-win10-da-explorer-unpacked-folder3.png
        :width: 49%
        :class: align-left 
    
    
    .. thumbnail:: figs/processing-win10-en-explorer-unpacked-folder3.png
        :width: 49%
        :class: align-left


#.  
    
    Fortsæt med afsnittet :ref:`sec-install-python-mode`.


*****
macOS 
*****
#. 

    Download Processing til macOS / OSX fra
    https://processing.org/download/
    eller brug det direkte link:
    
    `Processing macOS / OSX direkte link. 
    <http://download.processing.org/processing-3.5.3-macosx.zip>`_

    Find filen i Finder, 
    højest sandsynligt under ``Overførsler`` (engelsk: ``Downloads``).
    

    .. thumbnail:: figs/processing-macos-da-finder-unpacked.png
        :width: 48%
        :class: align-left
    
    .. thumbnail:: figs/processing-macos-en-finder-unpacked.png
        :width: 48%
        :class: align-left


#.

    Afhængigt af din browser og opsætning
    vil du enten finde en zip-fil som skal pakkes ud
    eller en app-mappe: 

    * ``processing-3.5.3-macosx.zip`` (evt. uden ``.zip``-endelsen)

      #. Dobbeltklik på zip-filen for at pakke den ud.

      #. Dobbeltklik på den resulterende ``Processing.app``-mappe
         (evt. uden ``.app``-endelsen) for at starte programmet.


    * ``Processing.app`` (evt. uden ``.app``-endelsen)

      #. Dobbeltklik på den allerede udpakkede ``Processing.app``-mappe
         (evt. uden ``.app``-endelsen) for at starte programmet.

#.

    Da programmet Processing er downloadet fra en hjemmeside
    og ikke installeret via App Store,
    spørger macOS højest sandsynligt om du er sikker på
    du vil starte programmet. 

    Vælg at åbne programmet ved at klikke ``[Åbn]`` (engelsk: ``[Open]``)
    i dialogboksen.

#.  
    
    Fortsæt med afsnittet :ref:`sec-install-python-mode`.

*****
Linux
*****
#. 

    Download Processing 32-bit eller 64-bit til Linux fra 
    https://processing.org/download/
    eller brug de direkte link længere nede.
    
    Læs afsnittet :ref:`sec-os-32-bit-64-bit` 
    hvis du er i tvivl om hvilken version du skal vælge.
    
    `Processing Linux 64-bit direkte link. 
    <http://download.processing.org/processing-3.5.3-linux64.tgz>`_
    
    `Processing Linux 32-bit direkte link. 
    <http://download.processing.org/processing-3.5.3-linux32.tgz>`_


#.

    Åbn en kommandolinje og skift mappe til mappen
    hvor din downloadede fil befinder sig.

    Se kapitlet :ref:`sec-cli` hvis du er i tvivl om hvordan dette gøres.

    .. code-block:: sh
    
        $ cd ~/Downloads 

#. 

   Udpak den downloadede fil med en af følgende kommando:

   .. code-block:: sh
   
       $ tar zxvf processing-3.5.3-linux32.tgz

   .. code-block:: sh
   
       $ tar zxvf processing-3.5.3-linux64.tgz

#.

    Skift mappe til den nyudpakkede mappe og start programmet:

    .. code-block:: sh
    
        $ cd processing-3.5.3
        $ ./processing

#.  
    
    Fortsæt med afsnittet :ref:`sec-install-python-mode`.



.. _sec-install-python-mode:

#####################
Installer Python Mode
#####################
Processing er egentlig designet til at skrive Java-kode.
For at kunne skrive Python-kode
skal ``Python Mode`` installeres i Processing.


.. note::
    Skærmbillederne viser Processing i Windows 10,
    men eneste forskel mellem Windows, Linux og macOS
    er dekorationen af vinduerne
    (udseende af kanter, skygger og knapper til
    at lukke, minimere og maksimere vinduer).
    

#. 

    Første gang du åbner Processing 
    vises en velkomstbesked.  
   
    Fjern fluebenet ved ``Show this message on startup`` og luk vinduet.

    .. thumbnail:: figs/processing-win10-en-startup-dialog.png
         :width: 60%

    

#.

    Klik knappen ``Java`` i øverste højre hjørne.
    Vælg menupunktet ``Add Mode ...``.

    .. thumbnail:: figs/processing-win10-en-add-mode1.png
          :width: 80%


#.

    Vælg punktet ``Python Mode for Processing 3``. 
    Klik ``Install``.

    .. thumbnail:: figs/processing-win10-en-add-mode2.png
        :width: 80%
    
#.

    Vent på Processing downloader og installerer Python Mode.

    .. thumbnail:: figs/processing-win10-en-add-mode3.png
        :width: 80%
    
#.      

    Installationen er færdig når der vises et grønt ikon med hvidt flueben
    ud for *Python Mode for PRocessing3*. Luk vinduet.
    
    Kan du ikke se ikonet kan du prøve at skifte faneblad
    ved at klikke på fanen ``Libraries`` og tilbage på fanen ``Modes``.    

    .. thumbnail:: figs/processing-win10-en-add-mode4.png
        :width: 80%

#.     
    
    Skift til Python Mode ved at klikke på knappen ``Java``
    i øvereste højre hjørne.

    Vælg ``Python`` fra menuen. Programmet lukker og åbner igen
    når du skifter mode.

    .. thumbnail:: figs/processing-win10-en-change-mode.png
        :width: 80%


#. 

   Du er nu klar til at fortsætte til afsnittet 
   :ref:`sec-first-program-processing`.
