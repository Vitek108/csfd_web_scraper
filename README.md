# ČSFD SCRAPE WEB

Jednoduchá Django aplikace, která scrapuje názvy a herce z databáze 300 ČSFD filmů. Na homepage je vyhledávání, které přináší výsledky jak mezi názvy filmů a jmény herců. Detail filmu zobrazuje herce, kteří v něm hrají. Detail herce zobrazuje filmy, ve kterém hraje.

Databáze SQLite je v tomto případě přiložená v repozitáři.

##Stažení databáze
Script na stažení dat je implementovaný v management command (csfd_app/management/commands/scrape.py). Pro stažení dat je možné použít příkaz:

<code>python manage.py scrape</code>

##Printscreen aplikace (vyhledávání)
![ČSFD web](./static/images/csfdweb.png "ČSFD web")