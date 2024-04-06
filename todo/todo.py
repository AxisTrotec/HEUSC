import pymongo

class todo:
     def dissect(info):
        #Remove activation word
        info.pop(info.index("note"))
        
        title = []
        for x in info:
            title.append(x)
        
        title = ' '.join(str(x) for x in title)  
        todo.insert(title)

     def insert(title):
        dbconnect = pymongo.MongoClient("mongodb+srv://mraxis:td2AwhSbLYYnkrj@heusc.r8nktkv.mongodb.net/?retryWrites=true&w=majority")
        dbdatabase = dbconnect["HEUSC_Database"]
        dbcollection = dbdatabase["Todo"]

        id = 0
        
        for x in dbcollection.find():
            id += 1
        
        dbdict = {"id": id,"title": title}

        x = dbcollection.insert_one(dbdict)