import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
  
class ImagesPipeline(ImagesPipeline):
  #因为不是按原来的object用了所以这个可以不用了
  #def process_item(self, item, spider):
      #return item
  #获取settings文件里设置的变量值
  IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
 #获取图片的链接并且发送图片的请求
  def get_media_request(self,item,info):

      image_url = item["imagelink"]
      yield scrapy.Request(image_url)

  def item_completed(self,result,item,info):
      image_path = [x["path"]for ok,x in result if ok]
      os.rename(self.IMAGESTORE + "/" + image_path[0],self.IMAGES_STORE + "/" + item["nickname"] + ".jpg"
      item["imagePath"] = self.IMAGE_STORE + "/" + item["nickname"]
      return item