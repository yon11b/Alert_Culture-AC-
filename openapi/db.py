import pymysql

# DB 연결 함수
def connect_DB():
    con = pymysql.connect(
        host='',
        user='',
        password='',
        charset='',
        db=''
    )
    return con