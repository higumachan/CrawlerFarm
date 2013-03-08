#coding: utf-8

import sys
import os

COMMANDS = ["deploy"];

def exec_command(command):
    if command not in COMMANDS:
        if command == "deploy":
            deploy(sys.argv[2:]);

def deploy(args):
    os.system("scp -r . root@jigoq.com:/var/CrawlerServer/crawlers");

if __name__ == '__main__':
    
    if (len(sys.argv) == 0):
        print u"""
        説明
        """
    else:
        command = sys.argv[1];
        
