import psycopg2
import sys

'''
该文件，暂时没有用
'''


def view_bar(num, total, other=''):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("=" * num, " " * (100 - num), rate_num) + '  ' + str(other)
    sys.stdout.write(r)
    sys.stdout.flush()


with open('../all_acute_kidney_hadm_id.txt') as file:
    all_acute_kidney_hadm_id = [L.strip('\n') for L in file]
print(all_acute_kidney_hadm_id)

with psycopg2.connect(database="mimic", user="postgres", password="123456", host="202.117.54.54",
                      port="5432") as conn, conn.cursor() as cur:
    print('connect successful!')
    print('一共有：', len(all_acute_kidney_hadm_id), '个icu_id       \n开始找hadm_id')
    for i, hadm_id in enumerate(all_acute_kidney_hadm_id[:10]):
        cur.execute("SELECT "
                    "DISTINCT mimiciii.chartevents.icustay_id, "
                    " mimiciii.chartevents.hadm_id "
                    "From mimiciii.chartevents "
                    "WHERE "
                    " chartevents.hadm_id = %s ", (str(hadm_id),))
        print(i, ':')
        print(cur.fetchall())
