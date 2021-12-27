# Python Workflows

### Files

- worflow.py
  template class gets passed a config file which explains the workflow

- work.workflow.py
  example workflow script, when executed, it opens the applications in the passed config


### Requirements

Currently wmctrl is needed because of the get_open_applications command. To use a different window manager, this would need to be updated to get the currently open application titles. If you don't need to check whether an application is already open, then this workflow class should be fine for you.
