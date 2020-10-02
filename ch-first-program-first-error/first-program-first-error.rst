.. include:: ../global.rst

.. _sec-first-program-first-error:

####################################
Første Python-program og første fejl
####################################

Nu hvor du har installeret en Python-fortolker,
som kan forstå de programmer du skriver,
og en teksteditor så du kan skrive programmer,
er du klar til at skrive dit første program.

Vælg om du vil skrive dit :ref:`sec-first-program-idle`
eller om du vil skrive dit :ref:`sec-first-program-atom`.

Er du i tvivl så kan du vælge IDLE, 
det er det simpleste af de to udviklingsmiljøer.

****
IDLE
****

.. _sec-first-program-idle:

Første program med IDLE
=======================

#.  Åbn programmet IDLE,
    det blev installeret sammen med Python-fortolkeren 
    i :ref:`sec-install-python`.

    Dette vindue kaldes **shell-vinduet**.
    
    .. image:: figs/idle-windows-shell-window.png
        :align: center
        :scale: 100%

#.  Brug genvejen ``[ctrl]``\ +\ ``[n]`` (Windows og Linux)
    eller ``[⌘]``\ +\ ``n`` (macOS) til at åbne en ny fil.
    
    Et nyt vindue åbner med en tom tekstfil.
    Dette vindue kaldes **editorvinduet**.
    Her skriver du følgende to linjers kode,
    dit første Python-program:
    
    .. code-block:: py
        :linenos:

        print("Python")
        print(2+2)

    .. image:: figs/idle-windows-file-window-unsaved.png
        :align: center
        :scale: 100%

#.  Gem filen ved at trykke ``[ctrl]``\ +\ ``S`` (Windows og Linux)
    eller ``[⌘]``\ +\ ``[S]`` (macOS).

    .. note::
        Det er vigtigt at have markeret editorvinduet (med koden)
        når man bruger genvejen (eller menuerne for den sags skyld)
        til at gemme sin fil.

        Hvis man har markeret det andet vindue (Python 3.x Shell)
        så gemmer den teksten fra det vindue i stedet for.

    Gem filen et fornuftigt sted, lav f.eks. en mappe kaldet ``programmering``
    og gem filen under den mappe med navnet ``my_first_program.py``.

    Brug mappe- og filnavne uden mellemrum.
    Hvis navnet består af mange ord kan de adskilles af underscores ``_``.

    .. seealso::
        :ref:`sec-os-filesystem-hierarchy` for mere information
        omkring hvordan operativsystemer organiserer mapper og filer,
        og hvordan du bedst organiserer dine Python-filer.
        

    Når filen er gemt vises filens navn og sti i toppen af vinduet.

    .. image:: figs/idle-windows-file-window-saved.png
        :align: center
        :scale: 100%

    
#.  Brug nu genvejen ``[F5]`` mens editorvinduet er markeret
    (eller bruge menuen ``[Run]`` > ``[Run Module]``)
    til at udføre/afvikle/køre programmet.

    Outputtet af programmet (tekst) vises i shellvinduet.

    I den røde markering står hvilket program (hvilken fil) 
    som afvikles/udføres/køres og bagefter står outputtet,
    i dette tilfælde en linje med teksten ``Python``
    og en linje med teksten ``4``.

    Hvis du ikke ser noget output,
    et output i rød tekst med ordet ``error`` i blandt
    eller en popup med teksten ``invalid syntax``
    så er du allerede et afsnit foran.
    Spring til næste afsnitt :ref:`sec-first-error-idle`
    for at forsøge at rette den fejl du har fået lavet.

    .. image:: figs/idle-windows-shell-window-output.png
        :align: center
        :scale: 100%


.. _sec-first-error-idle:

Første fejl med IDLE
====================

En stor del af at lære at programmere er at lave fejl,
skrive kode som ikke virker.
Det er i øvrigt også en stor del af at programmere 
selv når du på et tidspunkt har fået mange års erfaring.

Det er derfor vigtigt at vide hvordan man retter fejl i et program.
Her ser vi på to kategorier af fejl og hvordan de ser ud i IDLE;
syntaks fejl og alle andre fejl.

Alle andre fejl
---------------
#.  Ændre dit første program ``my_first_program.py``, eller endnu bedre,
    opret en kopi af det som heddder ``my_first_error.py``
    og ændre i det, så det ser således ud
    (slet et ``t`` fra ``print`` linje 1):

     .. code-block:: py
        :linenos:
        :emphasize-lines: 1

        prin("Python")
        print(2+2)

#.  Gem programmet og udfør det vha. ``[F5]``.
    Denne gang kommer der et rødt output som indikerer en fejl.
 
    .. image:: figs/idle-windows-name-error.png
        :align: center
        :scale: 100%

