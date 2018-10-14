#process_youyuan_mysql.py

# -*- coding: utf-8 -*-

import json
import redis
import MySQLdb

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.18.130', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = MySQLdb.connect(host='localhost', user='mysql', passwd='xxxxxxx', db = 'beer', port=3306, use_unicode=True)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["beer:items"])
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            cur.execute("INSERT INTO bjzufang (title, price, unit, rent_way_to, rent_way_to2, house_type_fl, house_type_fl2, area_fit, little_area,address,link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )", [item['title'], item['price'], item['unit'], item['rent_way_to'], item['rent_way_to2'], item['house_type_fl'], item['house_type_fl2'], item['area_fit'], item['little_area'],item['address'],item['link']])
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print "inserted %s" % item['link']
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
    main()
