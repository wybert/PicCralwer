# PicCralwer
自己的小程序用来根据图片的url直接把图片保存在本地

## Requirements

1. python3


2. python 包 pandas click

```
pip install pandas click
#or
conda install pandas click
```

3. 要爬取的图片的url文件

参考`pic_url_list.csv`

| id|mid|url                                                                |
|---|-----------------|-----------------------------------------------------|
| 0|************|http://ww1.sinaimg.cn/large/623cff04jw1dv9a1dccbtj.jpg |
| 1|************|http://ww1.sinaimg.cn/large/944e1756jw1dv9a04ag0uj.jpg |
| 2|************|http://ww2.sinaimg.cn/large/a0c0ea2fjw1dv9a00jy4kj.jpg |





##  设置

打开 `setting.yml`文件,设置

```
## 在浏览器登录微博账号,然后按F12,之后刷新,找到 cookie并copy到这里
cookie: 

## 设置每次爬虫请求之间的时间间隔,单位为秒
sleep_interval: 30

## url文件的路径
url_list_path: pic_url_list.csv

## 要保存图片的路径
picdir: /media/kandy/文档/dataDir/taifengPics1/

## 如果程序终端可以从这里设置 开始请求的 url的id
start: 0
```

## 运行

在命令行,切换到`PicCralwer`目录下

```bash
python crawlPictureV3.py --settings_path [setting file path]

```

TODO:

- 测试 访问限制和 账号以及 ip 的关系

一个多个账号可以在一个 ip 下面同时使用

- 账号的限制可以通过搜集账号获得
- 这样自动化的获得cookies就可以了
- 测试自动化获得cookies