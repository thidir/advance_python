from gpiozero import Button
# from signal import pause
import requests
# from gpiozero import LED
# redLed = LED
# redLed.on(1)
# print ("Button was pressed")
# print ("light is on")

class notnotify:
    def __init__(self,event_name,api_key,json_data = None):
        self.event_name = event_name
        self.api_key = api_key

    def notify(self,json_data={}):

        


    # def Messageme():
    

        # event_name = "send an email"


        # api_key = "eJix5ABylAwAJ7HfDKCyEQ--nnToJR8wSdWaY-4OQrr"


        #create url

        url = f"https://maker.ifttt.com/trigger/{self.event_name}/json/with/key/{self.api_key}"

        # json_data = {"value1": "Tawfeeq","value2": "hey"}


        try:
            print("sending")
            response = requests.post(url,json_data)

            if response.status_code == 200:
                print("requests sent successfully")
            else:
                print("requests failed!!!")

            # button.when_pressed =  notnotify
            
        except:    
            print("not sent")