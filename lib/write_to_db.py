from db_class import StorageDatabase
import pandas as pd

db = StorageDatabase("sql11.freemysqlhosting.net","3306","sql11593194","sql11593194","2CPjwjQHDQ")

df = pd.read_csv("data.csv")

for key, value in  df.to_dict().items():
    print(value)
    # db.table_add_row('TLV', value)

db.db_commit()