#.  Der er to interessante stykker information i fejlmeddelelsen:

    ``File "... my_first_program.py", line 1``
    fortæller i hvilken fil og på hvilken linje en fejl blev opdaget.
   
    
    ``NameError: name 'prin' is not defined``
    fortæller, at koden indeholder et navn, eller ord, ``prin``
    som Python-fortolkeren ikke forstår.

    Tilsammen kan de to stykker information lede os frem til,
    at der mangler et ``t`` i linje 1 således der står ``print``
    i stedet for ``prin``.


   

Syntaksfejl
-----------

#.  Ændre dit første program ``my_first_program.py``, eller endnu bedre,
    opret en kopi af det som heddder ``my_first_syntax_error.py``
    og ændre i det, så det ser således ud
    (slet sidste parentes i linje 1):

     .. code-block:: py
        :linenos:
        :emphasize-lines: 1

        print("Python"
        print(2+2)

#.  Gem programmet og udfør det vha. ``[F5]``.
    Denne gang kommer der ikke noget output i shellvinduet,
    der kommer derimod en popup med teksten ``invalid syntax``
    og linje 2 bliver markeret med rød overstregning:

    .. image:: figs/idle-windows-syntax-error.png
        :align: center
        :scale: 100%

    Syntaksfejl kan være sværere at rette fordi fejlen
    ofte indikere en anden linje end der hvor vi som programmører
    har skrevet noget andet end vi tænkte eller glemt noget. 
    
    Det er en smule teknisk at forstå hvorfor fortolkeren
    siger der er fejl i linje 2 og ikke linje 1 hvor vi slettede parentesen.

    Den korte forklaring er, at linje 1 i visse tilfælde er gyldig Python-kode
    og derfor vælger fortolkeren at sige det er linje 2 som indeholder fejlen.

    Hvis programmets linje 2 havde set ud som nedenfor, 
    ville linje 1 være gyldig.

    .. code-block:: py
        :linenos:
        :emphasize-lines: 2 

        print("Python"
              " rocks!)

    Fortolkeren kan altså ikke vide om vi glemte at skrive ``)`` i linje 1
    eller kom til at skrive ``print(2+2)`` 
    i stedet for f.eks. `` rocks!)`` i linje 2.

    .. important::
        Ved ``SyntaxError`` er kan programmørens fejl/forglemmelse
        sagtens findes på en af linjerne før den linje som fejlen angiver.
        Tjek derfor altid linjerne over der hvor fejlen meldes.

 
Indstilling af IDLE 
===================
Følgende indstillinger kan med fordel foretages eller overvejes
inden du går videre med bogen:

:ref:`sec-editor-idle-linenumbers`

****
Atom
****

.. _sec-first-program-atom:

Første program med Atom
=======================

#.  Åbn programmet *Atom* 
    som blev installeret i :ref:`sec-install-atom`.

    Åbn en ny tom fil med genvejen ``[ctrl]``\ +\ ``[N]`` (Windows og Linux)
    eller ``[⌘]``\ +\ ``[n]`` (macOS).

    Skriv følgende to linjers kode i det tomme vindue, 
    dit første Python-program:

    .. code-block:: py

        print("Python")
        print("2+2")


    .. image:: figs/atom-untitled-program-ubuntu1804.png
        :align: center
        :width: 100%


#.  Gem filen ved at trykke ``[ctrl]``\ +\ ``S`` (Windows og Linux)
    eller ``[⌘]``\ +\ ``[S]`` (macOS).

    Gem filen et fornuftigt sted, lav f.eks. en mappe kaldet ``programmering``
    og gem filen under den mappe med navnet ``my_first_program.py``.

    Brug mappe- og filnavne uden mellemrum.
    Hvis navnet består af mange ord kan de adskilles af underscores ``_``.

    .. seealso::
        :ref:`sec-os-filesystem-hierarchy` for mere information
        omkring hvordan operativsystemer organiserer mapper og filer,
        og hvordan du bedst organiserer dine Python-filer.

    .. image:: figs/atom-saved-program-ubuntu1804.png
        :align: center
        :width: 100%

    Når filen er gemt ændrer Atom-vinduet udseende. 
    Navnet på din fil står i filens faneblad
    og der åbner et nyt panel *Project*
    som viser filer i den mappe hvor din fil er gemt.
    
    Nu hvor filen har fået en navn med endelsen `.py` genkender
    Atom filen som en Python-fil og highlighter (farver) koden
    så den er lettere at læse.

