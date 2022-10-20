python3 readme/readme.py

python3 changedetection/changedetection.py

python3 rss/opml.py

docker-compose -f ./rss/docker-compose.yml up -d 

changedetection.io -C -d changedetection/data/ -h 127.0.0.1 -p 5000 &

sleep 10

open -na "Google Chrome" --args --incognito http://127.0.0.1:5000/ http://127.0.0.1:8080/ 


## Make sure to launch docker from application folder first or else will get following error
## Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
## cf https://stackoverflow.com/questions/44084846/cannot-connect-to-the-docker-daemon-on-macos