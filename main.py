import json
import subprocess

from flask import Flask,render_template, request
import webview as wb
import Github_handle as gh
import LocalFileHandler as LFH

app = Flask(__name__)

@app.route('/open_sap_gui', methods=['GET'])
def background_process_test():
    if request.args["action"] == "START":
        (projectId, guiServer, zone, instance_no) = gh.Github_handle().server_details_get(request.args["system"])
        # subprocess.run(['cmd', "/c",
        #                 f"gcloud compute start-iap-tunnel {guiServer} 3200 --project={projectId}" \
        #                 f" --local-host-port=localhost:{port} --zone={zone}"],
        #                shell=True)
        subprocess.Popen(f'start pythonw.exe Backend_system_triger.pyw "STARTSERV" '
                         f'{projectId} {guiServer} {zone} {instance_no}', shell=True)
    elif request.args["action"] == "STOP_SERVER":
        (projectId, guiServer, zone, instance_no) = gh.Github_handle().server_details_get(request.args["system"])
        subprocess.Popen(f'start pythonw.exe Backend_system_triger.pyw "STOPSERV" '
                         f'{instance_no}', shell=True)
    else:
        if gh.Github_handle().is_system_gcloud_server(request.args["system"]):
            (projectId, guiServer, zone, instance_no) = gh.Github_handle().server_details_get(request.args["system"])
            subprocess.Popen(f'start pythonw.exe Backend_system_triger.pyw "OPENSERVINST" '
                             f'{instance_no}', shell=True)
        else:
            subprocess.Popen(f'start pythonw.exe Backend_system_triger.pyw "NONCLOUD" ' 
                        f'{gh.Github_handle().system_address_get(request.args["system"])}', shell=True)
    return json.dumps(request.args['system'])

@app.route('/')
def main():
    return render_template('main.html',
                           The_title='Main Page',
                           the_content = gh.Github_handle().fecth_files())

@app.route('/update_client_info',methods=['GET'])
def client_info_update():
        LFH.CommentsHandle().clientInfoUpdate(request.args["system"],request.args["client"],
                                              request.args["username"],request.args["password"],
                                              request.args["comment"])
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.context_processor
def my_utility_processor():

    def Username_get(system,client):
        return local_details_get(system, client, 'username')

    def password_get(system,client):
        return local_details_get(system, client, 'password')

    def comment_get(system,client):
        return local_details_get(system,client,'comment')

    def local_details_get(system,client,keyword):
        client_info = LFH.CommentsHandle().system_client_details_get(system, client)
        if client_info:
            return client_info[keyword]
        else:
            return str()

    return dict(Username_get=Username_get, password_get=password_get, comment_get=comment_get)

if __name__ == '__main__':
    wb.create_window(title='GTMS Logon', url=app)
    #wb.start()
    wb.start(debug=True)