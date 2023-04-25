# besthack

This is a repo for the semifinal of BEST Hack at the Bauman MSTU

***

## Installation and running

<ins>**1. Download the repository:**</ins>

```
git clone https://github.com/Ronningen/besthack
```

<ins>**2. Run the server:**</ins>

```
cd web
python3 server.py
```

<ins>**3. Open the web page:**</ins>

http://localhost:8000/main.html

## Issues

Issue:
>Error code 403.
>
>Message: CGI script is not executable ('/cgi-bin/main.py').
>
>Error code explanation: 403 = Request forbidden -- authorization will not help.

Solution:
```
chmod a+x cgi-bin/main.py
```