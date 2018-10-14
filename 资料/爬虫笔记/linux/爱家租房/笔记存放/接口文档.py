
实现流程:

前端：界面加载--->当点击时生成验证码id--->并将验证码id放到img中如：
img src=/api/pitcode?codeid=123--->此时浏览器会对未加载的链接进行向后端请求--->
/api/pitcode?codeid=123后端接收到请求，生成验证码（文本，图片）--->验证码id文本->redis设置有效期
--->返回图片--->用户填写图片验证码


获取手机验证码时需要验证图片验证码--->




1.图片验证码

描述：用来生成图片验证码

url: /api/imagecode?codeid=123&pcodeid=
method:get
传入参数 	
名称	  		类型		说明
codeid 		int		验证码编号
pcodeid 	int 	上一个验证码编号(为了保证只要一刷新上一个立即失效)

返回值:图片二进制数据

UUID
