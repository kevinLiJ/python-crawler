# coding:utf-8
# 操作数据库的封装
import MySQLdb

USERNAME = "root"
PASSWD = "812118541"


class OperSql():
    def __init__(self, table):

        self.conn = MySQLdb.connect("localhost", USERNAME, PASSWD,
                                    table, charset="utf8")

        # 使用cursor()方法获取操作游标
        self.cursor = self.conn.cursor()

    def oper(self, fn):

        try:
            return fn(self.conn, self.cursor)
        except Exception as e:
            print e
            self.conn.rollback()
            return False

    def close(self):
        # 关闭指针
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()


def opermysql(conn, cursor):
    # 操作数据库
    cursor.execute("update test set name = 'lijianyang' where id = 1")
    cursor.execute("insert into test (name) values ('dongdongdong') ")
    result = conn.commit()
    return result


def querymysql(conn, cursor):
    # 查询数据库
    cursor.execute("select * from test")
    result = cursor.fetchall()
    return result


if __name__ == '__main__':
    opersql = OperSql('python')
    result = opersql.oper(querymysql)
    print result
