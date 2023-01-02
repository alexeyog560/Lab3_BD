import csv
import psycopg2



username = 'postgres'
password = '111'
database = 'LAB3'
host = 'localhost'
port = '5432'

OUTPUT_FILE_T = 'Osinovyi_DB_{}.csv'

TABLES = [
    'video',
    'statistic',
    'channel'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w',encoding="UTF-8" ) as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])