# cookie-bypass
The main purpose is to allow external devices to share their state, better saying,
their cookie, with a configured gateway. It's a bit like a hack!

### example
You are browsing some ecommerce and choosing a lot of stuff on your cellphone.
When you are done of putting everything on the cart, you realize the only way
you can finish the shopping is to do it on your home computer. Plus for any
reason you are not able to synchronize the cart using your login. This is a very
strange scenario which may happen, and generally HTTP cookies hold enough
information to get your cart back.
#### how it works
The idea is the very basic concept of how HTTP cookie works. When you access some
site it ask you to store a cookie with a random value, and with this the remote
server is able to track you. So whenever you access that site again, you send
in the request your cookies on the header "Cookie".

This is very straightforward, but the big deal is to impersonate the client device
to send his cookies to our server. Looking back again some concepts, the HTTP
client implementation, the cookies are assigned to the hostname where it was
created. This means that when you access "google.com", you will only send cookies
where "google.com" server had ask you to create them.

Now we just have to make the client resolve the name of the desired site to the
IP address of your gateway.

### gateway
The gateway machine will be also the web server and the DNS server. The only
restriction here is that the external device be in the same LAN of the gateway,
or your gateway has an static IP.

#### web server
It will run Nginx, with a virtual server as being the target site web server,
then proxying the request to a local server which will interpret incoming requests
and opening firefox browser at the target site with cookies already loaded.

#### DNS server
It will run Dnsmasq, resolving the target site name to the gateway IP address.
With this we can impersonate who try to reach that site through us.

Getting back to the example, and with the core concepts in mind we can solve this
puzzle. I will show only one resolution here, besides it has many.
First we need to put both gateway and client on the same LAN, and for this we
create an access point because this is the easiest setup. The access point also
restrict other users from accessing your environment, which is good. Now the
web server and DNS server should be configured.

For this example, we take this information as our environment:
- gateway IP: 10.0.0.1/24
- site name: https://rockcity.it

Then we execute this commands as ROOT:
```shell
./bin/install 10.0.0.1 rockcity.it
```

If everything was ok, continue as NON-ROOT (you can run with root, but is not recommended):
```shell
./bin/start_proxy
```

The install script put everything in place, web server and DNS configuration,
and the start_proxy script will start and hang on the python proxy server.

Now our gateway is up and running, we have to connect the client to our LAN through
the access point, and access that target site in the browser! When you do that
you will see a blank page on the client browser, but on the gateway, a firefox
window will be loaded with the target site and after a few seconds with everything
previously on the client side.

More docs comming soon...  
