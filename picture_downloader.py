# * * coding:utf-8 * *
import requests
import re

def get_picture_by_url(url):
    global icon
 # try:
    av = url[29:-5]
    # print av
    html = requests.get(url, params='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Mobile Safari/537.36')
    # print html.text
    html.encoding = html.apparent_encoding
    realURL = re.findall(r'img src="//i.*?.hdslb.com/bfs/archive/(.*?)" style="display:none;" class="cover_image"/>', html.text)
    #在使用findall的时候，括号前后有点将会影响结果

    # print realURL
    imageUrl = 'https://i2.hdslb.com/bfs/archive/'+realURL[0]
    # print imageUrl
    image = requests.get(imageUrl,params='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Mobile Safari/537.36')
    with open('downloadsImages/'+av+'.jpg', 'wb') as f: #路径前面不能够加斜杠
        f.write(image.content)
    if icon == 1 :
       iconUrl = 'http://i1.hdslb.com/bfs/face/' + re.findall('data-fn-src="http://i.*?.hdslb.com/bfs/face/(.*?)"', html.text)[0]
       # print iconUrl
       icon = requests.get(iconUrl,params='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Mobile Safari/537.36')
       with open('downloadsFaces/up'+re.findall('href="//space.bilibili.com/(.*?)"', html.text)[0]+'.jpg', 'wb') as f:
           f.write(icon.content)
 # except:
 #     print


if __name__ == '__main__':
  while True :
   icon = 0
   # python 中，raw_input可以输入字符串，input只能输入数字
   av = raw_input('请输入av号或者直接复制视频地址（在输入最后面加入#，可以一起下载up主的头像噢）：')
   if av[len(av)-1] == '#':
      icon = 1
      av = av[:-1]
   if av[0] == 'a':
       av = av[2:]
   if av[0] == 'h':
      av = str(re.findall('om/video/av(.*?)/', av)[0])
   if av.isdigit():  #isdigit可以判断字符串是否全部为数字
      get_picture_by_url('https://m.bilibili.com/video/av'+av+'.html')
   print '恭喜，成功了哟～'





