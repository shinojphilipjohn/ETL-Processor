def load(load_tbl):

    
    from sqlalchemy import create_engine
    from pandas.util import hash_pandas_object
    from db_credentials import datawarehouse_config
    from datetime import datetime


    import urllib.parse
    password_new=urllib.parse.quote_plus(datawarehouse_config['password'])    
    print("Connection to DataWarehouse Commencing......")
    print("\n")
    engine=create_engine("mysql+pymysql://{user}:{password}@{host}/{db}"
                         .format(user=datawarehouse_config['user'],
                                 password=password_new,
                                 host=datawarehouse_config['host'],
                                 db=datawarehouse_config['database']))
    print("Connection to {} in Datawarehouse established....".format(datawarehouse_config['database']))
    print("\n")

    #User step
    table="payroll"
    load_tbl["payroll_id"]=load_tbl['emp_id'].astype(str)+load_tbl['payed_month'].astype(str) +load_tbl['Year'].astype(str) 
    load_tbl["record_update_ts"]=datetime.now()
    load_tbl["active_record_flag"]=1

    load_tbl=load_tbl[['payroll_id', 'emp_id', 'emp_name', 'payed_month', 'location', 'salary', 'record_update_ts', 'active_record_flag']]
    print("Loading into DataWarehouse Commencing......")
    print("\n")
    print(load_tbl)
    load_tbl.to_sql(table,engine,if_exists="append",index=False)
    
    #User step end
    
    print("Loaded into {tbl} in {db} in the Datawarehouse!!!".format(tbl=table,db=datawarehouse_config['database']))
    print("\n")
    

    return("Load Completed!!!")

