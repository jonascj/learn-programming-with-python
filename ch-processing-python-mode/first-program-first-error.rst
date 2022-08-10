.. include:: ../global.rst


.. _sec-first-program-processing:

#############################
Første program og første fejl
#############################

Efter at have installeret Processing og Python Mode
kan du nu skrive og køre dit første Python program i Processing.

Du er også klar til at lave din første fejl,
bevidst eller ved et uheld. 


**************
Første program
**************
Skriv følgende kode i Processing-vinduets område (1):

.. code-block:: py
    :linenos:

    print("Python")
    print(2+2)
    fill(color(255,0,0))
    ellipse(50,50,80,80)

Tryk på Play-knappen (2) for at køre dit program.

Resultatet af programmet linje 1 og 2 er, 
at teksten ``Python`` og teksten ``4`` (resultatet af regnestykket ``2+2``)
bliver printet/vist i Processing-vinduets område (3).

Resultatet af programmes linje 3 og 4 er,
at der tegnes en rød cirkel i et nyt vindue (4).

Hvis du ikke ser disse resultater ser du højest sandsynligt en fejl.
Spring midlertidigt til afsnittet :ref:`sec-first-error-processing`
og forsøg at rette fejlen.

.. thumbnail:: figs/processing-win10-first-sketch-unsaved.png
    :width: 90%

.. _sec-first-error-processing:

***********
Første fejl
***********
Prøv at fjerne den sidste parentes i linje 1
og kør programmet igen.

.. code-block:: py
    :linenos:
    :emphasize-lines: 1

    print("Python"
    print(2+2)
    fill(color(255,0,0))
    ellipse(50,50,80,80)

Denne gang vises en fejl i Processing-vinduets område (3)
og linje 2 i Processing-vinduets område (2) er markeret.

Fejlmeddelelsen markeret med en blå firkant
giver et hint om hvad fejlen kan være:
``Maybe there's an unclosed paren og quote mark somewhere before this line?``

Hintet foreslår, at der mangler en parentes eller anførselstegn
i linjen før linje 2, altså linje 1.
Dette er korrekt, der mangler den parentes i linje 1 som vi slettede.

.. thumbnail:: figs/processing-win10-first-error.png
    :width: 90%

Hintet er desværre ikke altid så brugbart som ved den manglende parentes.
Prøv at slette det ene 2-tal i linje 2 og kør programmet igen.

.. code-block:: py
    :linenos:
    :emphasize-lines: 1

    print("Python")
    print(2+)
    fill(color(255,0,0))
    ellipse(50,50,80,80)

Samme fejlmeddelelse vises, men denne gang mangler der ikke en parentes,
det er regnestykket ``2+`` som ikke giver mening, der mangler et tal mere.
Linje 2 er dog korrekt markeret som linjen hvor der er en fejl.

***************
Gem dit program
***************
De linjers kode du har skrevet udgør et Python-program
også kaldet en skitse (engelsk: sketch) i Processing.

For at kunne dele dit arbejde med andre,
arbejde videre på det efter at have genstartet din computer osv.
skal dit program gemmes.

Vælg menuen ``[File]`` og ``[Save As]``.
Vælg et fornuftigt sted at gemme dit program,
f.eks. i en mappe kaldet ``lær_python/processing_programmer/``,
og giv programmet et fornuftigt navn, f.eks. ``my_first_sketch``.

.. seealso::
    TODO: link til afsnit om gode navne og filsystem.

.. note::
    I macOS, og visse Linux-opsætninger, befinder menuen
    ``[Filer]`` sig ikke i toppen af Processing vinduet,
    men i en menubar helt i toppen af skærmbilledet. 

.. thumbnail:: figs/processing-win10-first-sketch-save-as.png
    :width: 90%

Processing opretter en mappe med det navn du valgte,
f.eks. ``my_first_sketch`` og under den gemmer Processing to filer;
``my_first_sketch.pyde`` og ``sketch.properties``.

Begge filer er simple tekstfiler, ``.pyde``-filen indeholder koden
og ``sketch.properties`` indeholder information om, 
at programmet skal køre i Python Mode.

Efter at have gemt programmet viser Processing navnet på programmet
i vinduet.

.. thumbnail:: figs/processing-win10-first-sketch-saved.png
    :width: 90%



