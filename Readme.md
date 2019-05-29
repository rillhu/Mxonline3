# OnlineEdu

## 如何开始使用？

```
git clone https://github.com/rillhu/Mxonline3.git
cd Mxonline3
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

use the address: http://127.0.0.1:8000/

## TODO:

- [ ] Docker-compose打包部署; Ueditor Xadmin 与七牛云集成(已做好，待整理); 第三方登录集成; 课程弹幕集成;

- [ ] uwagi + Nginx