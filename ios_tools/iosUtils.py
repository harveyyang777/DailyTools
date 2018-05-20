#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

import os
import time
def get_uuid():
    #os.system('idevice_id --list')
    uuid=os.popen('idevice_id --list').readline()
    print(uuid)
    return uuid


def get_kwai_bundleID():
    bundle_IDs= os.popen('ideviceinstaller -l | grep \"kwai\"').readlines()
    id_list =[]
    for id in bundle_IDs:
        print(id[:-3])
        id_list.append(id.split('-')[0])
    return id_list

def get_screen_shot():
    path = os.getcwd()
    usr_path = path.split('/')[2]
    dst_path = '/'+path.split('/')[1]+'/'+path.split('/')[2]+'/'+'Desktop/'
    file_time =time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
    file_name = dst_path+file_time+'.png'
    print(file_name)
    os.system('idevicescreenshot '+file_name)
def clear_images():
    os.popen('rm  ~/Desktop/*.png')

#get_uuid()
#get_kwai_bundleID()
#get_screen_shot()
#clear_images()