#!/usr/bin/env python
#coding: utf-8

import sys
sys.path.append("/home/cbbsaux/apps/python3/lib/python3.5/site-packages")
sys.path.append("/cmcc_na1/xfer/cbbs_interface/lib")
import cx_Oracle
import pyhs2
import pymysql

#连接oracle数据库
def get_ora_conn(user, passwd, tns):
    oracle_conn_str = "%s/%s@%s" % (user, passwd, tns)  # 连接数据库
    try:
        conn = cx_Oracle.connect(oracle_conn_str)

        return conn

    except Exception as e:
        raise e

#连接hive
def get_hive_conn(ip, port, user, passwd, tns):
    try:
        conn = pyhs2.connect(host=ip,
                            port=port,
                            authMechanism='PLAIN',
                            user=user,
                            password=passwd,
                            database=tns)

        return conn

    except Exception as e:
        raise e

def get_mysql_conn(ip, port, user, passwd, tns):
    try:
        conn_str = ip + ":" + port
        conn = pymysql.connect(conn_str, user, passwd, tns)

        return conn
    except Exception as e:
        raise e

def search(cursor, sql, type="one"):
    try:
        cursor.execute(sql)

        if "one" == type:
            result_list = list(cursor.fetchone())

            return result_list

        if "many" == type:
            result_list = list(cursor.fetchmany())

            return result_list

    except Exception as e:
        raise e
