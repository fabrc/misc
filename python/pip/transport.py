import os
import xmlrpclib

class Transport(xmlrpclib.SafeTransport):

    def make_connection(self, host):

	proxy = os.getenv("http_proxy")
	if proxy:
	    if proxy.startswith("http://"):
		proxy = proxy[len("http://"):]
	    try:
		proxy = proxy[:proxy.index('/')]
	    except:
		pass

	    conn = xmlrpclib.SafeTransport.make_connection(self, proxy)
	    conn.set_tunnel(host)
	else:
	    conn = xmlrpclib.SafeTransport.make_connection(self, host)
	return conn
