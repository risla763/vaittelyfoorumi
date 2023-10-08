Sovellus on keskustelufoorumi, jonka tarkoitus on että siellä voi väitellä erilaisista aiheista. 
Sovellukseen voi kirjautua sisään ja ulos, kun on tehnyt oman käyttäjän.
Kirjautuneen käyttäjän avatessa sovelluksen siinä näkyy käyttäjän oma profiili, ehdotetut keskustelut ja aloita keskustelu osiot.

# Profiili:

-Käytäjä voi näyttää siinä väittelyt, jotka hän haluaa näyttää. 
   -Nyt käyttäjän profiilissa näkyy kaikki väittelyt, joihin hän on osallistunut. 

-Käyttäjä muuten näkee kaikki väittelyt johon on osallistunut yksityisenä profiilissaan.
   -Näkyy, mutta näkyy nyt myös julkisena

-Profiilissa myös näkee jollain pienellä merkillä väittelyn vieressä, etä kumpaa puolta väittelyssä kannattaa. Esim punainen ja sininen pallo  otsikon vieressä ja väittelystä painamalla saa lisätietoa tästä...

-Käyttäjä voi poistaa aloittamansa keskustelut ja myös viestinsä väittelyketjuista, joihin hän on liittynyt.

-Profiilissa näkyy erikseen käyttäjän aloittamat väittelyt ja väittelyt, joihin tämä on osallistunut.
  -Nyt käyttäjän profiilissa näkyy vain väittelyt joihin käyttäjä on osallistunut ja aloittanut samassa jonossa...



# Väittelyketjun aloittaminen:

-Käyttäjä voi aloittaa väittelyketjun antamalla ketjulle otsikon ja aloitusviestin sisällön.
   -Valmis

-Ketjun aloittanut käyttäjä voi päättää ketjun, jolloin väittely on ns päättynyt ja siihen ei enää voi lisätä viestejä, mutta väittelyketjuun osallistuneet voivat julkaista sen omassa profiilissaan, jolloin ihmiset jotka vierailevat heidän profiilessaan voivat äänestää kumpi puoli on voittanut.



# Väittelyketjuun liittyminen:

-Sovelluksessa on osio, jossa käyttäjä voi kirjoittaa hakukoneeseen sanoja ja sieltä löytyy väittelyitä,

joiden otsikot sisältävät näitä sanoja.

-Käyttäjä voi liittyä tai vain tarkastella väittelyä.
   -Valmis

-Kun käyttäjä liittyy ketjuun hänen pitää valita kumpaa puolta hän kannattaa ennen kuin lähettää siihen viestejä. (tämä myös näkyy ketjussa muille siihen ketjuun osallistuneille)



# Lisää ominaisuuksia:

-Käyttäjien profiileissa/etusivulla julkaistuja väittelyitä saa äänestää, että kumpi puoli väittelyssä on voittanut.

# Tarkemmat ohjeet mitä luvassa:

Ennen viimeistä palautusta pitää lisätä 2 tietokantaa...

Nämä tietokannat liittyisivät tähän:

Kun käyttäjä aloittaa väittelyn hänen pitää valita kahdesta väristä toinen ja tämän värinen hänen aloitusviestinsä "viestiboxi" on. Muut käyttäjät, jotka osallistuvat väittelyyn voivat lukea aloitusviestin ja päättää kannattavatko he tätä vai vastustavat tätä väitettä. Tällöin jos käyttäjä kannattaa aloitusviestin väitettä hän julkaistessa oman kommenttinsa samaan viestiketjuun, hän valitsee kahdesta väristä saman värin kuin ketjun aloitusviesti on, jolloin käyttäjän "viestiboxi" näkyy saman värisenä kuin väittelyn aloittajan viestiboxi. Ja jos käyttäjä ei kannata väitettä tämä valitsee toisen värin, jolloin tämän viestiboxi on sen värinen. 

Käyttäjien profiilissa näkyy niiden väittelyiden vieressä jompi kumpi väri pienenä pallona, joiden puolella he väittelyssä ovat.

Myös kun on valinnut kantansa sitä ei voi muuttaa.

Toinen tietokanta voisi sisältää äänestystuloksia.

Käyttäjät jotka eivät ole osallistuneet väittelyihin voivat äänestää kumpi puoli heidän mielestään on väitellyt paremmin. Tämä tapahtuu niin, että kun käyttäjä menee main pagelle niin ne väittelyt, joihin hän ei ole osallistunut niin niiden vieressä on nappi jossa lukee äänestä ja tällöin käytäjä voi äänestää kahdesta puolesta toista. Äänestämisen jälkeen käyttäjä näkee kumpi puoli on "johdolla". Tämä näkyy niin, että väittelyn viereen tulee pienet pronsentit jotka näyttävät mitä käyttäjät ovat äänestäneet. 

Käyttäjien, jotka ovat osallistuneet väittelyihin niin niiden profiilissa näkyy heidän "osallistuneet väittelyt" vieressä heidän kantansa ja pronsentit, mitä muut käyttäjät ovat äänestäneet, että kumpi puoli on voitolla. 

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
