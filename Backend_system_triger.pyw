import subprocess
import sys
print(sys)
# f = open(r"C:\Users\kiran.rachamalla\PycharmProjects\GTMSLOGON\demofile2.txt", "w")
# f.write("Now the file has more content!"+"\n")
# f.write(str(sys.argv))
# for i,value in range(len(sys.argv)):
#     match i:
#         case 'projectId': projectId = i
#         case 'guiServer': guiServer = i
#         case 'zone': zone = i
#         case 'port':
#             port = i
#             f.write(port)
#     f.write(i+"\n")
# f.write("sucess")
# try:
#     f.write(type(sys.agrv[1]))
# except:
#     f.write('error raised121')
# finally:
#     f.write('good')
# #
# # f.write(type(projectId))
# # guiServer = sys.argv[3]
# # zone = sys.argv[4]
# # port = sys.argv[5]
# # f.write(f"so {projectId}")
# f.write("sucess1")
# #+ {guiServer}+ {zone}+{port}")
# f.close()
if sys.argv[1] == "NONCLOUD":
    subprocess.Popen(["cmd", "/c", f"Sapgui {sys.argv[2]} 00"],
                 shell=True,
                 cwd="C:\Program Files (x86)\SAP\FrontEnd\SAPgui")
elif sys.argv[1] ==  "STARTSERV":
    # f = open(r"C:\Users\kiran.rachamalla\PycharmProjects\GTMSLOGON\demofile2.txt", "w")
    # f.write("Now the file has more content good!"+"\n")
    # f.write(str(sys.argv))
    projectId = sys.argv[2]
    guiServer = sys.argv[3]
    zone = sys.argv[4]
    instance_no = sys.argv[5]

    # for i in range(len(sys.argv)):
    #     match i:
    #         case 2:
    #         case 3:
            #         case 'zone':  = i
            #         case '':
            #             port = i
            #             f.write(port)
        # f.write(str(i) + str(projectId) +str(type(sys.argv[i])))
    # f.write(str(projectId)+str(guiServer)+str(port))
    # f.write(f"gcloud compute start-iap-tunnel {guiServer} 3200 --project={projectId}" \
    #                 f" --local-host-port=localhost:{port} --zone={zone}")
    # f.close()
    # (projectId,guiServer,zone,port) = (sys.agrv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    # f = open(r"C:\Users\kiran.rachamalla\PycharmProjects\GTMSLOGON\demofile2.txt", "w")
    # f.write("Now the file has more content!")
    # f.close()
    subprocess.run(['cmd', "/c",
                    f"gcloud compute start-iap-tunnel {guiServer} 3200 --project={projectId}" \
                    f" --local-host-port=localhost:32{instance_no} --zone={zone}"],
                   shell=True)
    # subprocess.run(['cmd', "/c",
    #                 f"gcloud compute start-iap-tunnel {guiServer} 3200 --project={projectId}" \
    #                 f" --local-host-port=localhost:{port} --zone={zone}"],
    #                shell=True)
elif sys.argv[1] == 'OPENSERVINST':
    f = open(r"C:\Users\kiran.rachamalla\PycharmProjects\GTMSLOGON\demofile2.txt", "w")
    f.write("Now the file has more content horrrayyyyyyyyy!"+"\n")
    f.close()
    subprocess.Popen(["cmd", "/c", f"Sapgui localhost {sys.argv[2]}"],
                     shell=True,
                     cwd="C:\Program Files (x86)\SAP\FrontEnd\SAPgui")
elif sys.argv[1] == 'STOPSERV':
    # f = open(r"C:\Users\kiran.rachamalla\PycharmProjects\GTMSLOGON\demofile2.txt", "w")
    # f.write("Now the file has more content stop!" + "\n")
    # f.close()
    lv_command = '''for /f "tokens=2,5 delims= " %p in ('netstat -ano ^| findstr 127.0.0.1:3201') do ( if %p == 127.0.0.1:3201 ( taskkill /pid %q /f & exit ) )'''
    subprocess.run(lv_command, shell=True)
    # subprocess.Popen(["cmd", "/c", f'''for /f "tokens=2,5 delims= " %p in ('netstat -ano ^| findstr 127.0.0.1:3201') do ( if %p == 127.0.0.1:3201 ( taskkill /pid %q /f & exit ) ) '''],
    #                  shell=True,
    #                  cwd="C:\Program Files (x86)\SAP\FrontEnd\SAPgui")