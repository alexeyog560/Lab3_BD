import psycopg2
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

username = 'postgres'
password = '111'
database = 'LAB3'


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

    periods = []
    p_count = []
    #negative = []
    plt.xticks(rotation=5)
    i=0
    for row in cur:
        i+=1
        if i==20:
            break
        periods.append(row[0])
        p_count.append(row[1])
    sns.barplot(x = periods , y = p_count)
    plt.show()


    print('2.\n')
    cur.execute(query_2)
    periods = []
    p_count = []
    explode = []
    for row in cur:
        explode.append(0.08)
        periods.append(row[0])
        print(row[0],row[1])
        p_count.append(row[1])
    p_count.append(periods[0])
    print(p_count)
    label=["dislike","like"]
    plt.pie(p_count,labels=label , autopct='%1.1f%%')

    plt.show()

    def bulba(list,name):
        sorted = True
        lent = len(list)
        for i in range(lent - 1):
            sorted = True
            for j in range(lent - (i + 1)):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    name[j], name[j + 1] = name[j + 1], name[j]
                    sorted = False
            if sorted:
                break
        return list,name
    print('3.\n')
    cur.execute(query_3)

    periods = []
    p_count = []
    plt.xticks(rotation=5)
    i = 0
    for row in cur:
        if i==20:
            break
        periods.append(row[0])
        p_count.append(row[1])
        i+=1
    bulba(p_count,periods)
    sns.lineplot(x = periods, y = p_count)
    plt.show()