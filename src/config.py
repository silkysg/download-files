#!/usr/bin/env python 
"""
Create and manage the INI file 
"""
import os, sys 
import json
import shelve 
import configparser 

#config = None 

def getprofileini():
    """
    Full path of the INI file
    """
    profileini = os.path.expanduser('~/.downloadfiles.ini')
    return profileini

def init(show=False):
    """
    Initialize the INI file
    """
    config = None
    
    profileini = getprofileini()    
    if os.path.exists(profileini):
       # print(os.path.dirname(profileini))
        config = configparser.ConfigParser()    
        config.read(profileini)
        if show: 
            for source in config: 
                for k in config[source]: 
                    print(k, config[source][k])
    else:
        print("Profile does not exist")
        if not show:
            config = update()
    return config        
    
def input_with_default(message, default):
    res = input("%s [%s]: " %(message, default))
    return res or default

def update():
    #global config 

    print("Updating profile")
    config = None
    profileini = getprofileini()
    config = configparser.ConfigParser()    

    default = {
        'download-files': { 
            'workspace': os.path.join(os.environ['HOME'], 'workspace/segment/downloads'),
            'bucket': "ccd-lapp-data.fourthlion.in",
            'prefix': "pipeline/logs/segment"
        }
            
    }

    config['download-files'] = {}
    for k in ['workspace', 'bucket', 'prefix', 'access', 'secret']:
        config['download-files'][k] = input_with_default('SEGMENT ' + k, default['download-files'].get(k,""))


    try: 
        os.makedirs(config['download-files']['workspace'])
    except:
        pass     

    with open(profileini, 'w') as fd:
        config.write(fd)

    print("Updated profile file:", config)

    return config

def get_config():
    #if config is None: 
     #   init() 
    config = init()
    return config 


    