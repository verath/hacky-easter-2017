# 16 - Pathfinder



> Can you find the right path?
> 
> hackyeaster.hacking-lab.com:9999

Using [httpie](https://github.com/jakubroztocil/httpie) we try visiting the
url provided:

```
C:\Users\Peter> http get hackyeaster.hacking-lab.com:9999
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 39
Content-Type: application/json; charset=utf-8
Date: Thu, 06 Apr 2017 20:37:55 GMT

{
    "Answer": "I only talk to PathFinder!"
}
```

It seems like the server will only talk to a PathFinder. Setting the User-Agent
header to `PathFinder` we get the following:

```
C:\Users\Peter> http get hackyeaster.hacking-lab.com:9999/1 User-Agent:PathFinder
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 63
Content-Type: application/json; charset=utf-8
Date: Tue, 06 Jun 2017 09:49:00 GMT

{
    "Answer": "Follow one of the possible paths",
    "paths": [
        1,
        3,
        5,
        8
    ]
}
```

Following one of the paths, we see that we get another set of paths...

```
C:\Users\Peter> http get hackyeaster.hacking-lab.com:9999/1 User-Agent:PathFinder
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 64
Content-Type: application/json; charset=utf-8
Date: Tue, 06 Jun 2017 09:49:33 GMT

{
    "Answer": "Go on! Follow one of the possible paths",
    "paths": [
        5
    ]
}
```

By writing a simple bruteforce solver ([pathfinder.py](./pathfinder.py)) we 
finally end up at the following:

```
C:\Users\Peter\Desktop\hacky-easter\16-Pathfinder>http get hackyeaster.hacking-lab.com:9999/157294683269358174843716529496583712528971346731642895972135468685427931314869257 User-Agent:PathFinder
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 576
Content-Type: application/json; charset=utf-8
Date: Thu, 06 Apr 2017 20:55:07 GMT

{
    "Answer": "Thanks PathFinder you saved my life by giving me the solution to this sudoku!",
    "Secret": "https://hackyeaster.hacking-lab.com/hackyeaster/images/challenge/egg16_UYgXzJqpfc.png",
    "sudoku": [
        [0,0,0,2,0,4,6,0,0],
        [2,0,9,0,0,0,0,0,0],
        [0,0,0,0,0,6,5,0,0],
        [0,0,6,5,0,0,7,1,0],
        [0,0,0,9,0,0,0,4,0],
        [7,3,1,0,0,0,0,0,0],
        [0,7,0,0,3,0,0,0,8],
        [0,8,0,0,2,7,0,3,1],
        [0,1,4,0,6,0,0,0,0]
    ],
    "your_solution": [
        [1,5,7,2,9,4,6,8,3],
        [2,6,9,3,5,8,1,7,4],
        [8,4,3,7,1,6,5,2,9],
        [4,9,6,5,8,3,7,1,2],
        [5,2,8,9,7,1,3,4,6],
        [7,3,1,6,4,2,8,9,5],
        [9,7,2,1,3,5,4,6,8],
        [6,8,5,4,2,7,9,3,1],
        [3,1,4,8,6,9,2,5,7]
    ]
}
```