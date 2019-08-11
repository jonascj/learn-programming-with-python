.. include:: ../global.rst

.. _sec-os-show-filename-extensions:

########################
Vis endelser på filnavne
########################

Filnavne slutter ofte med en endelse ``.<ext>``,
hvor ``<ext>`` typisk er 1-5 bogstaver og tal:

* ``script.py``
* ``cat.gif``
* ``specs.pdf``
* ``everlong.mp3``
* ``data.xls``

Operativsystemer bruger endelsen af filnavnet til at afgøre
hvilket program der skal startes hvis brugeren 
f.eks. dobbeltklikker på filen i en grafisk filbrowser.

En fil kan dog sagtens have et navn uden endelsen ``.<ext>``,
f.eks. ``data`` eller ``script``.
Et filnavn kan også sagtens starte med punktum, f.eks. ``.cat.gif``.

Windows og macOS skjuler som standard endelsen på filnavnet
for udvalgte eller alle filnavne. 
Linux kommer i så mange udgaver det er svært at udtale sig om,
men Linux viser generelt de fulde filnavne.

Du kan ændre indstillinger for visning af filnavnendelser på følgende måde:

.. admonition:: Prøv selv

    Ændre indstillinger for visning af endelser på filnavne.

    Erstat ``.pdf`` filendelsen på et PDF-dokument med ``.txt``,
    f.eks. ``document.pdf`` til ``document.txt``
    (højreklik på filen i en grafisk filbrowser, vælg ``Omdøb``
    (engelsk: ``Rename``)).

    Hvis du nu dobbeltklikker på PDF-dokumentet (med ``.txt`` endelse)
    vil det ikke åbne i din sædvanlige PDF-viser, 
    i et simpel teksteditor som ikke kan finde ud af at vise en PDF-fil. 

    Der er dog intet galt med PDF-filen. Den kan fint åbnes manuelt
    i en PDFviser (via træk-og-slip/drag-and-drop eller programmets
    åbn-dialog).
    

*******
Windows
*******

Tryk start-ikonet eller  ``[win]``-tasten,
skriv ``indstillinger for stifinder`` (engelsk: ``file explorer options``),
og vælg ``Instillinger for Stifinder`` (engelsk: ``File Explorer Options``).

Åbn fanebladet ``Vis`` (engelsk: ``View``), og sæt flueben ved indstillingen 
``Skjul filtypenavne for kendte filtyper``
(engelsk: ``Hide extensions for known file types``).

Afslut ved at trykke ``[Anvend]`` og ``[OK]``.

.. thumbnail:: figs/windows-da-show-filename-extensions.png
    :width: 49%
    :class: align-left

.. thumbnail:: figs/windows-en-show-filename-extensions.png
    :width: 49%
    :class: align-left

*****
macOS
*****

Åbn ``Finder`` (engelsk: ``Finder``),
åbn menuen ``Finder`` (engelsk: ``Finder``) 
og vælg ``Indstillinger`` (engelsk: ``Preferences``).

Alternativt kan du åbne ``Finder`` (engelsk: ``Finder``)
og bruge genvejen ``[⌘]``\ +\ ``[,]``.

Vælg fanebladet ``Avanceret`` (engelsk: ``Advanced``).

Sæt flueben ved indstillingen ``Vis alle endelser på arkivnavne``
(engelsk: ``Show all filename extensions``).

.. thumbnail:: figs/macos-da-show-filename-extensions.png
    :width: 49%
    :class: align-left

.. thumbnail:: figs/macos-en-show-filename-extensions.png
    :width: 49%
    :class: align-left





