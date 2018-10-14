处理Redis里的数据
有缘网的数据爬回来了，但是放在Redis里没有处理。之前我们配置文件里面没有定制自己的ITEM_PIPELINES，而是使用了RedisPipeline，所以现在这些数据都被保存在redis的youyuan:items键中，所以我们需要另外做处理。

在scrapy-youyuan目录下可以看到一个process_items.py文件，这个文件就是scrapy-redis的example提供的从redis读取item进行处理的模版。

假设我们要把youyuan:items中保存的数据读出来写进MongoDB或者MySQL，那么我们可以自己写一个process_youyuan_profile.py文件，然后保持后台运行就可以不停地将爬回来的数据入库了。

存入MongoDB
启动MongoDB数据库：sudo mongod

执行下面程序：py2 process_youyuan_mongodb.py

# process_youyuan_mongodb.py

# -*- coding: utf-8 -*-

import json
import redis
import pymongo

def main():

    # 指定Redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.199.108', port=6379, db=0)
    # 指定MongoDB数据库信息
    mongocli = pymongo.MongoClient(host='localhost', port=27017)

    # 创建数据库名
    db = mongocli['youyuan']
    # 创建表名
    sheet = db['beijing_18_25']

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["youyuan:items"])

        item = json.loads(data)
        sheet.insert(item)

        try:
            print u"Processing: %(name)s <%(link)s>" % item
        except KeyError:
            print u"Error procesing: %r" % item

if __name__ == '__main__':
    main()


存入 MySQL
启动mysql：mysql.server start（更平台不一样）
登录到root用户：mysql -uroot -p
创建数据库youyuan:create database youyuan;
切换到指定数据库：use youyuan
创建表beijing_18_25以及所有字段的列名和数据类型。



执行下面程序：py2 process_youyuan_mysql.py
#process_youyuan_mysql.py

# -*- coding: utf-8 -*-

import json
import redis
import MySQLdb

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.199.108', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = MySQLdb.connect(host='127.0.0.1', user='power', passwd='xxxxxxx', db = 'youyuan', port=3306, use_unicode=True)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["youyuan:items"])
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            cur.execute("INSERT INTO beijing_18_25 (username, crawled, age, spider, header_url, source, pic_urls, monologue, source_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )", [item['username'], item['crawled'], item['age'], item['spider'], item['header_url'], item['source'], item['pic_urls'], item['monologue'], item['source_url']])
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print "inserted %s" % item['source_url']
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
    main()