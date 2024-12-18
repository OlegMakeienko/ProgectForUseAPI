Charging Station Simulator

Beskrivning

Det här projektet simulerar en laddstation för elbilar (EV) som är kopplad till ett hushåll. Simuleringen använder Python och Flask för att skapa en webbtjänst som svarar på HTTP-anrop via JSON-protokollet.

Projektet innehåller två huvudkomponenter:

Simulering av laddstationen och batteriets status.
Servern som körs lokalt och kan kommunicera med externa applikationer via API:er.
Genom att använda detta API kan användare:

Hämta information om laddstationens kapacitet.
Hämta information om hushållets energiförbrukning.

Funktioner

GET /info: Hämtar aktuell information om laddstationen, inklusive simulerad tid, hushållets energiförbrukning, batterikapacitet och om laddningen är på eller av.

Installation

För att köra projektet på din lokala maskin, följ dessa steg:

Förutsättningar
Python 3.x
Flask
Requests (för att göra HTTP-anrop till servern)

Kör servern:
Navigera till mappen där ChargingWebserver_v0.8.py finns.
Kör servern med följande kommando:
python ChargingWebserver_v0.8.py

Exempel på användning

När servern är igång, kan du göra GET- och POST-förfrågningar till servern:

GET /info:
Hämtar aktuell status för laddstationen.

curl http://127.0.0.1:5000/info