1.问题一
@property
def foo(self):
	return self._foo

log_file_max_size #代表文件最大为多少，超过时会新建一个文件
log_file_num_backups #该文件中存最近的几个文件，超过时以前的一部分就会被删除
log-rotate-mode#日期，比如每天新建一个
log-rotate-when#当什么时候新建文件

more log 
less log

tail -f log #tail表示显示这个文件的最后几行

模仿airbnb，小猪短租

项目难点:
	根据地区、位置进行筛选完之后自己写分页，
	动态加载分页，分页缓存