def addToSales(store,startDate,endDate,item,description,price):
	from datetime import datetime
	from sqlite3 import connect

	conn = connect('coupons.db')
	curs = conn.cursor()
	db_rows = curs.execute('SELECT Id FROM sales where store=? and endDate=? and item=? and description=? and price=?',(store,endDate,item,description,price))
	if not db_rows.fetchone():
		curs.execute('insert into sales (store,startDate,endDate,item,description,price,AddedTS) values (?,?,?,?,?,?,datetime("now"))',(store,startDate,endDate,item,description,price))
		
	conn.commit()
	curs.close()
	conn.close()
	return
