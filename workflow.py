#!/bin/python3
import time
import subprocess
from typing import List

class WorkFlow():
    '''
    Example config:

    {
        "firefox": {
            "run": "firefox", 
            "adjust": "wmctrl -r Firefox -t 0"
        },
        "vscode":{
            "run": "code /home/user/Dev/example",
            "adjust":"wmctrl -r Visual -t 0"
        },
        "todoist":{
            "run":"/home/adam/user/Todoist.AppImage",
            "adjust":"wmctrl -r Todoist -t 2"
        },
        "thunderbird":{
            "run":"thunderbird", 
            "adjust":"wmctrl -r Thunderbird -t 2"
        }
    }


    Example workflow script:
        import workflow
        conf = {
            "app": {
                "run": "run_cmd",
                "adjust": "adjust_command"
                }
            }
        workflow.Workflow(conf).run()
    '''
    config = {}
    open_apps = []

    def __init__(self,cfg=None):
        self.config=cfg
        #self.open_apps= self.get_open_apps()
        
    def init_apps(self):
        for app,cmds in self.config.items():
            #print(f"Opening {app} with command:\n\t {cmds['run']}")
            subprocess.Popen(cmds["run"].split())
    
    def arrange_applications(self):
        for app,cmds in self.config.items():
            #print(f"Adjusting [{app}] with command:\n\t {cmds['adjust']}")
            subprocess.run(cmds["adjust"].split())

    def is_open(self, window_title, refresh=True) -> bool:
        if refresh:
            self.open_apps = self.get_open_apps()
        return window_title in self.open_apps

    def get_open_apps(self) -> List:
        out= subprocess.check_output(['wmctrl' ,'-l']).decode("utf-8").splitlines()
        self.open_apps= []
        [self.open_apps.append(self.strip_app_title(title)) for title in out]
        return self.open_apps

    def strip_app_title(self, title) ->str:
        return " ".join(title.split()[3::])
            
    def run(self):
        self.init_apps()
        time.sleep(5)
        self.arrange_applications()
