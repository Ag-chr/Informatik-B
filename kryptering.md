# Kryptering
## 10-01-25
https://informatik.systime.dk/?id=810
### Krav til kryptering system:
	• Privathed (privacy)
		○ Ingen ved at man er den som sender
	• Fortrolighed (confidentiality)
		○ Den besked man sender til en bliver kun set af den som man sender til.
	• Integritet (Intergerity)
		○ Man kan stole på at det virker
	• Uafviselighed
		○ Hvis man krypterer en besked så ved de andre at man er den som har krypteret det.
	• Sikkerhed (ligesom en rundkørsel)

Message: M
Cipher: C

Afsender og modtager er enig om nøgle

### To kategorier af kryptering:
	1. Symmetrisk (Caesar cipher). Begge skal blive enig om nøgle, hvor de er nødt til at sende det ukrypteret.
	2. Asymmetrisk
		RSA:
		Alle har en public og secret key. Kaldes for et nøglepar. Public key bliver uddelt til alle.
		pk: public key
		sk: secret key
		
		public_key(M) --> C
		Den C kan kun dekrypteres med ejerens secret key.

ob: Står for binæer

Matematikken i RSA

#### RSA keygen:
2 primtal: Kaldes p og q.

n produkt af de to primtal

n=p·q

e skal være større end n

e=3

d er en funktion som beregner noget med e, n, p, q

d=math(e,n,p,q)

Public key er: n og e

Secret key er: n og d



Mod: modulær

Når en besked sendes af en som hedder A og modtageren er B

Når A sender beskeden krypteres den med B's public key:

C_Bpk=M^(e_B )  mod n_B

Dekrypteres af B:

M=C^d  mod n

Signature: Så man kan se hvem afsenderen er. Det sendes med beskeden

Hash(M)→sign_sk (Hash→signature sendes med M

Der bruges SHA 256 til signaturen

Regning af d

λ(n): Greatest commom denomerator
d=e^(−1)  mod(λ(n))

## 17-01-2025


