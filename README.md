### 说明
统计跟踪开源区块链项目的star/fork/commit记录等信息

前端使用 Vue.js+ElementUI   后端使用 flask+mysql

### 本地运行
```
## 安装依赖
pip install -r requirements.txt

## 新建表格
python manage.py db init
python manage.py db migrate
python manage.py db upgrade


## 启动爬虫
cd spider  #进如spider目录
python spider.py

##开启服务
python manage.py runserver
```
