Sovellus on keskustelufoorumi, jonka tarkoitus on että siellä voi väitellä erilaisista aiheista. 
Sovellukseen voi kirjautua sisään ja ulos, kun on tehnyt oman käyttäjän.
Kirjautuneen käyttäjän avatessa sovelluksen siinä näkyy käyttäjän oma profiili, ehdotetut keskustelut ja aloita keskustelu osiot.

# Profiili:

-Käytäjä voi näyttää siinä väittelyt, jotka hän haluaa 

-Käyttäjä muuten näkee kaikki väittelyt johon on osallistunut yksityisenä profiilissaan

-Profiilissa myös näkee, jos väittely on julkaistuna niin kumman puolen ihmiset ovat äänestäneet että olisi voitolla/voittanut

-Käyttäjä voi poistaa aloittamansa keskustelut ja myös viestinsä väittelyketjuista, joihin hän on liittynyt.



# Väittelyketjun aloittaminen:

-Käyttäjä voi aloittaa väittelyketjun antamalla ketjulle otsikon ja aloitusviestin sisällön.

-Ketjun aloittanut käyttäjä voi päättää ketjun, jolloin väittely on ns päättynyt ja siihen ei enää voi lisätä viestejä, mutta väittelyketjuun osallistuneet voivat julkaista sen omassa profiilissaan, jolloin ihmiset jotka vierailevat heidän profiilessaan voivat äänestää kumpi puoli on voittanut.



# Väittelyketjuun liittyminen:

-Sovelluksessa on osio, jossa käyttäjä voi kirjoittaa hakukoneeseen sanoja ja sieltä löytyy väittelyitä,

joiden otsikot sisältävät näitä sanoja.

-Käyttäjä voi liittyä tai vain tarkastella väittelyä.

-Kun käyttäjä liittyy ketjuun hänen pitää valita kumpaa puolta hän kannattaa ennen kuin lähettää siihen viestejä. (tämä myös näkyy ketjussa muille siihen ketjuun osallistuneille)



# Lisää ominaisuuksia:

-Käyttäjien profiileissa/etusivulla julkaistuja väittelyitä saa äänestää, että kumpi puoli väittelyssä on voittanut.

# käyttöönotto:

Kirjoita seuraavat komennot terminaaliin:

python3 -m venv venv

source venv/bin/activate

Asenna riippuvuudet näillä komennoilla:

pip install -r requirements.txt

psql < schema.sql

Käynnistä projekti:


flask run

Luo ennen käynnistystä kuitenkin .env tiedosto kansioon, jonne sijoita nämä:

SECRET_KEY = tähän asenna secret key
DEBUG = True
DATABASE_URL = postgresql:///user 


Laita user kohdalle oma käyttäjä.


# Huomion arvoista

- Kun on aloittamassa uutta väittelyä niin pitää kirjoittaa username kohtaan oikea username tietokannasta tai muuten tulee error.

- Myös kun teet uuden väittelyn ja valitset sille otsikon niin otsikon täytyy olla uniikki. Eli ei kahta samannimistä otsikkoa.
