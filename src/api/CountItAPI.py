
import datetime
import json
import requests


class API():
    
    def __init__(self, token):
        '''token: the citoken cookie value from logging in to the count.it website'''
        self.headers = {
            'Content-type': 'application/json; charset=utf-8', 
            'Accept': 'application/json, text/plain', 
            "Accept-Encoding": "gzip", 
            "Cookie":"citoken=" + token
            }
    

    def setEntry(self, stepCount, date:datetime.date, source="google"):
        site="https://www.countit.com/mobile_api/post_measurements"
        measurement={
            "measurements":[
            {
                "source": source,
                "value": stepCount,
                "units": "steps",
                "activity": "walk",
                "date": date.strftime("%Y/%m/%d")
            }],
            "provider":"google"
        }

        r=requests.post(site, data=json.dumps(measurement), headers=self.headers)

    def getDiary(self):
        site="https://www.countit.com/mobile_api/diary_entries"
        return requests.get(site, self.headers)


    