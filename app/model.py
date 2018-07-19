import json
import requests
import psycopg2
import urllib.parse as urlparse
import os
from app import db

# class Region(object):
#     """docstring for UserFunctions"""
#     def __init__(self):
#         super(Region, self).__init__()

#     def getTouristSiteWeather(self,city):
#         print(city)
#         if city!="":
#             url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric"+ "&APPID=e2cd7d4ec205a87e9fedc5b591cedd72"
#             result = requests.get(url)
#             result = json.loads(result.text)
#             weather_data = {
#                 'temp': result['main']['temp'],
#                 'humidity': result['main']['humidity']
#             }
            

#             return weather_data
    

#     def getTouriteSiteByRegion(self,data):
#         conn = ""
#         out = []
#         try:
#             url = urlparse.urlparse(os.environ['DATABASE_URL'])
#             dbname = url.path[1:]
#             user = url.username
#             password = url.password
#             host = url.hostname
#             port = url.port
#             conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
#         except:
#             out = {"err": "Unable to connect to the database"}
#         try:
#             cur = conn.cursor()
#             cur.execute("""SELECT * from tbl_tourist_site where region_shortname = '{0}'""".format(data['region_shortname']))
#             rows = cur.fetchall()
         
#             data = []
#             for row in rows:
#                 data.append({ "id": row[0], "tourist_site_name": row[1], "tourist_site_image": row[2], "tourist_alt_name": row[3], "region_shortname": row[4], "tourist_site_description": row[5] })
          
#             if data == []:
#                 out = {'code': '01', 'msg': 'Failed to retrieve data', 'data': [] }
#             else:
#                 out = { 'code': '00', 'msg': 'Data Retrieved Successfully', 'data': data }
#         except:
#             out = {"err": "General SQL Error"}
#         return json.dumps(out)

#     def getTouriteSiteById(self,data):
#         conn = ""
#         out = []
#         try:
#             url = urlparse.urlparse(os.environ['DATABASE_URL'])
#             dbname = url.path[1:]
#             user = url.username
#             password = url.password
#             host = url.hostname
#             port = url.port
#             conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
#         except:
#             out = {"err": "Unable to connect to the database"}
#         try:
#             cur = conn.cursor()
#             cur.execute("""SELECT * from tbl_tourist_site where id = '{0}'""".format(data['id']))
#             rows = cur.fetchall()
#             data = []
#             for row in rows:
#                 data.append({
#                     "id": row[0], 
#                     "tourist_site_name": row[1],
#                     "tourist_site_image": row[2], 
#                     "tourist_alt_name": row[3],
#                     "region_shortname": row[4], 
#                     "tourist_site_description": row[5] })
            
#             if data != []:
#                 # weather_data = weather.getTouristSiteWeather(data['city'])
#                 out = {
#                     'code':'00',
#                     'msg':'Data Retrieved Successfully',
#                     #'weather':weather_data,
#                     'data':data }
#             else:
#                 out = {
#                     'code':'01',
#                     'msg':'Failed to retrieve data',
#                     'data':[] }
#         except:
#             out = {"err": "General SQL Error"}
#         return json.dumps(out)






class Region(db.Model):
    __tablename__ = "tourist_site"
    id = db.Column(db.Integer, primary_key=True)
    tourist_site_name = db.Column(db.String(120), unique=True)
    tourist_site_image = db.Column(db.String(120), unique=True)
    tourist_alt_name = db.Column(db.String(120), unique=True)
    region_shortname = db.Column(db.String(120), unique=True)
    tourist_site_description = db.Column(db.String(120), unique=True)

    def __init__(self, tourist_site_name,tourist_site_image,tourist_alt_name,region_shortname,tourist_site_description):
        self.tourist_site_name = tourist_site_name,
        self.tourist_site_image = tourist_site_image
        self.tourist_alt_name = tourist_alt_name
        self.region_shortname = region_shortname
        self.tourist_site_description = tourist_site_description



    def getTouristSiteWeather(self,city):
        print(city)
        if city!="":
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric"+ "&APPID=e2cd7d4ec205a87e9fedc5b591cedd72"
            result = requests.get(url)
            result = json.loads(result.text)
            weather_data = {
                'temp': result['main']['temp'],
                'humidity': result['main']['humidity']
            }
            

            return weather_data
    

    def getTouriteSiteByRegion(self,data):
        
        try:
            
            result = query.filter_by(region_shortname = '{0}'.format(data['region_shortname'])).all()
            db.session.commit()
            print("Printing data from db")
            print(result)
            # data = []
            # for row in rows:
            #     data.append({ "id": row[0], "tourist_site_name": row[1], "tourist_site_image": row[2], "tourist_alt_name": row[3], "region_shortname": row[4], "tourist_site_description": row[5] })
          
            if result == []:
                out = {'code': '01', 'msg': 'Failed to retrieve data', 'data': [] }
            else:
                out = { 'code': '00', 'msg': 'Data Retrieved Successfully', 'data': result }
        except:
            out = {"err": "General SQL Error"}
        return json.dumps(out)

    def getTouriteSiteById(self,data):
        
        
        try:
            
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
                # weather_data = weather.getTouristSiteWeather(data['city'])
                out = {
                    'code':'00',
                    'msg':'Data Retrieved Successfully',
                    #'weather':weather_data,
                    'data':data }
            else:
                out = {
                    'code':'01',
                    'msg':'Failed to retrieve data',
                    'data':[] }
        except:
            out = {"err": "General SQL Error"}
        return json.dumps(out)





# if __name__ == '__main__':
#     weather = Region()

#     city = 'accra'
#     weather_data = weather.getTouristSiteWeather(city)
#     print("Printing weather condition")
#     print(weather_data)

