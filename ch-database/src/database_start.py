import sqlite3

#Her oprettes en forbindelse til databasefilen
#Hvis filen ikke findes, vil sqlite oprette en ny tom database.
con = sqlite3.connect('start.db')
print('Database åbnet')

try:
    con.execute("""CREATE TABLE personer (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		navn STRING,
        alder INTEGER)""")
    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')

c = con.cursor()
c.execute('INSERT INTO personer (navn,alder) VALUES (?,?)', ("Hans", 38))
c.execute('INSERT INTO personer (navn,alder) VALUES (?,?)', ("Kim", 37))

#Efter at have ændret i databasen skal man kalde funktionen commit.
con.commit()

#Denne variabel bruges til at modtage input fra brugeren
inp = ''

print('')
print('Kommandoer: ')
print('  vis - Viser alle personer i databasen')
print('  ny  - Opret ny person')
print('  q   - Afslut program')

while not inp.startswith('q'):
    inp = input('> ')

    if inp == 'vis':
        c = con.cursor()
        c.execute('SELECT navn,alder FROM personer')

        for p in c:
            print('{} er {} år'.format(p[0], p[1]))

    elif inp == 'ny':
        n = input('Indtast navn: ')
        a = input('Indtast alder: ')
        c = con.cursor()
        c.execute('INSERT INTO personer (navn,alder) VALUES (?,?)', (n, a))
        con.commit()
