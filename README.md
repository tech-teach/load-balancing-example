# Load balancing example

This is a basic example of service registering and load balancing in docker
compose, the idea here is: we will have 2 services, frontend and backend, the
frontend service will serve html files and potentialy consume the backend
service, the backend service will serve a simple python api.

## Requirements

Both services will run different subdomains and the need to be scaled freely
as needed, this we should,

```bash
$ http get api.app.dev
HTTP/1.0 200 OK
Content-Type: application/json
[... omited headers ...]
{ "hostname": "9fdbbe9e4ff8", "message": "Hi there fella" }
```

and

```bash
$ http get app.app.dev
HTTP/1.1 200 OK
Content-Type: text/html
[... omited headers ...]
<!DOCTYPE html>
<html lang="en">
<head> <meta charset="UTF-8"> <title>My stuffs</title> </head>
<body> Hello </body>
</html>
```

and each of them will need to ve served by different images.

## Implementation

For implementation we used [apistar] for the backend and a simple [nginx] site
for the frontend using their default docker image, finally for load balancing
we used the nice [dockercloud-haproxy] image. Finally as listed in the
requirements we're using the git version of [apistar] just because it
implements [CORS] by default and that makes a lot of sense for APIS.

## Run

In this particular case we're using [docer-compose] however there are other
options. To run it you can,

```bash
$ docker-compose up
$ # or if you made changes
$ docker-compose up --build
```

Then you can query any of the services through,

```bash
$ curl --header 'Host: app.app.dev' 'http://localhost/'
$ curl --header 'Host: app.app.dev' 'http://localhost/'
```

That tests the _service dicovery_ part, to test the load balancing try,

```bash
$ # after killing the other docker compose up
$ docker-compose up --build --scale api=5
$ # In a different terminal
$ for i in `seq 20`; curl 'http://api.app.dev/'
```

If you check the logs you'll see that different instances of the `api` service
served those 20 requests.


[apistar]: https://github.com/tomchristie/apistar
[nginx]: https://docs.docker.com/samples/nginx/
[dockercloud-haproxy]: https://github.com/docker/dockercloud-haproxy
[CORS]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
[docker-compose]: https://docs.docker.com/compose/
