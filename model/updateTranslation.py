# Module Imports
import mariadb
from mariadb.cursors import Cursor
import sys

import re

from convertiseur import csvToWpjson

def updateTranslation(JsonLangs,listwpJson):
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3306,
            database="www_guillemot"
        )

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur : Cursor = conn.cursor()

    cur.execute(
        "SELECT option_value FROM wp_options WHERE option_name = '_transient_pll_languages_list';", 
        ("test",))
    

    #get information of lang
    result = []
    for (index,ligne) in enumerate(cur):
        result.append(ligne)

    if len(result) != 1:
        raise IndexError
    stringResult : str = result[0][0]


    #get lang of post
    langs = [ stringResult[i.end()+7:i.end()+7+2] for i in re.finditer('slug', stringResult)]


    #get Index of Post
    id = []#get the ID of the post
    for i in re.finditer('mo_id', stringResult):
        iend = i.end()
        index1 = iend+6+stringResult[iend+6:].index('"')
        index2 = index1+1+stringResult[index1+1:].index('"')

        id.append(stringResult[index1+1:index2])


    for index, lang in enumerate(JsonLangs):

        if lang in langs:
            req = "UPDATE wp_postmeta SET meta_value='"+listwpJson[index].replace("'", "\\'")+"' WHERE meta_key='_pll_strings_translations' AND post_id="+str(id[langs.index(lang)])+";"
            cur.execute(
                req 
            )

            conn.commit()

    conn.close()
        


dirrectory = "traductionvirgu.csv"

langs,wpJson = csvToWpjson(dirrectory)


updateTranslation(langs,wpJson)