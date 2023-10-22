# Väittelyfoorumi

Sovellus on keskustelufoorumi, jonka tarkoitus on että siellä voi väitellä erilaisista aiheista. 
Sovellukseen voi kirjautua sisään ja ulos, sen jälkeen kun on rekisteröitynyt käyttäjäksi.
Sovelluksen osiot ovat: käyttäjän oma profiili, etusivu sekä aloita uusi väittely. 

# Sovelluksen osiot:

[Profiili](#profiili)

[Väittely](#chat_page)

[Etusivu](#main_page)

[Uuden väittelyn aloittaminen](#start_debate")

[Muuta](#liity_vait)


## Profiili

<a name="profiili"></a>

Profiili sisältää käyttäjää koskevia tietoja, esimerkiksi kaikki väittelyt joihin käyttäjä on osallistunut sekä erikseen kaikki väittelyt, jotka käyttäjä on aloittanut. (Molemmat tehty) 

Profiiliin voisi vielä lisätä kaverilistan, jossa on ihmiset joita käyttäjä seuraa. (ei vielä tehty)

Myös yksi toiminto jonka voisi tehdä on että käyttäjä voi piilottaa profiilistaan väittelyt joihin hän on osallistunut tai aloittanut. Tällöin ne näkyisivät vain profiilin omistajalle. (ei vielä tehty)

Myös profiilikuvan sekä "bio:n" voisi lisätä. (ei vielä tehty)

Profiilissa myös näkee jollain pienellä merkillä väittelyn vieressä, että kumpaa puolta väittelyssä kannattaa viimeisen viestinsä perusteella. (tehty)

Käyttäjä voi poistaa aloittamansa keskustelut. (tehty)

Käyttäjä voi päättää aloittamansa keskustelut, jolloin niihin ei voi enää lisätät viestejä. (tehty, mutta tämä jäi hieman kesken)

## Chat page

<a name="chat_page"></a>

Näkymä, joka näkyy käyttäjälle kun käyttäjä lukee tai kommentoi tiettyä väittelyä.(tehty)

Eri puolten viestiboxit eri väreillä. Eli viestien tekstiboksit näkyvät eri väreillä riippuen siitä kumpaa puolta kannattaa. (tehty)

Voi kommentoida väittelyyn. (tehty)

-Textarean koolla on jokin raja. (ei tehty)


## Etusivu

<a name="main_page"></a>

Tässä näkyy kaikki väittelyt ja näihin on linkit, joista painamalla pääsee väittelyyn. (tehty)

Statistics (eli erilaisia tietoja käydyistä väittelyistä): 
-suosituin väittely eli väittely mihin on tullut eniten viestejä. (tehty)
-Jokaisen väittelyn vieressä on luvut, että kuinka paljon väittelyn aloittajan kanssa ollaan samaa mieltä sekä eri mieltä. (tehty)

## Väittelyketjun aloittaminen:

<a name="start_debate"></a>

-Käyttäjä voi aloittaa väittelyketjun antamalla ketjulle otsikon, mielipiteensä ja aloitusviestin sisällön. (valmis)

-Ketjun aloittanut käyttäjä voi päättää ketjun, jolloin väittely on ns päättynyt ja siihen ei enää voi lisätä viestejä, mutta väittelyketjuun osallistuneet voivat julkaista sen omassa profiilissaan, jolloin ihmiset jotka vierailevat heidän profiilessaan voivat äänestää kumpi puoli on voittanut. (pantu alulle, mutta ei tehty loppuun (jäi keskeneräiseksi))



## Väittelyketjuun liittyminen:

<a name="liity_vait"></a>

Sovelluksessa on osio, jossa käyttäjä voi kirjoittaa hakukoneeseen sanoja ja sieltä löytyy väittelyitä, joita käyttäjän hakemat sanat koskevat. (tehty)

Käyttäjä voi liittyä tai vain tarkastella väittelyä. (tehty)

Kun käyttäjä liittyy ketjuun hänen pitää valita kumpaa puolta hän kannattaa ennen kuin lähettää siihen viestejä. (tehty)



# Lisää ominaisuuksia:

-Käyttäjien profiileissa/etusivulla julkaistuja väittelyitä saa äänestää, että kumpi puoli väittelyssä on voittanut. (ei vielä tehty)

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


- Joissain kohdissa on xss-haavoittuvuutta. Ne kohdat korjaan ennen lopullista palautusta. xss-haavoittuvuutta kun voi aloittaa uuden väittelyn esimerkiksi. (korjattu)
