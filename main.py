import psycopg2


username = 'postgres'
password = '111'
database = 'oliksiy'

query_1 = '''
SELECT trim(video.title),statistic.comment_count from video,statistic
where statistic.video_id = video.video_id

'''

query_2 = '''
select sum(likes),sum(dislikes) from statistic

'''

query_3 = '''
SELECT trim(video.title),statistic.viewse from video,statistic
where statistic.video_id = video.video_id and statistic.viewse>30000000

'''

conn = psycopg2.connect(user = username, password = password, dbname = database)

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    print('1.\n')
    cur.execute(query_1)
    for row in cur:
        print(row[0])
        print(row[1])

    print('2.\n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('3.\n')
    cur.execute(query_3)
    for row in cur:
        print(row)