# Асинхронный python для бекендеров

* Настройка проекта
```console
pip3 install -r requirements.txt
```
Дока http://127.0.0.1:8000/docs (SwaggerUI) или http://127.0.0.1:8000/redoc (ReDoc).

Запуск проекта
```console
uvicorn main:app --reload
```


* Теория
* Типовые задачи
    * http-server (https://github.com/aio-libs/aiohttp + https://github.com/MagicStack/uvloop,
      https://github.com/sanic-org/sanic, https://github.com/encode/uvicorn)
    * websocket (https://github.com/aaugustin/websockets)
    * tcp-клиент
    * http-клиент (https://github.com/aio-libs/aiohttp,
      https://github.com/encode/httpx,
      https://github.com/Neoteroi/BlackSheep)
    * ftp (https://github.com/aio-libs/aioftp)
    * sqlite (https://github.com/omnilib/aiosqlite, https://github.com/aio-libs/aioodbc)
    * postgresql (https://github.com/aio-libs/aiopg)
    * mysql, maria (https://github.com/aio-libs/aiomysql)
    * ORM (https://github.com/python-gino/gino,
      https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)
    * mongodb (https://github.com/mongodb/motor)
    * cassandra (https://github.com/aio-libs/aiocassandra)
    * memcached (https://github.com/aio-libs/aiomcache, https://github.com/aio-libs/aiocache)
    * redis (https://github.com/aio-libs/aioredis-py)
    * rabbitmq ampq (https://github.com/mosquito/aio-pika)
    * zeromq (https://github.com/aio-libs/aiozmq)
    * elastic search (https://github.com/aio-libs/aioelasticsearch,
      https://github.com/elastic/elasticsearch-py)
    * kafka (https://github.com/aio-libs/aiokafka)
    * neo4j (https://github.com/aio-libs/aioneo4j)
    * fs (https://github.com/mosquito/aiofile,
      https://github.com/Tinche/aiofiles)
    * clickhouse (https://github.com/maximdanilchenko/aiochclient,
      https://github.com/long2ice/asynch)
