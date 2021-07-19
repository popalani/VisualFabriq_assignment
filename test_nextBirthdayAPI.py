import requests
import datetime
import pytest
from datetime import datetime
 
@pytest.fixture 
def calculateNextBirthday():
    year = int(1990)
    month = int(10)
    day = int(30)
    birthday = datetime(year,month,day)
    now = datetime.now()
    #find birthday for current year
    delta1 = datetime(now.year, birthday.month, birthday.day)
    delta2 = datetime(now.year+1, birthday.month, birthday.day)    
    nextBirthdays_inDays = ((delta1 if delta1 > now else delta2) - now).days +1
    return nextBirthdays_inDays
    
    
def test_Unit_IsDay(calculateNextBirthday):
     response = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=day")
     response_body = response.json() 
     #save only the  value-x days left from key-message 
     actualValue = response_body["message"]
     #verify expected equals actual
     assert (str(calculateNextBirthday)+" days left") == actualValue
     
def test_Unit_IsWeek(calculateNextBirthday):
     response = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=week")
     response_body = response.json() 
     #save only the  value-x days left from key-message
     actualValue = response_body["message"]
     #compute expected value in weeks
     expectedValue = int((calculateNextBirthday)/7)
     #verify expected equals actual 
     assert (str(expectedValue)+" weeks left") == actualValue
     
def test_Unit_IsMonth(calculateNextBirthday):
     response = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=month")
     response_body = response.json() 
     #save only the  value-x days left from key-message
     actualValue = response_body["message"]
     #compute expected value in months
     expectedValue = int((calculateNextBirthday)/30)
     #verify expected equals actual 
     assert (str(expectedValue)+" months left") == actualValue
     
def test_valid_dob_unit_isHour(calculateNextBirthday):
     response = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=hour")
     response_body = response.json() 
     #save only the  value-x days left from key-message
     actualValue = response_body["message"]
     #compute expected from input parameter
     expectedValue = int((calculateNextBirthday)*24)
     #verify expected equals actual 
     assert (str(expectedValue)+" hours left") == actualValue
     
def test_InvalidCase_DOBFormat_IsIncorrect_Unit_IsCorrect():
     response = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=-10-30&unit=month")
     response_body = response.json() 
     #save only the  value-x days left from key-message
     actualValue = response_body["message"]
     expectedValue = "Please specify dateofbirth in ISO format YYYY-MM-DD"
     #verify expected equals actual 
     assert  str(expectedValue) == str(actualValue) 
     
def test_InvalidCase_DOB_IsEmpty_Unit_IsEmpty():
     response = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=&unit=")
     response_body = response.json() 
     #print the value of key- 104 days left
     actualValue = response_body["message"]
     expectedValue = "Please specify both query parameter dateofbirth and unit"
     #verify expected equals actual 
     assert  str(expectedValue) == str(actualValue)
     
def test_InvalidCase_DOB_IsCorrect_Unit_IsEmpty():
     response = requests.get("https://p9fwi1d77e.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=")
     response_body = response.json() 
     #print the value of key- 104 days left
     actualValue = response_body["message"]
     expectedValue = "Please specify both query parameter dateofbirth and unit"
     #verify expected equals actual 
     assert  str(expectedValue) == str(actualValue)