import pymongo

class reminder:
    #Dissect data array passed from analyze@main.py
    def dissect(data):
        #subordinating_conjunction = {"even though","provided","provide that","if","if then","if when","if only","just as","where","wherever","whereas","where if","whether","since","because","whose","whoever","unless","while","before","why","so that","until","how","since","than","till","whenever","supposing","when","or not","what"}
        prepostions_time = {"on","in","at","for","before","by","after"}

        desc = []
        time = []

        data.pop(data.index("remind"))
        data.pop(data.index("me"))
        data.pop(data.index("to"))

        flag = False

        for x in data:
            if x in prepostions_time:
                flag = True

            if not flag:
                desc.append(x)
            else:
                time.append(x)

        title = ' '.join(str(x) for x in desc)
        date = ' '.join(str(x) for x in time)

        reminder.insert(title,date)
    
    def insert(title, date):
        dbconnect = pymongo.MongoClient("mongodb+srv://mraxis:td2AwhSbLYYnkrj@heusc.r8nktkv.mongodb.net/?retryWrites=true&w=majority")
        dbdatabase = dbconnect["HEUSC_Database"]
        dbcollection = dbdatabase["Reminder"]

        id = 0

        for x in dbcollection.find():
            id += 1
        
        dbdict = {"id": id,"title": title, "date": date}

        x = dbcollection.insert_one(dbdict)