# BI.Zone test app

Default host and port are:
```
0.0.0.0:5000
```
*Example curl request command:*
```
curl -X POST -H 'Content-Type: application/json' -d '{"x":5, "y":4, "map": [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]}' http://localhost:5000/api/islands
```
*Example response:*

```
{"count":1}
```

# Set another ip and port

**You should use environment variables**

*Example:*
```
ENDPOINT_HOST = '127.0.0.1'
ENDPOINT_PORT = 3000
```

# Docker

**Image on dockerhub:**

```
https://hub.docker.com/repository/docker/damirchikr/bi.zone_test
```

*Example docker-compose file:*
```
version: '3.5'

services:
    test_app:
        image: damirchikr/bi.zone_test:latest
        container_name: test_app
        restart: always
        environment:
            - ENDPOINT_HOST
            - ENDPOINT_PORT=5001
        ports:
            - 5000:5001
```
