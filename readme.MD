
## Bot de telegram

### Descripció del bot

L'objectiu d'aquest bot es enviar la informació que demana l'usuari sobre un producte
En aquest cas el bot recull informació que ja tenim enmagatzemada

### Com funciona?

El bot es comunica mitjançant un servei de Python on tenim creades totes les funcions que preveiem
que els usuaris que interactuen amb el bot poden arribar a necessitar.

Les comandes que hi ha disponibles son:

| Comanda   |     Parametre 1      |  Parametre 2 |
|----------|:-------------:|:-------------:|
| /help |  |  |
| /info | [codi producte] |  |
| /imatge | [codi producte] | |
| /compra | [codi producte] | [quantitat] |

#### descripció de cada comanda:

| Comanda   |      Descripció      |
|----------|:-------------|
| /help |  retorna totes les comandes que hi ha disponibles |
| /info |    retorna el nom, el codi, el format i el preu del producte demanat   |
| /imatge | retorna el nom i la foto que tenim enmagatzemada del producte |
| /compra |  afageix el producte en les quantitas que hem especificat a la cistella |