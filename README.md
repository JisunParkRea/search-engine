# search-engine

한글 형태소 분석기(nori)를 이용한 검색 엔진 구현 

[너드 팩토리 기술 블로그](https://oboki.net/workspace/bigdata/elasticsearch/elasticsearch-%ED%95%9C%EA%B8%80-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EA%B8%B0-nori/)를 참고하여 진행하였습니다.


### 개발 환경

* Windows 10 HOME
* Docker Toolbox
* Elasticsearch
* Django REST Framework


### 실행

```sh
$ git clone https://github.com/JisunParkRea/search-engine.git
$ cd search-engine

$ python -m venv venv
$ venv\Scripts\activate

$ pip install django
$ pip install djangorestframework

$ docker pull docker.elastic.co/elasticsearch/elasticsearch:7.7.1
$ docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.7.1

$ python search_engine_app\setting_bulk.py
$ python manage.py runserver
```
