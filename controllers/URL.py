import falcon
import json
import logging as log
from config.config import dbsetup
from utils.helpers import FETCH_SHORT_URL, INSERT_SHORT_URL, _short_url


class ShortenedURL:

    def on_get(self, req, resp, url):
        try:
            db = dbsetup()
            cursor = db.cursor()
            cursor.execute(FETCH_SHORT_URL,(url,))
            data = cursor.fetchall()
            log.info("=============")
            log.info(data)
            details = {"urlDetails":data}

        except Exception as e:
            log.info(e)

        finally:
            db.close()

        resp.status = falcon.HTTP_200
        log.info(details)
        resp.body = (json.dumps(details))


class CreateShortURL:

    def on_post(self, req, resp):
        json_data = json.loads(req.stream.read())
        original_url = json_data["original_url"]
        details = on_post_data(original_url)
        resp.status = falcon.HTTP_200
        resp.body = (json.dumps(details))

def on_post_data(original_url):
    details = {}
    try:
        db = dbsetup()
        cursor = db.cursor()
        cursor.execute(FETCH_SHORT_URL,(original_url,))
        data = cursor.fetchall()
        if len(data) == 0:
            url = _short_url(original_url)
            print url
            cursor.execute(INSERT_SHORT_URL,(original_url,url,))
            db.commit()
        cursor.execute(FETCH_SHORT_URL,(original_url,))
        data = cursor.fetchall()
        print data
        details = {"ShortenedURL":data}
        print details

    except Exception as e:
        log.info(e)

    finally:
        db.commit()
        db.close()
    return details
"""
@mock.patch(config.config.dbsetup)
def test_on_post(self, mock_setup):

    mock_setup.reuturn_value = Mock()
    mock_setup.cursor.reuturn_value = Mock()
    mock_setup.cursor.execute.reuturn_value = Mock()
    mock_setup.cursor.cursor.fetchall.reuturn_value = ('4544')

"""

