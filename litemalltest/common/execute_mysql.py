from litemalltest.common.connect_mysql import  *
db_info = {
        "host": "localhost",
        "user": "root",
        "password": "123456",
        "port": 3306
    }

def selec_sql(sql):
    db = Connectmysql(db_info)
    r = db.sql_select(sql)
    print(r)
    db.close()

def execu_sql(sql):
    db = Connectmysql(db_info)
    db.sql_execute(sql)
    db.close()

'''
del_sql1 = "delete from litemall_role where name='test1'"
execu_sql(del_sql1)
sel_sql1 = "select * from litemall_role where name='test1'"
selec_sql(sel_sql1)
ins_sql = "insert into litemall_role (5,'test2','测试2',True, , ,False) "
execu_sql(ins_sql)'''


