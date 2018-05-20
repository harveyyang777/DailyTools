#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import argparse
import iosUtils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', type=str, help='input the command')

    args = parser.parse_args()
    command = args.command


    if command == 'shoot':
        print('get screenshot')
        iosUtils.get_screen_shot()
    elif command == 'info' :
        print('get device info')
    elif command == 'clear':
        iosUtils.clear_images()
    else:
        print('not supprted')
        iosUtils.get_uuid()

