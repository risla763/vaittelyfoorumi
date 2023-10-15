from database import db
from sqlalchemy import text

def headlines_list():
    sql = text("SELECT headline_text FROM headlines")
    data = db.session.execute(sql)
    headlines = [row[0] for row in data.fetchall()] #tekee listan    
    return headlines

def opinions_list():
    result_list = []
    headlines = headlines_list()
    for i in headlines:
        sql = text("SELECT opinion FROM opinions WHERE headline = :headline")
        result = db.session.execute(sql, {"headline": i}).fetchall()
        for i in result:
            result_list.append((i))
    print(f"STATEEEMEEEENTSS {result_list}")
    return result_list

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

def combination(headlines,answers,opinions):
    combination_of_three = []
    for h, a, o in zip(headlines,answers,opinions):
        combination_of_three.append({'headline': h, 'agree_count': a[1], 'disagree_count': a[2], 'opinion':o[0]})
    return combination_of_three


