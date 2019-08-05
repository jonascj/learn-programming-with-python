.. include:: ../global.rst

.. _sec-first-program-first-error:

####################################
Første Python-program og første fejl
####################################

Der er flere forskellige måder at skrive og afvikle
et Python-program på.

Afsnittet her viser ...

Endnu flere måder gennemgåes senere i afsnit ...

.. _sec-first-program-idle:

***********************
Første program med IDLE
***********************

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
        omkring hvordan operativsystemer organisere mapper og filer.

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

********************
Første fejl med IDLE
********************
En stor del af at lære at programmere, 
og programmere når du har lært det,
er at lave fejl.

Det er derfor vigtigt at vide hvordan man retter fejl i et program.
Her ser vi på to kategorier af fejl og hvordan de ser ud i IDLE;
syntaks fejl og alle andre fejl.

Alle andre fejl
===============
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


Visning af linjenumre
=====================

#.  Da programmet kun består af to linjer er det ikke noget problem
    at finde linjen som fejlenmeddelelsen omtaler,
    men havde programmet nu været flere hundrede linjer langt
    kunne det godt være svært hurtigt at identificere linje 134.
    Det problem løses ved at slå visning af linjenumre i editoren til.

    .. note:: 
        Dette kræver Python 3.8.0b3 (beta 3 af 3.8.0) eller
        muligvis version 3.7.5 når den udkommer.

        I tidligere udgaver af IDLE vises linjenummeret 
        kun for den linje cursoren står på
        som ``Ln: x`` i nederste højre hjørne af editoren.
         
    Åbn IDLEs indstillinger ved at vælge menuen 
    ``[Options]`` > ``Configure IDLE`` (Windows og Linux)
    eller med genvejen ``[⌘]``\ +\ ``,`` (macOS).

    Vælg herefter fanebladet ``[General]``,
    og sæt flueben ved valgmuligheden ``Show line numbers in new windows [ ]``,
    tryk ``[Apply]`` og afslut med ``[Ok]``.

    .. image:: figs/idle-windows-settings-line-numbers.png
        :align: center
        :scale: 100%

    Indstillingen gælder kun for nye vinduer. 
    Luk derfor din fil og åbn den igen.
    Genvejen ``[ctrl]``\ +\ ``O`` (Windows og Linux)
    eller ``[⌘]``\ +\ ``[O]`` (macOS)
    åbner åbn-fil-dialogen (det er 'o' som i 'open').

    Editorvinduet ser nu således ud, med linjenumre i venstre side.

    .. image:: figs/idle-windows-file-window-with-line-numbers.png
        :align: center
        :scale: 100%
    

Syntaksfejl
===========

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

    Fordi vi har slettet slutparentesen i linje 1,
    er det let at tænke fejlen findes i linje 1,
    men Python/IDLE meddeler fremhæver linje 2.

    Hvis linje 2 havde set ud som her
    ville linje 1 være gyldig:

     .. code-block:: py
        :linenos:
        :emphasize-lines: 2 

        print("Python"
              " rocks!")


    Da Python-fortolkeren læser linje 1 før linje 2
    bliver `print` i linje 2 fremhævet som stedet fejlen er,
    men vi som programmører vil måske sige vi lavede fejlen i linje 1.

 
    

.. _sec-first-program-atom:

***********************
Første program med Atom
***********************





