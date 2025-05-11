# 13-03-2025
## cybermesterskaberne
Jeg var inde på cybermesterskaberne og prøvede at lave what time is it.
Jeg prøvede at lave den i en time hvor jeg blev en smule færdig med den. 
Jeg tror jeg fik lavede den rigtige nøgle noget til at få adgang til den der post /9012340-123849081239582304213-42134123 fil
, derefter sad jeg fast. Det var, fordi det var svært at finde ud af hvordan man sendte den nøgle i en json fil med POST method. (det var også på grund af jeg løb ud af GPT-4o, men same same)

chatgpt logs: [https://chatgpt.com/share/67d29a25-df94-8003-88b9-f66e293567c8]()

Efter det gik jeg hen til overthewire, da de andre opgaver på cybermesterskaber (jeg ikke allerede havde løst) var der meget få løsninger på.
## overthewire.org
Jeg begyndte med bandit, da det er lavet til begyndere og intoducerede en til ssh.

lavede level 0 ved at indtaste det rigtige port, username og webadresse. (så jeg husker, hvordan det gøres: ssh -p 2220 bandit0@bandit.labs.overthewire.org)

Lavede level 1 ved at logge ud og ind når jeg fik kodeordet til bandit1.

Lavede level 2 ved at brug hjælpen i opgaven som var at søge på dashed filenames

Lavede level 3

Lavede level 4

Lavede level 5 ved at manuelt at tjekke dem igennem.

# 27-03-2025
## noter fra time:

CVE (Common Vulnerabilities and Exposures): et nummer af et rapporterede bug

Bug bounty: penge for at finde bug i sikkerhed

Responsible discolsure: I stedet for at sælge bug til hacker for penge så giver man viden til firmaet.

UDP: sender packets uden at tjekke om modtagelse

TCP: Med hver packets skal modtageren sende en besked som sikre for modtagelse, ellers sendes den igen.

### The seven layers of the OSI model
![img.png](billeder/seven_layer_ISO_model.png)


HTTP: port 80

Port 0-1000 er priviledged. Det kræver administrator. 


Steps:
	1. Mapping (curl til port scanning)


### Netcat (NC)
Ligesom cat, som spytter tekst ud i terminal.

netcat kan bruges til at tale til en server hvor man kan specificerer input til serveren og så spytter output ud i terminalen.

### Sql injection
Ødelægger måske databaser.

Prøver at lave en sekvens af tegn som får computeren til at tro strenget slutter tidligere og dermed skal køre en kommando i stedet for, som hacker selv kan specificere. 

lavet dette inde på link:
https://guicommits.com/how-sql-injection-attack-works-with-examples/


