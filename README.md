# Integrations WeatherAPI

- Doc for developers https://developer.yr.no/

## Task

> Необходимо написать небольшой сервис на JavaScript.
> _(Backend мы реализовали на Python с FastAPI, Frontend будет с JavaScript для интерактивности. 
> Нужно попробовать для фронтенда - htmx, Svelte)_.
> 
> доступный через собственный API, который выводит данные о ежедневной температуре в Москве 
> на время около 14:00 на столько ближайших дней, сколько возможно. Для получения сводки о погоде нужно будет
> использовать API метеорологической службы yr.no. Сервис необходимо завернуть в Dockerfile, чтобы можно было запустить 
> одной командой.
> 
> - [x] Для сервиса и API должна быть осмысленная документация.
> - [x] Покрытие кода тестами, которые проверяют реальную работу кода.
> - [x] Кроме Москвы можно указать другую локацию по координатам.
> _(Во избежания перегрузки, мы будем указывать локацию по городу, работа будет только по зарегистрированным 
> городам в БД. Автор сервиса рекомендует использовать широту и долготу до 4 заков после запятой, также требует
> кешировать ответы по `Expired` и `If-Modified-Since`)_.
> - [x] Населённый пункт можно найти по названию.
> - [x] Предусмотрена защита от перегрузки yr.no запросами через данный сервис(Кешируем)
> - [ ] Доступен Web-интерфейс, позволяющий работать с сервисом не только через API, 
> но и через браузер, как обычный пользователь.


## Run app

1. initialize data for DB
   ```bash
   make init-db
   ```
2. build image and run docker containers
   ```bash
   docker compose up
   ```
3. go swagger doc http://127.0.0.1:8000/docs


## Working with memcached

1. 
   - start memcached container
    ```bash
     sudo docker exec -it --user=root  <id container> sh
    ```
   - install telnet on alpine version
     https://gist.github.com/Ryanb58/9e63e186981090d4f2de8ec0ea420e1d
    ```bash
    apk update
    apk add busybox-extras
    netstat -tulpn | grep LISTEN
    telnet 127.0.0.1 11211
    ```

## Tests

1. Before run test, start memcached
    ```bash
    docker compose up memcached
    ```
    
2. Run tests locally in root dir
    ```bash
    pytest ./tests
    ```
3. Check test coverage
    ```bash
    coverage run -m pytest
    coverage report
    ```

## Problems

- [ ] Need correctly handling status code 304 Not Modified
- [ ] Need add simple web interface
- [ ] Try better restructured modules and dirs. Good example https://github.com/mohamad-liyaghi/fast-commerce
- [ ] Need fully asynchronous code, prevent blocking event loop


## Links

1. FTS in sqlite3, official doc - https://www.sqlite.org/fts5.html
2. FTS in sqlite3, more examples - https://www.sqlitetutorial.net/sqlite-full-text-search/
3. Sqlite3 Habr - https://habr.com/ru/articles/754400/
4. PostgreSQL : Документация - https://postgrespro.ru/docs/postgresql/
5. Weather API(s)
   + https://open-meteo.com/
   + https://openweathermap.org/
   + https://api.met.no/doc/GettingStarted - по задаче
6. Swagger specification - https://swagger.io/specification/
7. Dockerfile start app - https://docs.docker.com/get-started/02_our_app/
8. Makefiles and `make` - https://en.wikipedia.org/wiki/Make_(software), https://makefiletutorial.com/
9. cmake vs make - https://www.incredibuild.com/blog/cmake-vs-make
10. Caching in python libs. All of these implementations have the problem of unsafely threading.
Additional synchronization required.
    + functools.cache - https://docs.python.org/3/library/functools.html#functools.cache
    + cachetools - https://github.com/tkem/cachetools/
    + cachelib - https://cachelib.readthedocs.io/en/stable/simple/
    + boltons.cacheutils - https://boltons.readthedocs.io/en/latest/cacheutils.html
11. Dockerfile and compose - https://docs.docker.com/compose/gettingstarted/
12. relative-imports-in-python-3 - https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
13. FastAPI app factory - https://testdriven.io/courses/fastapi-celery/app-factory/
14. RFC 2616 - https://datatracker.ietf.org/doc/html/rfc2616
15. Memcached docker compose environs - https://hub.docker.com/r/bitnami/memcached
16. Memcached wiki - https://github.com/memcached/memcached/wiki
17. Add curl in Alpine container - https://gist.github.com/bruno-brant/e119da3713a657036ff7e3446d98176a
18. Examples Memcached commands, all args and descriptions
    https://book.hacktricks.xyz/network-services-pentesting/11211-memcache/memcache-commands
19. Alpine, Bookworm and others Docker images -
    https://stackoverflow.com/questions/52083380/in-docker-image-names-what-is-the-difference-between-alpine-jessie-stretch-an
20. Requirements format - https://pip.pypa.io/en/stable/reference/requirements-file-format/
21. Importance, history, evolution and etc. memcached +/- - https://www.dragonflydb.io/guides/memcached
22. Scaling smoothly: RevenueCat’s data-caching techniques for 1.2 billion daily API requests -
    https://www.revenuecat.com/blog/engineering/data-caching-revenuecat/
