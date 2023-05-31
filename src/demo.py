import api.CountItAPI as CountItAPI
import datetime

token=input("Enter your token: ")
api=CountItAPI.API(token=token)
stepCount=input("Enter amount of steps taken: ")
api.setEntry(stepCount,datetime.datetime.today())