import csv
import psycopg2

username = 'postgres'
password = '111'
database = 'LAB3'

INPUT_CSV_FILE = 'GBvideos.csv'

delete_all = '''
DELETE FROM channel;
DELETE FROM statistic;
DELETE FROM video;
'''

query_video = '''
INSERT INTO video (video_id, title ,publish_time)  VALUES (%s, %s, %s)
'''

query_chanel = '''
INSERT INTO channel(video_id, channel_title) VALUES (%s, %s)
'''

query_stat = '''
INSERT INTO statistic (video_id, viewse, comment_count, likes, dislikes) VALUES (%s, %s, %s, %s,%s)
'''


conn = psycopg2.connect(user=username, password=password, dbname=database)

def find_count(s):
    word_list = s.split()
    for i in word_list:
        if i.isnumeric():
            return i
    return 0


def chanel_insert(idx,local_video_id, local_row, local_cur,globals):
    local_cur.execute(query_chanel, (local_video_id, local_row))

def video_insert(local_video_id, local_title, local_public, local_cur,globals):
    local_cur.execute(query_video, (local_video_id, local_title, local_public))



def stat_insert(local_video_id, local_views, local_com_count,local_likes, local_dislike, local_cur,globals):
    local_cur.execute(query_stat, (local_video_id, local_views, local_com_count,local_likes, local_dislike))


with conn:
    cur = conn.cursor()
    cur.execute(delete_all)
    with open(INPUT_CSV_FILE, 'r',encoding="UTF-8") as ret:
        reader = csv.DictReader(ret)
        globals=[]
        i=0
        for idx, row in enumerate(reader):
            if globals.count(row['video_id'].strip()) == 0:
                globals.append(row['video_id'].strip())
                video_insert(row['video_id'], row['title'], row['publish_time'], cur,globals)
                chanel_insert(idx, row['video_id'], row['channel_title'], cur, globals)
                stat_insert(row['video_id'], row['views'], row['comment_count'], row["likes"], row["dislikes"], cur,globals)

                i+=1
        print("Done", i )
    conn.commit()