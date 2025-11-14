def extract(): 
     #csv file extraction
    import pandas as pd

    #User step
    file_source='C:/Users/shino/OneDrive/Documents/salary.csv'

    #User step end

    df_CSV_staging=pd.read_csv(file_source)
    df_CSV_staging.name='Data Frame Source CSV Staging'

    # mysql source table extraction
    import mysql.connector
    from db_credentials import source_server_config

    conn_db=mysql.connector.connect(**source_server_config)
    cursor=conn_db.cursor()

    #User step
    query="SELECT * FROM employees"

    #User step end 

    l=[]
    cursor.execute(query)
    for x in cursor:
        # print("{}".format(x))
        l.append(x)
    
    #User step
    df_sql_staging=pd.DataFrame(l,columns=['emp_id','first_name','last_name','birth_date','gender','location','record_update_ts','active_record_flag'])
    
    #User step end
    
    df_sql_staging.name='Data Frame Source MYSQL Table Staging '
    cursor.close()
    conn_db.close()

    #Checking the dataframes
    #Printing the dataframes to check the data inside
    # print("Data in the ", df_CSV_staging.name,".......")
    # print("\n")
    # print(df_CSV_staging)
    # print("\n")
    # print("Data in the ", df_sql_staging.name,".......")
    # print("\n")
    # print(df_sql_staging)

    return(df_CSV_staging,df_sql_staging,"Extract Process Completed!!!")
