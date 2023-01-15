# simple-chat
A simple Chat with fast api

run Fastapi.py on a server
if you are using windows server just do this things befor u run the fastapi

  run netsh as run as adminstrator 
##run this command :
  advfirewall firewall add rule name="Open Port 5000" dir=in action=allow protocol=TCP localport=5000
##and this
  interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=5000 connectaddress=127.0.0.1 connectport=5000

this jobs forward the local port that fast api running on that to public address

  after that run the fastapi.py

  and run user's on another pc without any config
