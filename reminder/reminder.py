import pymongo

class reminder:
     def insert(title, time):
        dbconnect = pymongo.MongoClient("mongodb+srv://mraxis:td2AwhSbLYYnkrj@heusc.r8nktkv.mongodb.net/?retryWrites=true&w=majority")
        dbdatabase = dbconnect["HEUSC_Database"]
        dbcollection = dbdatabase["Reminder"]

        id = 0

        for x in dbcollection.find():
            id += 1
        
        dbdict = {"id": id,"title": title, "date": time}

        x = dbcollection.insert_one(dbdict)