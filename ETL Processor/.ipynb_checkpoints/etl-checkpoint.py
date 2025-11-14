# ETL Processor

#Import the file location and other arguments from cmd line


import sys
path=sys.argv[1]
sys.path.append(path)

#Info to the user
import os
print("-------------------------------")
print(" =====   ======  ||")
print("||         ||    ||")
print("||==       ||    ||")
print("||         ||    ||")
print(" =====     ||     =====")
print("-------------------------------")
print("ETL Processor Initialising.......")
print("Folder location contains:" , os.listdir(path))

#Checking if the necessary files are present 
files=os.listdir(path)
necessary_files=['db_credentials.py', 'main.py', 'sql_queries.py']

print("Checking if all necessary files are present.......")

miss_file=[file for file in necessary_files if file not in files]
missing_no=len(necessary_files)-len(miss_file)

if len(miss_file)==0:
    print("All necessary files are present!")
else:
    print("Check files, as only",missing_no," files are available out of the the ", len(necessary_files),"required files to continue!!!")
    print("Missing Files:", miss_file)

#Connecting to the source systems

print("Initialising the connection to the server......")
print("Fetching info to connect to the server......")

from db_credentials import source_server_config,datawarehouse_config
import mysql.connector
from mysql.connector import errorcode

conn_db=mysql.connector.connect(**source_server_config)

print("Connection successful to",source_server_config['database'],"database!")

# Extract process

print("Extraction process from sources initialising.....")
print("\n")
import extract as ex
df_CSV_staging,df_sql_staging,confirm=ex.extract()

print("Data in the ", df_CSV_staging.name,".......")
print("\n")
print(df_CSV_staging)
print("\n")
print("Data in the ", df_sql_staging.name,".......")
print("\n")
print(df_sql_staging)
print("\n")
print(confirm)

#DDL DW creation
print("\n")
print("DDL process initialising.....")

import sql_DDL_queries as dl
print("\n")
print(dl.ddl())

#Transforming the data
print("\n")
import transform as tr
print("Transforming process initialising.....")
transform_df,msg=tr.transform(df_CSV_staging,df_sql_staging)
print("\n")
print(msg)

#Load data
import load as ld
ld.load(transform_df)
