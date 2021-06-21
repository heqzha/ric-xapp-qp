from ricxappframe.xapp_frame import Xapp
import schedule

def entry(self):
    schedule.every(1).seconds.do(prediction, self)
    while True:
        schedule.run_pending()

def prediction():
    print("hello world")

def start():
    # Initiates xapp api and runs the entry() using xapp.run()
    xapp = Xapp(entrypoint=entry, rmr_port=4560, use_fake_sdl=True)
    xapp.run()