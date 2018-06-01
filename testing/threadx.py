import threading
import time
def foo():
    time.sleep(5)
thr = threading.Thread(target=foo, args=(), kwargs={})
thr.start()


while __name__ == '__main__':
    thr.is_alive() # Boolean return
    #It will be easy to update the front end of the site dynamically because of this function
    #I can use the request library to get the content size, then iterate through each data chunk and calculate its size
    # Then its just simple math
