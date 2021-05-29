import glob
import time
import xml.etree.cElementTree as ET
import matplotlib.pyplot as plt

my_time = time.localtime()
string_time = time.strftime("%H:%M")
print(string_time)
start = int(string_time[3:5])-2
call = []
byte = []
listt = []
fig = plt.figure()
ax = fig.add_subplot(111)
while True:
    path = '/usr/local/freeswitch/log/xml_cdr/*.xml'
    files=glob.glob(path)
    for file in files:
        if file not in listt:
            #print(file[34:len(file)])
            path2 = file
            tree = ET.ElementTree(file=path2)
            root = tree.getroot()
            for tag1 in root:
                for tag2 in tag1:
                    if (tag2.tag=='application'):
                        if (tag2.get('app_name')=='record_session'):
                            name =  tag2.get('app_data')
                            name =  name[44:len(name)]
                    for tag3 in tag2:
                        for tag4 in tag3:
                            if (tag4.tag=='media_bytes' and tag3.tag=='inbound'):
                                data = tag4.text
            timeh = name[0:2]
            timem = name[3:5]
            callr = name[9:13]
            callt = name[14:18]
            if (start == int(timem)):
                listt.append(path2)
                count = 0
                if (callr in call):
                    for c in call:
                        if (callr == c):
                            byte[count] = byte[count]+int(data)
                        count = count+1
                count = 0
                if (callt in call):
                    for c in call:
                        if (callt == c):
                            byte[count] = byte[count]+int(data)
                        count = count+1
                if (callr not in call):
                    call.append(callr)
                    byte.append(int(data))
                if (callt not in call):
                    call.append(callt)
                    byte.append(int(data))
                #byte[0] = byte[0]+int(data)
                #byte[1] = byte[1]+int(data)
            ax.bar(call,byte,color='blue')
            fig.show()
            plt.pause(0.05)
    my_time = time.localtime()
    timeu = time.strftime("%H:%M")
    print('update at time '+ timeu[0:2]+':'+str(int(timeu[3:5])-2))
    print('total data '+str(sum(byte))+' (byte)')
    time.sleep(60)
    start = start+1
