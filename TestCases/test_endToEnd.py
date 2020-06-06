import requests
import jsonpath
import json


def test_Add_newStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\Chandu\\Desktop\\StudentData.json", 'r')
    request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    print("New Student Details :", response.text)
    get_id = jsonpath.jsonpath(response.json(), 'id')
    print(get_id[0])

    tech_details_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open("C:\\Users\\Chandu\\Desktop\\TechnicalDetails.json", 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(get_id[0])
    request_json['st_id'] = get_id[0]
    print(request_json)
    response = requests.post(tech_details_url, request_json)
    print("Technical Details: ", response.text)

    get_tech_details = "http://thetestingworldapi.com/api/technicalskills/"+str(get_id[0])
    response = requests.get(get_tech_details)
    print(response.text)

    # address_url = "http://thetestingworldapi.com/api/addresses"
    # file1 = open("C:\\Users\\Chandu\\Desktop\\Address.json", 'r')
    # request_json1 = json.loads(file1.read())
    # response = requests.post(address_url, request_json1)
    # print("Addresss :", response.text)
    #
    # final_details_url = "http://thetestingworldapi.com/api/FinalStudentDetails/269047"
    # response = requests.get(final_details_url)
    # print("Final Details :", response.text)
