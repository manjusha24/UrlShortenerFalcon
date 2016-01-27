import uuid
import contextlib
from urllib import urlencode
from urllib2 import urlopen
import sys 


def _generate_id():
    return str(uuid.uuid4())

def _short_url(url):
	request_url = ('http://tinyurl.com/api-create.php?' + 
    				urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

FETCH_SHORT_URL = "SELECT * FROM URLTABLE where original_url = %s"
INSERT_SHORT_URL = "INSERT INTO URLTABLE(original_url,shortened_url) values(%s,%s)"