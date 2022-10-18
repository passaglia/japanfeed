changedetection.io -d data/ -h 127.0.0.1 -p 5000 &

sleep 10
open -na "Google Chrome" --args --incognito http://127.0.0.1:5000/