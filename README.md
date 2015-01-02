Discourse 使用七牛 CDN 的话，存在上传新头像后获取到85B的空文件问题，在网站上表现为用户头像空白。该脚本能自动删除这些错误图片，七牛会重新抓取到正常的头像图片。

有关这个问题的讨论见[这里](https://meta.discoursecn.org/t/qi-niu-cdnhuo-qu-tou-xiang-de-dao-kong-bai-tou-xiang-de-wen-ti/205/4)。

该脚本只是一个权宜之计，并不能完美解决这个问题，但是能很大程度上避免人工操作的烦恼。可以等待官方或七牛出更好的解决方案。

##安装

安装依赖库

```python
sudo pip install qiniu
sudo pip install pyyaml
```

在home目录下下载本脚本

```bash
git clone https://github.com/wuchong/discourse-qiniu-helper.git
```

##执行

```python
python ~/discourse-qiniu-helper/helper.py
```

建议将该脚本设置为定期任务，每天自动执行一次。