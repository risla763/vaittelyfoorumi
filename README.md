Sovellus on keskustelufoorumi, jonka tarkoitus on että siellä voi väitellä erilaisista aiheista. 
Sovellukseen voi kirjautua sisään ja ulos rekisteröitymisen jälkeen.
Sovelluksen osiot ovat: käyttäjän oma profiili, etusivu, aloita uusi väittely sekä väittelyt. 

# Sovelluksen osiot:

## Profiili

Sisältää käyttäjää koskevia tietoja, esimerkiksi kaikki väittelyt joihin käyttäjä on osallistunut sekä erikseen kaikki väittelyt, jotka käyttäjä on aloittanut. (Molemmat tehty) 

Profiiliin voisi vielä lisätä kaverilistan, jossa on ihmiset joita käyttäjä seuraa. (ei vielä tehty)

Myös yksi toiminto jonka voisi tehdä on että käyttäjä voi piilottaa profiilistaan väittelyt joihin hän on osallistunut tai aloittanut. Tällöin ne näkyisivät vain profiilin omistajalle. (ei vielä tehty)

Myös profiilikuvan sekä "bio:n" voisi lisätä. (ei vielä tehty)

Profiilissa myös näkee jollain pienellä merkillä väittelyn vieressä, että kumpaa puolta väittelyssä kannattaa. Esim punainen ja sininen pallo  otsikon vieressä. (ei vielä tehty)

Käyttäjä voi poistaa aloittamansa keskustelut. (ei vielä tehty)

Profiilissa näkyy kannattaako käyttäjä tällä hetkellä kumpaa puolta ja nämä lasketaan tietokantaan ja sitten main pagelle voi tulla kuinka monta käyttäjää kannattaa kumpaakin puolta. (Tee tämä seuraavaksi)

## Chat page

Näkymä, joka näkyy sovelluksen käyttäjälle kun haluaa lukea tai kommentoida yhtä väittelyä.

Eri puolten viestiboxit eri väreillä. (tehty)

Voi kommentoida väittelyyn. (tehty)

-Textarean koolla on jokin raja. (se kun sitä siis venyttää ylöspäin...työn alla)


## main page

Tässä näkyy kaikki väittelyt ja näihin on linkit, joista painamalla pääsee väittelyyn. (tehty)

Statistics (eli erilaisia tietoja käydyistä väittelyistä): 
-suosituin väittely eli väittely mihin on tullut eniten viestejä. (ei vielä tehty)
-Jokaisen väittelyn vieressä on prosentit, että kuinka paljon väitteen kanssa ollaan samaa mieltä sekä eri mieltä. (ei vielä tehty)


## Väittelyketjun aloittaminen:

-Käyttäjä voi aloittaa väittelyketjun antamalla ketjulle otsikon ja aloitusviestin sisällön. (valmis)

-Ketjun aloittanut käyttäjä voi päättää ketjun, jolloin väittely on ns päättynyt ja siihen ei enää voi lisätä viestejä, mutta väittelyketjuun osallistuneet voivat julkaista sen omassa profiilissaan, jolloin ihmiset jotka vierailevat heidän profiilessaan voivat äänestää kumpi puoli on voittanut. (ei vielä tehty)



## Väittelyketjuun liittyminen:

Sovelluksessa on osio, jossa käyttäjä voi kirjoittaa hakukoneeseen sanoja ja sieltä löytyy väittelyitä, joita käyttäjän hakemat sanat koskevat. (ei vielä tehty)

Käyttäjä voi liittyä tai vain tarkastella väittelyä. (valmis)

Kun käyttäjä liittyy ketjuun hänen pitää valita kumpaa puolta hän kannattaa ennen kuin lähettää siihen viestejä. (tehty)



# Lisää ominaisuuksia:

-Käyttäjien profiileissa/etusivulla julkaistuja väittelyitä saa äänestää, että kumpi puoli väittelyssä on voittanut. (ei vielä tehty)

# Tarkemmat ohjeet mitä luvassa:

Ennen viimeistä palautusta pitää lisätä 1 tietokanta...

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

- Myös kun teet uuden väittelyn ja valitset sille otsikon niin otsikon täytyy olla uniikki. Eli ei kahta samannimistä otsikkoa.

- Joissain kohdissa on xss-haavoittuvuutta. Ne kohdat korjaan ennen lopullista palautusta. xss-haavoittuvuutta kun voi aloittaa uuden väittelyn esimerkiksi.
