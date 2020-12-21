import mysql.connector
import csv


def get_connection():
    try:
        mydb = mysql.connector.connect(user='root', host="127.0.0.1",
                                       password='fdwu2838FD',
                                       database='customer')
        print('connected')
        return mydb
    except Exception as e:
        print('Connection failed', e)
        return None


def create_tables(col_tab):
    sql = "create table customer("
    for i in range(0, len(col_tab)):
        if i == 0:
            sql += (col_tab[i] + ' int primary key')
        else:
            sql += (col_tab[i] + ' varchar(225)')
        sql += ', ' if i != len(col_tab) - 1 else ')'
    print(sql)
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
        print('created table customer')
    except Exception as e:
        print(e)


def insert_data(col_tab, row_tab):
    insert_sql = "insert into customer("
    for i in range(0, len(col_tab)):
        insert_sql += (col_tab[i])
        insert_sql += ', ' if i != len(col_tab) - 1 else ') values '
    for i in range(0, len(row_tab)):
        # insert_sql += str((x + ',') for x in row_tab[i])
        insert_sql += '('
        for j in range(0, len(row_tab[i])):
            insert_sql += str(row_tab[i][j]) if j == 0 else '\''+row_tab[i][j]+'\''
            insert_sql += ',' if j != (len(row_tab[i]) - 1) else ''
        # insert_sql += ', ' if i != len(row_tab) - 1 else ')'
        insert_sql += '),' if i != (len(row_tab) - 1) else ')'
    # print(insert_sql)
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(insert_sql)
        cur.close()
        conn.commit()
        print('inserted into table customer')
    except Exception as e:
        print(e)



def read_csv(file_csv):
    global data
    with open(file_csv) as csv_customer:
        csv_read = csv.reader(csv_customer, delimiter=',')
        data = list(csv_read)


if __name__ == '__main__':
    csv_file = 'customer.csv'
    data = None
    read_csv(csv_file)
    col_table = data[0]
    row_table = data[1:]
    # print(col_table)
    # print(row_table)
    # create_tables(col_table)
    insert_data(col_table, row_table)
