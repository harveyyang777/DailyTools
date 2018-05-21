#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import time
import chardet

def get_uuid():
    #os.system('idevice_id --list')
    uuid = os.popen('idevice_id --list').readline()
    print(uuid)
    return uuid


def get_kwai_bundleID():
    bundle_IDs= os.popen('ideviceinstaller -l | grep \"kwai\"').readlines()
    id_list =[]
    for id in bundle_IDs:
        print(id[:-3])
        id_list.append(id.split('-')[0])
    return id_list

def get_bundleID():
    #results = os.popen('ideviceinstaller -l | grep \"gifshow\"', 'r')
    os.system('ideviceinstaller -l | grep \"gifshow\" >tmp.txt')
    with open('tmp.txt', 'r', encoding='utf-8') as f:
        #print(chardet.detect(f.read()))
        results = f.readlines()
    print(results[0])
    os.system('rm tmp.txt')
    return results[0]



def get_screen_shot():
    path = os.getcwd()
    usr_path = path.split('/')[2]
    dst_path = '/'+path.split('/')[1]+'/'+path.split('/')[2]+'/'+'Desktop/'
    file_time =time.strftime("%Y-%m-%d__%H-%M-%S",time.localtime())
    file_name = dst_path+file_time+'.png'
    print(file_name)
    os.system('idevicescreenshot '+file_name)
def clear_images():
    os.popen('rm  ~/Desktop/*.png')

if __name__ == '__main__':
    print(0)
  #  get_uuid()
   # print(sys.getdefaultencoding())
   # get_bundleID()
