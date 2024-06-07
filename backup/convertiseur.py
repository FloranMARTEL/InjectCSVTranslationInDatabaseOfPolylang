import csv

def csvToWpjson(dir):

    

    with open(dir, newline='') as csvfile:
        result = "a:"

        
        spamreader = csv.reader(csvfile, delimiter=',')

        compteurLigne = 0


        stringlistVal = "{"
        for rowindex,row in enumerate(spamreader):
            if rowindex != 0:
                                 
                if rowindex != 1:
                        stringlistVal += ";"
                
                stringlistVal += "i:"+str(rowindex-1)+";a:"+str(len(row))+":"


                stringValeur = "{"
                for elementIndex,element in enumerate(row):
                    if elementIndex != 0:
                        stringValeur += ";"
                    
                    stringValeur += "i:"+str(elementIndex)+";s:"+str(len(element))+":'"+element+"'"
                stringValeur += "}"

                stringlistVal += stringValeur

                compteurLigne += 1
            

        stringlistVal += "}"
        

        result += str(compteurLigne)+":"+stringlistVal
    
    return result