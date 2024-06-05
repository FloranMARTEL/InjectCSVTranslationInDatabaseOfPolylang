import csv

def csvToWpjson(dir):

    resultList = []

    with open(dir, newline='',encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";")
        numcol = len(next(spamreader))
        resultList = [""]*(numcol-1)
        
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
            #a:3:{i:0;a:2:{i:0;s:2:\"je\";i:1;s:2:\"je\"};i:1;a:2:{i:0;s:1:\"n\";i:1;s:4:\"nous\"};i:2;a:2:{i:0;s:1:\"v\";i:1;s:4:\"vous\"}}
            resultList[colLang-1] = "a:"+ str(compteurligne) +":{"+resultList[colLang-1]+"}"

    
    return resultList


def mergeWPJson(str1,str2):
    pass
     

wpJson = csvToWpjson("traductionvirgu.csv")

for st in wpJson:
     print(st)
     print("----------------------")