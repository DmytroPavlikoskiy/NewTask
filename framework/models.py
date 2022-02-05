from abc import ABC
from NewTask.framework.config import InfoConn
from mysql import connector
from mysql.connector import Error


class Model(ABC):
    table = ""

    @classmethod
    def connects(cls):
        try:
            cls.connect = connector.connect(host=InfoConn.host,
                                            port=InfoConn.port,
                                            user=InfoConn.user,
                                            password=InfoConn.password,
                                            database=InfoConn.database)
            if cls.connect.is_connected():
                print("Connect to mySQL")
        except Error as e:
            print(e)
        cursor = cls.connect.cursor()
        return cursor

    @classmethod
    def get_all(cls):
        cursor = cls.connects()
        sql = ("SELECT * FROM " + cls.table)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def search_by(cls, parameters, choose):
        cursor = cls.connects()
        sql = ("SELECT * FROM " + cls.table + " WHERE " + parameters + "=" + "'" + choose + "'")
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            cursor.rollback()

    @classmethod
    def update_user(cls, type_id, choose, parameters):
        cursor = cls.connects()
        sql = ("UPDATE " + cls.table + " SET " + choose + " = " + "'" + parameters + "'" + " WHERE id = " + str(
            type_id))
        try:
            cursor.execute(sql)
            cls.connect.commit()
            return cls.connect.fetchall()
        except:
            cls.connect.rollback()

