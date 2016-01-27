import unittest
import re
from datetime import datetime
import requests
import json
import logging as log
import mock
from mock import Mock, MagicMock
from config.config import dbsetup
from controllers import URL
from controllers.URL import CreateShortURL


class TestDateQuery(unittest.TestCase):

	def setUp(self):
		self.url = "http://localhost:8000/createShortURL"
		self.headers = {'content-type':'application/json'}
		print "******************TestCase Execution Started*********************"

		"""
		Test whether wrong email is handled well.
		in this case server should respond with correct error message.
		"""
		
	def test(self):
		payload = {"original_url":"http://www.holidayiq.com/blog/8-offbeat-destinations-in-south-india-you-should-check-out-this-year-1847.html?dvhbcnmsfbm"}
		resp = requests.post(self.url, data = json.dumps(payload), headers = self.headers)
		self.assertEqual(200,resp.status_code)
		print dir(resp.json)
		data = json.loads(resp.content)
		print data

	def tearDown(self):
		print "******************TestCase Execution Completed*********************"

class Test(unittest.TestCase):
	def setUp(self):
		self.dbsetup = Mock()
		self.on_post_dta = URL.on_post_data
		URL.on_post_data = MagicMock()
		URL.on_post_data.return_value = {"ShortenedURL":"http://tinyurl.com/zmlyyuo"}
		self.original_url = "http://www.holidayiq.com/blog/8-offbeat-destinations-in-south-india-you-should-check-out-this-year-1847.html?dvhbcnmsfbm"
		self.data = {"ShortenedURL":"http://tinyurl.com/zmlyyuo"}

	def test_case(self):
		print "*********entered********** "
		result = CreateShortURL.on_post(CreateShortURL(),req,resp)
		self.assertEqual(result,self.data)

	def tearDown(self):
		on_post_data = self.on_post_dta

if __name__ == "__main__":
	unittest.main()  
