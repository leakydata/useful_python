import shutil
import os

def clearCache():
    """
    Removes generic `__pycache__` .

    The `__pycache__` files are automatically created by python during the simulation.
    This function removes the genric files on simulation start and simulation end.
    """
    path = "C:\\Users\\njones\\Documents\\Python Scripts\\AR Tracking\\"
    try:
        for all in os.listdir(path):
            if os.path.isdir(path + all):
                if all == '__pycache__':
                    shutil.rmtree(path + all, ignore_errors=False) 
    except:
        pass
clearCache()
