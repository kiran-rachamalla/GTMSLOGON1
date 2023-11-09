import singleton as sh
import json
import os
from json import JSONDecodeError

class CommentsHandle(metaclass=sh.SingletonMeta):
    def __init__(self):
        self.createDirectory()
        self.client_dtls = {}

    def createDirectory(self):
        dir = os.getenv('APPDATA') + '/GTMS_Logon'
        if not os.path.isdir(dir):
            os.mkdir(dir)
        file = dir + '/userdata.json'
        if not os.path.isfile(file):
         with open(file, 'w') as f:
             pass

    def fileLocationGet(self):
        return os.getenv('APPDATA') + '/GTMS_Logon' + '/userdata.json'

    def clienInfoGet(self):
        with open(self.fileLocationGet(), "r") as f:
            try:
                self.client_dtls = json.load(f)
            except JSONDecodeError:
                self.client_dtls = {}
        return self.client_dtls

    def system_client_details_get(self,system,client):
        if len(self.client_dtls) == 0:
            self.clienInfoGet()
        if system not in self.client_dtls:
            return
        for i, item in enumerate(self.client_dtls[system]):
            if item.get(client, None):
                return self.client_dtls[system][i][client]


    def clientInfoUpdate(self,system,client,username='',password='',comment=''):
        self.clienInfoGet()

        with open(self.fileLocationGet(), "w") as f:
            if system not in self.client_dtls:
                self.client_dtls[system] = []
            new_client = True
            for i, item in enumerate(self.client_dtls[system]):
                if item.get(client, None):
                    self.client_dtls[system][i][client] = {"username": username,"password":password,"comment":comment}
                    new_client = False
            if new_client:
                self.client_dtls[system].append({client: {"username": username,"password":password,"comment":comment}})

            json.dump(self.client_dtls, f)