def transform(csv,mysql):
    import pandas as pd
        

    #Filtering to get  activer records
    csv=csv[csv['active_record_flag']==1]
    mysql=mysql[mysql['active_record_flag']==1]

    #Joining both the dataframes 
    df_staging_transform=pd.merge(mysql,csv,on='emp_id',how='inner')
    print("\n")
    
    print("\n")
    
    #Transformation steps done by user
    out_file_path='C:/Users/shino/Documents/staging_transform_file.csv'

    month_map={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}

    df_staging_transform["emp_name"]=df_staging_transform["first_name"]+" "+df_staging_transform["last_name"]
    df_staging_transform["salary"]=df_staging_transform["base_salary"]+df_staging_transform["housing"]+df_staging_transform["stock_value"]+df_staging_transform["bonus"]
    df_staging_transform.replace("February ","February",inplace=True)
    df_staging_transform.month=df_staging_transform.month.map(month_map)
    df_staging_transform.rename(columns={"month":"payed_month"},inplace=True)
    df_staging_transform=df_staging_transform[["emp_id","emp_name","location","payed_month","Year","salary"]]
    
    #User steps end
    print("\n")
        
    df_staging_transform.to_csv(out_file_path,index=False)

    print("Transform Staging File created....")

    return(df_staging_transform,"Transform step completed successfully!!!")