
#获取当前页的链接
//div[@class="company-list-left"]/ul/li//a[1]/@href
#公司名字
//div/span[@class="title"]/h1/text()

#公司全称
//div[@class="essential"]//thead/tr

#是否获投
//div/span[@class="title"]/h1/span

#公司主页
//div[@class="link-line"]/a/@href

#公司简介
//div[@class="block"]/div[@class="abstract"][2]

# 法人姓名
# //div/ul[@cllimitedass="list-unstyled team-list limited-itemnum"]/li/div[@class="per-name"]/a/text()
# #在贵公司的职位
# //div/ul[@class="list-unstyled team-list -itemnum"]/li/div[@class="per-position"]/text()

# #产品信息
//div[@class="trigger-feedback toggle-feedback-btn"]/text()

#注册资本
//div[@class="essential"]//tbody/tr/td/span/i

#公司成立时间
//div[@class="essential"]//tbody/tr[1]/td[2]/span[2]

#公司地址
//div[@class="essential"]//tbody/tr[3]/td/span[2]
#投资人及企业列表
//div[@class="shareholder"]/table/tbody/tr/td

#商标申请方
//div[@class="block block-v padb0"]//div/p[1]
#申请总数:有些信息是空的
//div[@class="block block-v padb0"]//div/p[2]/span/text()

#企业对外投资信息列表
//div[@class="tab-pane fade bussiness_main active in"]//table[@class="table table-bordered"]/tbody/tr/td[@class]/text()


#起始页码
Host: radar.itjuzi.com
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://radar.itjuzi.com/company?page=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: _ga=GA1.2.471449210.1536411013; _gid=GA1.2.1916391213.1536411013; gr_user_id=c6d7f22d-b9c6-4cc2-a14c-c1aa6ffad5ce; identity=17791459322%40test.com; remember_code=%2F6mZRsiCm3; unique_token=632735; MEIQIA_EXTRA_TRACK_ID=19vWc1wtNpmjmkAw8VQuvJYSZvU; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1536411013,1536456432; user-radar.itjuzi.com=%7B%22n%22%3A%22%5Cu6854%5Cu53cba0ff59b700303%22%2C%22v%22%3A2%7D; Hm_lvt_80ec13defd46fe15d2c2dcf90450d14b=1536411124,1536457158; MEIQIA_VISIT_ID=19x23tWBh7QIDGPWD1Qe6Dp3cAU; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1536459438; acw_tc=781bad0815364614337788746e4dec3c8a8cfef67429f45c1dfe9d3d9c847d; session=8dadba52a25cc0d6c2668528873fddce5b4e90b5; gr_session_id_eee5a46c52000d401f969f4535bdaa78=fb28c522-3fbb-4891-9366-421eb64ccceb; gr_cs1_fb28c522-3fbb-4891-9366-421eb64ccceb=user_id%3A632735; gr_session_id_eee5a46c52000d401f969f4535bdaa78_fb28c522-3fbb-4891-9366-421eb64ccceb=true; Hm_lpvt_80ec13defd46fe15d2c2dcf90450d14b=1536461368


