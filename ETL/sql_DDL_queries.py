def ddl():  
    #User step for DDL

     # DDL scipt for target table in the DW
    new_table={}
    new_table["payroll"]=(
        "CREATE TABLE IF NOT EXISTS payroll("
        "payroll_id VARCHAR(200) NOT NULL," 
        "emp_id INTEGER NOT NULL,"
        "emp_name VARCHAR(100),"
        "payed_month VARCHAR(20),"
        "location VARCHAR(50),"
        "salary DECIMAL,"
        "record_update_ts DATETIME,"
        "active_record_flag char(1),"
        "PRIMARY KEY (payroll_id)) ENGINE=InnoDB"
    )

    #User step end

    import mysql.connector
    from db_credentials import datawarehouse_config
    conn_db=mysql.connector.connect(**datawarehouse_config)
    print("Connection to {} in Datawarehouse established....".format(datawarehouse_config['database']))
    print("\n")
    cursor=conn_db.cursor()

    #User step
    cursor.execute(new_table['payroll'])
    #User step end

    print("MYSQL Table Created!")

    cursor.close()
    conn_db.close()
    return("DDL process completed !!!")

