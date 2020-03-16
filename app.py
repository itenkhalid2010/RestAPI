import  urllib
import json
import flask
from flask import render_template, request
from API import BaseAPI
from DataBase import OfflineData
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Global variable
INTERNETCONNECTION = False


@app.route('/', methods=["GET"])
def home():
   return"Welcome to Our simple API <br/> " \
         "to use our API please follow the following instruction <br/> " \
         "for specific country with all info please type localhost:5000/ and type the country name <br/>" \
         "for specific info about a specific country please type localhost:5000/ then add the country name then /info= and here add your specific info <br/>" \
         "for more than one info please type  localhost:5000/ then add the country name then /info= and here add your specific info , the second info"
@app.route('/<country>')
def ALLInfo(country=None):
        countryInfo = None
        baseAPI = BaseAPI()
        country =country
        if INTERNETCONNECTION:
         countryInfo =baseAPI.get_country_info(country)
        else:
            o = OfflineData()
            countryInfo = o.GetData(country)
        if countryInfo is not None:
                return countryInfo[0]
        else:
                return ("Not Found")
@app.route('/<country>/info=<specificInfo>')
def GetInfo(country=None,specificInfo=None):
    countryInfo = None
    baseAPI = BaseAPI()
    country = country
    countryInfo = baseAPI.get_country_info(country)
    specificInfo=specificInfo
    if countryInfo is not None:
        return str(countryInfo[0][specificInfo])
    else:
        return ("Not Found")
@app.route('/<country>/info=<specificInfo>,<specificInfo2>')
def GetInfo2(country=None,specificInfo=None,specificInfo2=None):
    countryInfo = None
    baseAPI = BaseAPI()
    country = country
    countryInfo = baseAPI.get_country_info(country)
    specificInfo=specificInfo
    specificInfo2=specificInfo2
    if countryInfo is not None:
        return str(specificInfo +"= "+str(countryInfo[0][specificInfo])+"\n "+specificInfo2+"= "+str(countryInfo[0][specificInfo2]))
    else:
        return ("Not Found")
def CheckInternetConnection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


if __name__ == '__main__':
    INTERNETCONNECTION = CheckInternetConnection()
    app.run(debug=True)