#.  Nu er der to måder at afvikle/køre/udføre Python-programmet
    du har skrevet. 

    1.  Vha. *script*-pakken: 
        Tryk ``[ctrl]``\ +\ ``[shift]``\ +\ ``[b]`` (Windows og Linux)
        eller ``[⌘]``\ +\ ``[i]`` (macOS)

         .. thumbnail:: figs/atom-script-success-ubuntu1804.png
             :width: 70%
             :align: center

        Programmets output vises i et nyt panel i bunden af vinduet,
        i dette filfælde tekste ``Python`` og teksten ``4``
        på hver sin linje.

        Hvis du ikke ser noget output eller output med
        ord som ``Traceback`` og ``Error`` så er der højest sandsynligt
        en fejl i dit program.
        Gå til :ref:`sec-first-error-atom`.

        .. note::

            Hvis du ændrer filen skal du gemme ændringerne før du
            afvikler/kører/udfører programmet igen via *script*-pakken.

    2.  Vha. *atom-python-run*-pakken: Tryk ``[F5]``.

        .. thumbnail:: figs/atom-python-run-success-ubuntu1804.png
            :width: 70%
            :align: center
        
        Et nyt vindue åbnes og viser outputtet af programmet.
        I dette tilfælde teksten ``Python`` og teksten ``4``
        på hver sin linje.
        
        Vinduet kan lukkes ved at trykke ``[Enter]``
        eller ved at lukke vinduet som alle andre vinduer
        i dit operativsystem 
        (typisk noget med at trykke på et kryds i hjørnet af vinduet).
 
        Hvis du ikke ser noget output eller output med
        ord som ``Traceback`` og ``Error`` så er der højest sandsynligt
        en fejl i dit program.
        Gå til :ref:`sec-first-error-atom`.


.. _sec-first-error-atom:

Første fejl med Atom
====================

En stor del af at lære at programmere er at lave fejl,
skrive kode som ikke virker.
Det er i øvrigt også en stor del af at programmere 
selv når du på et tidspunkt har fået mange års erfaring.

Det er derfor vigtigt at vide hvordan man retter fejl i et program.
Her ser vi på hvordan Python-fejl rapporteres i Atom
med de to pakker *script* og *atom-python-run*.

#.  Ret dit første program ``my_first_program.py``, eller endnu bedre,
    opret en kopi af det som heddder ``my_first_error.py``
    og ret i det, så det ser således ud
    (slet et ``t`` fra ``print`` linje 1):

     .. code-block:: py
        :linenos:
        :emphasize-lines: 1

        prin("Python")
        print(2+2)

#.  Kør programmet via *script*- eller *atom-python-run*-pakken
    som beskrevet i :ref:`sec-first-program-atom`.
    
    Fejlmeddelelsen vises samme sted som programmets output.

    .. code-block:: text 
        :linenos:

        Traceback (most recent call last):
          File "{path}/my_first_program.py", line 1, in <module>
            prin("Python")
        NameError: name 'prin' is not defined

    
    .. thumbnail:: figs/atom-python-run-name-error-ubuntu1804.png
       :width: 49%
       :class: align-left
    
    .. thumbnail:: figs/atom-script-name-error-ubuntu1804.png
       :width: 49%
       :class: align-left

    Fejlmeddelelsen indeholder to vigtige stykker information:

    *   Linje 2 fortæller hvilken fil og på hvilken linje fejlen befinder sig
        (my_first_program.py, linje 1).
        *Bemærk* ``{path}`` er stien til din fil.
    
    *   Linje 4 fortæller hvilken fejl fortolkeren fandt
        (NameError, ``prin`` er ikke et navn Python kender).
#.  Ret dit første program igen, eller endnu bedre,
    opret en kopi af det som hedder ``my_second_error.py``
    og ret i det, så det ser således ud
    (slet den sidste parentes i linje 1):

     .. code-block:: py
        :linenos:
        :emphasize-lines: 1

        print("Python"
        print(2+2)

#.  Kør programmet via *script*- eller *atom-python-run*-pakken.
   
    Denne gang er fejlmeddelelsen en anden: 

    .. code-block:: text 
        :linenos:

          File {path}/my_first_program.py", line 2
            print(2+2)
                ^
        SyntaxError: invalid syntax

    Fejlen angives til at være i linje 2, 
    der er endda en ``^`` som peger på ``t`` i ``print``.

    Det er en smule teknisk at forstå hvorfor fortolkeren
    siger der er fejl i linje 2 og ikke linje 1 hvor vi slettede parentesen.

    Den korte forklaring er, at linje 1 i visse tilfælde er gyldig Python-kode
    og derfor vælger fortolkeren at sige det er linje 2 som indeholder fejlen.

    Hvis programmets linje 2 havde set ud som nedenfor, 
    ville linje 1 være gyldig.

    .. code-block:: py
        :linenos:
        :emphasize-lines: 2 

        print("Python"
              " rocks!)

    Fortolkeren kan altså ikke vide om vi glemte at skrive ``)`` i linje 1
    eller kom til at skrive ``print(2+2)`` 
    i stedet for f.eks. `` rocks!)`` i linje 2.

    .. important::
        Ved ``SyntaxError`` er kan programmørens fejl/forglemmelse
        sagtens findes på en af linjerne før den linje som fejlen angiver.
        Tjek derfor altid linjerne over der hvor fejlen meldes.

Indstilling af Atom
===================
Følgende indstillinger kan med fordel foretages eller overvejes
inden du går videre med bogen:

:ref:`sec-editor-atom-theme`

