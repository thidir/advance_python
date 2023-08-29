import requests
def Messageme():

    event_name = "send an email"


    api_key = "eJix5ABylAwAJ7HfDKCyEQ--nnToJR8wSdWaY-4OQrr"


    #create url

    url = f"https://maker.ifttt.com/trigger/{event_name}/json/with/key/{api_key}"

    json_data = {"value1": "Tawfeeq","value2": "hey"}


    response = requests.post(url,json_data)

    if response.status_code == 200:
        print("requests sent successfully")
    else:
        print("requests failed!!!")


