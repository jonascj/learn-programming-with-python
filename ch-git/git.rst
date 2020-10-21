.. _sec-git:

#################################
Git (distributed version control)
#################################

.. list-table:: 
    :header-rows: 1

    * - Beskrivelse/handling
      - Kommando
      - Eksempel

    * - Klon/hent/kopier repository
      - ``git clone <url>``
      - ``git clone https://github.com/<username>/repo-name.git``

    * - Se status på din lokale repository
      - ``git status``
      - 

    * - Tilføj en ny (untracked) fil til repository
      - ``git add <untracked file>``
      - ``git add app.py``

    * - Tilføj en eksisterende fil med ændringer til et (kommende) commit
      - ``git add <already tracked file>`` 
      - ``git add app.py``

    * - Commit ændringer (tilføjet til commit vha. ``git add``)
      - ``git commit -m "description of changes"``
      - ``git commit -m "Improved error handling of user input"``

    * - Offentliggør ændringer til github (remote repository)
      - ``git push origin master``
      - 


