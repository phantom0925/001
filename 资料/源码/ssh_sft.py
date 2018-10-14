import paramiko

transport = paramiko.Transport(('192.168.1.14', 22))
transport.connect(username='root', password='995945908')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('笔记', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/home/phantom/1.txt', 'fromlinux.txt')

transport.close()