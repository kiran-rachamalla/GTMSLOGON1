import requests
import base64
import json
import singleton as sh

class Github_handle(metaclass=sh.SingletonMeta):
    ACCESS_KEY = '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'
    USER = 'kiran-rachamalla'
    REPO_NAME = 'Sample_data'
    JSON_URL = 'https://api.github.com/repos/{USER}/{REPO_NAME}/contents/GTMSLogon/'

    def __init__(self):
        self.mt_system_data = []
        self.mt_server_details = {}

    def constructURL(self,user="404",repo_name="404",url="404"):
        url=url.replace("{USER}",user)
        url=url.replace("{REPO_NAME}",repo_name)
        return url

    def fecth_files(self):
        if not self.mt_system_data:
            response = requests.get(self.constructURL(self.USER, self.REPO_NAME, self.JSON_URL),
                                    headers={"Authorization":f"Bearer {self.ACCESS_KEY}"})

            if response.status_code == requests.codes.ok:
                for lwa_files in response.json():
                    file_data = requests.get(lwa_files["git_url"],
                                             headers={"Authorization": f"Bearer {self.ACCESS_KEY}"})
                    jsonResponse = file_data.json()
                    content = base64.b64decode(jsonResponse['content'])
                    jsonString = content.decode('utf-8')
                    self.mt_system_data.append(json.loads(jsonString))
        return self.mt_system_data

    def system_address_get(self,system):
        for i in self.mt_system_data:
            if i['INFOCUS']['SYSTEM_ID'] in system:
                return i['INFOCUS']['APL_SRVR']

    def server_details_fetch(self):
        if not self.mt_server_details:
            self.mt_server_details = requests.get('https://tmsapi.vistex.com/api/ApplicationServer/GetAllGcpSystems').json()
        return self.mt_server_details

    def server_details_get(self,system):
        self.server_details_fetch()
        for i in self.mt_server_details['data']:
            if i['sid'] in system:
                return (i['projectId'],i['guiServer'],i['zone'],i['instanceNo'])

    def is_system_gcloud_server(self,system):
        self.server_details_fetch()
        for i in self.mt_server_details['data']:
            if i['sid'] in system:
                return True