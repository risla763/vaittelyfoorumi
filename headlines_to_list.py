from database import db
from sqlalchemy import text

def headlines_list():
    sql = text("SELECT headline_text FROM headlines")
    data = db.session.execute(sql)

    headlines = [row[0] for row in data.fetchall()] #tekee listan
    #for headline in headlines:
        #sql = text("INSET INTO percentages (headline,agree,disagree) VALUES (:headline,COALESCE(:agree, 0), COALESCE(:disagree, 0)")
        #db.session.execute(sql, {"headline": headline})
        #db.session.commit()         
    return headlines

def count_percentages():
    result_list = []
    headlines = headlines_list()
    for i in headlines:
        sql = text("SELECT headline, SUM(CASE WHEN answer = 'agree' THEN 1 ELSE 0 END) as agree_count, SUM(CASE WHEN answer = 'disagree' THEN 1 ELSE 0 END) as disagree_count FROM answers WHERE headline = :headline_text GROUP BY headline")
        result = db.session.execute(sql, {"headline_text": i}).fetchall()
        for i in result:
            result_list.append((i))
    print(f"LOLOLOLOL {result_list}")
    return result_list

def combination(headlines,answers):
    combination_of_he_an = []
    for h, a in zip(headlines,answers):
        combination_of_he_an.append({'headline': h, 'agree_count': a[1], 'disagree_count': a[2]})
    return combination_of_he_an

    #HAE NE MÄÄRÄT JOSTAIN SE COUNT
    #MÄÄRÄT KATO OLISKO JOTAIN SQL KOMENTOO JOKA SUORAAN LASKEE PROSENTIT SEN HEADLINEN MUKAAN
