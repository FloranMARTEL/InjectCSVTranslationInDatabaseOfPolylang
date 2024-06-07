import csv

def csvToWpjson(dir):

    resultList = []

    with open(dir, newline='',encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";")
        
        csvhead = next(spamreader)
        head = [lang for lang in csvhead[1:]]

        numcol = len(csvhead)
        resultList = [""]*(numcol-1)
        

        ##generate the WPJson
        compteurligne = 0
        for rowindex,row in enumerate(spamreader):
            compteurligne += 1

            strlistTranslation = ""

            #i:0;a:2:{i:0;s:2:\"je\";i:1;s:
            strlistTranslation += "i:"+str(rowindex)+";a:"+str(2)+":{i:0"+";s:"+str(len(row[0].encode('utf8')))+":\""+row[0]+"\";i:1;s:"

            for colLang in range(1,numcol):
                resultList[colLang-1] += strlistTranslation
                #2:\"je\";}
                resultList[colLang-1] += str(len(row[colLang].encode('utf8')))+":\""+row[colLang]+"\";}"

            
        for colLang in range(1,numcol):
            
            resultList[colLang-1] = "a:"+ str(compteurligne) +":{"+resultList[colLang-1]+"}"

    
    return head,resultList

