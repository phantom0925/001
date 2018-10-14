 1993  ssh-keygen -t rsa  -C "995945908@qqcom"#创建项目的ssh key
 1994  cd  .ssh/
 1997  sudo vi id_rsa.pub#将key复制到github中
 2002  cd Desktop/
 2004  git clone git@github.com:phantom0925/plane-crawl.git#将github上的项目下载到本地仓库
 2008  git init#表示对这个项目进行管理
 2011  git config --global user.name phantom #修改用户名
 2012  git config --global user.email 995945908@qq.com#修改邮箱
