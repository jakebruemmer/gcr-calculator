import requests
from bs4 import BeautifulSoup

class GCRCalculator:

    def __init__(self):
        self.GCR_CALCULATOR_URL = "http://www.gcmap.com/dist?P=%s&DU=%s&DM=&SG=&SU=%s"
        self.__values = {
            'SU': ['mph', 'kph'],
            'DU': ['mi', 'km']
        }

    def calculate_distance(self, orig, dest, distance_unit, speed_unit):
        if distance_unit not in self.__values['DU'] or speed_unit not in self.__values['SU']:
                raise ValueError('You must supply the following values for distance and speed %s' % str(self.__values))

        req_url = self.GCR_CALCULATOR_URL % (orig + '-' + dest, distance_unit, speed_unit)
        soup = BeautifulSoup(requests.get(req_url).content, 'html.parser')
        dist = int(soup.find(id='mdist').find_all('tr')[1].td.string.strip(' ' + distance_unit).replace(',', ''))

        return {'orig': orig, 'dest': dest, 'distance_unit': distance_unit, 'distance': dist}

