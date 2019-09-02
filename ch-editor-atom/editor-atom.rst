.. include:: ../global.rst

.. _sec-editor-atom:

#############
Atom (editor) 
#############


.. _sec-editor-atom-theme:

************************
Skift til lyst farvetema
************************

Atom benytter som standard et mørkt farvetema,
men kommer også med et glimrende lyst farvetema.  
Farvetemaet kan skiftes på følgende måde:

Åbn ``Settings`` (indstillinger)
(Windows/Linux: ``ctrl``\ +\ ``,``, macOS: ``⌘``\ +\ ``,``)
og vælg fanebladet ``Themes``.

Vælg et lyst tema under ``UI Theme`` og/eller ``Syntax Theme``,
f.eks. ``One Light``.

.. thumbnail:: figs/atom-change-theme.png
   :width: 80%
   :align: center

Med både ``UI Theme`` og ``Syntax Theme`` valgt til ``One Light``
ser Atom nu således ud:
 
.. thumbnail:: figs/atom-light-theme.png
   :width: 80%
   :align: center


****************************
Working directory for Python
****************************

.. admonition:: TODO
    
    Working directory for Python afhænger af opsætningen af script.
    Som standard er det et *projektbibliotek*,
    men det kan ændres til at være mappen hvor scriptet befinder sig.


**************************************
Python3 i stedet for Python2.7 i macOS
**************************************

.. admonition:: TODO
    `python` i macOS's path peger som standard på en python 2.7 fortolker.
    Derfor benytter både ``atom-python-run`` og ``script`` pakkerne
    python2.7 som standard på macOS. 
    Skriv her hvordan det ændres.
