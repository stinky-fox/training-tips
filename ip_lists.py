#!/bin/python

'''
Scripter: Stinky Fox
Version: 1
Purpose:
    Test usage only, not for production!
'''


import json
import requests
import sys


lName = sys.argv[2]
rIP = sys.argv[3]

instance = {}
instance['api_path'] ='type here'
instance['api_key'] = sys.argv[1]
instance['api_version'] = 'v1'


def getLists(listName,appendIP):

  apiPath = "/iplists/search"
  apiHeaders = {'Content-type': 'application/json', 'api-version': instance['api_version'], 'api-secret-key': instance['api_key']}
  apiInstance = instance['api_path'] + apiPath
  apiPayload = '{"maxItems":1,"searchCriteria":[{"fieldName":"name","stringValue":"' + listName + '"}]}'
  runApi = requests.post(apiInstance, data=apiPayload, headers=apiHeaders)
  converted = json.loads(runApi.content)
  ID = converted['ipLists'][0]['ID']
  oldIPs = converted['ipLists'][0]['items']
  oldIPs.append(appendIP)
  IPs = json.dumps(oldIPs)
  action = appendList(ID, IPs)
  return(action)

def appendList(ID,IPs):

  apiPath = "/iplists/" + str(ID)
  apiHeaders = {'Content-type': 'application/json', 'api-version': instance['api_version'], 'api-secret-key': instance['api_key']}
  apiInstance = instance['api_path'] + apiPath
  apiPayload = '{"items":' + IPs + '}'
  runApi = requests.post(apiInstance, data=apiPayload, headers=apiHeaders)

  if runApi.status_code == 200:
    message = "Status code: " + str(runApi.status_code) + ". IP List with ID: " + str(ID) + " was updated as follows - " + str(runApi.content)
  else:
    message = "Status code: " + str(runApi.status_code) + ". IP List with ID: " + str(ID) + " wasn't updated " + str(runApi.content)

  return(message)

print(getLists(lName,rIP))
