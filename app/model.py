from app.libs.mysqllib import MysqlLib
import os

class Region(object):
    """docstring for UserFunctions"""
    def __init__(self):
        super(Region, self).__init__()
        self.dbconn = MysqlLib()

    def getTouriteSiteByRegion(self,data):
    	data = self.dbconn.select_from_table("tbl_tourist_sites", condition="where region_shortname = '{0}'".format(data['region_shortname']))
    	if data!= []:
    		
    		data = {
    			'code':'00',
    			'msg':'Data Retrieved Successfully',
    			'data':data
    		}
    		

    		return data
    	else:
    		data = {
    			'code':'01',
    			'msg':'Failed to retrieve data',
    			'data':[]
    		}
    		return data


    def getTouriteSiteById(self,data):
    	data = self.dbconn.select_from_table("tbl_tourist_sites", condition="where id = '{0}'".format(data['id']))
    	if data!= []:
    		data = {
    			'code':'00',
    			'msg':'Data Retrieved Successfully',
    			'data':data
    		}
    		return data
    	else:
    		data = {
    			'code':'01',
    			'msg':'Failed to retrieve data',
    			'data':[]
    		}
    		return data

  