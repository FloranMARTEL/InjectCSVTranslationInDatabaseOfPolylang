# Module Imports
import mariadb
import sys

import re


def updateTranslation(JsonLangs,listwpJson,user,password,host,port,database):
    # Connect to MariaDB Platform
    
    
    conn = mariadb.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
    )

    # Get Cursor
    cur = conn.cursor()

    cur.execute(
        "SELECT option_value FROM wp_options WHERE option_name = '_transient_pll_languages_list';", 
        ("test",))
    

    #get information of lang
    result = []
    for (index,ligne) in enumerate(cur):
        result.append(ligne)

    if len(result) != 1:
        raise IndexError("Lang non trouvé, le plugin polylang est-il bien installé")
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
        