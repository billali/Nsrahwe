import json
import psycopg2
import urllib.parse as urlparse
import os

class Region(object):
    """docstring for UserFunctions"""
    def __init__(self):
        super(Region, self).__init__()
    

    def getTouriteSiteByRegion(self,data):
        conn = ""
        out = []
        try:
            url = urlparse.urlparse(os.environ['DATABASE_URL'])
            dbname = url.path[1:]
            user = url.username
            password = url.password
            host = url.hostname
            port = url.port
            conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        except:
            out = {"err": "Unable to connect to the database"}
        try:
            cur = conn.cursor()
            cur.execute("""SELECT * from tbl_tourist_site where region_shortname = '{0}'""".format(data['region_shortname']))
            rows = cur.fetchall()
         
            data = []
            for row in rows:
                data.append({ "id": row[0], "tourist_site_name": row[1], "tourist_site_image": row[2], "tourist_alt_name": row[3], "region_shortname": row[4], "tourist_site_description": row[5] })
          
            if data == []:
                out = {'code': '01', 'msg': 'Failed to retrieve data', 'data': [] }
            else:
                out = { 'code': '00', 'msg': 'Data Retrieved Successfully', 'data': data }
        except:
            out = {"err": "General SQL Error"}
        return json.dumps(out)

    def getTouriteSiteById(self,data):
        conn = ""
        out = []
        try:
            url = urlparse.urlparse(os.environ['DATABASE_URL'])
            dbname = url.path[1:]
            user = url.username
            password = url.password
            host = url.hostname
            port = url.port
            conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        except:
            out = {"err": "Unable to connect to the database"}
        try:
            cur = conn.cursor()
            cur.execute("""SELECT * from tbl_tourist_site where id = '{0}'""".format(data['id']))
            rows = cur.fetchall()
            data = []
            for row in rows:
                data.append({
                    "id": row[0], 
                    "tourist_site_name": row[1],
                    "tourist_site_image": row[2], 
                    "tourist_alt_name": row[3],
                    "region_shortname": row[4], 
                    "tourist_site_description": row[5] })
            if data != []:
                out = {
                    'code':'00',
                    'msg':'Data Retrieved Successfully',
                    'data':data }
            else:
                out = {
                    'code':'01',
                    'msg':'Failed to retrieve data',
                    'data':[] }
        except:
            out = {"err": "General SQL Error"}
        return json.dumps(out)
  
