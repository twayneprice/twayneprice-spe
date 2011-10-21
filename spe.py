def addPageToDb( process, page):
	from datetime import datetime
	from sqlite3 import connect

	conn = connect('spe.db')
	curs = conn.cursor()

	db_rows = curs.execute('SELECT Id FROM pages where Process=? and Page=?',(process,page))
	if not db_rows.fetchone():
		curs.execute('insert into pages (Process,Page,AddedTS) values (?,?,datetime("now"))',(process,page))
	conn.commit()
	curs.close()
	conn.close()
	return
def getPagesFromDb(process):
	from datetime import datetime
	from sqlite3 import connect

	db = connect('spe.db')
	c = db.cursor()
	db_rows = c.execute('SELECT page,Id FROM pages where process=? and (processed<>1 or processed is null)',[(process)])
	rows = []
	for db_row in db_rows:
		rows.append(db_row)
	c.close()
	db.close()
	return rows	
def removeNonAscii(s): 
	return "".join(i for i in s if ord(i)<128)
def setPageAsProcessed(Id):
	from datetime import datetime
	from sqlite3 import connect

	conn = connect('spe.db')
	curs = conn.cursor()

	curs.execute('update pages set Processed=1,ProcessedTS=datetime("now") where Id = ?',[(Id)])
	conn.commit()
	curs.close()

	return
	