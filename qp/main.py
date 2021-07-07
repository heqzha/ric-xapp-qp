from ricxappframe.xapp_frame import Xapp
import schedule
import qp.sdl_test as sdl

cnt=0
def entry(self):
    schedule.every(1).seconds.do(prediction, self)
    while True:
        schedule.run_pending()

def prediction(self):
    print("hello world")
    global cnt
    if cnt%10==0:
        print(sdl.sdl_get_ue_pos_idx_list(sdl.NS_UE1))
        print(sdl.sdl_get_ue_pos_list(sdl.NS_UE1))
        # print(sdl.sdl_get_ue_pos_idx_list(sdl.NS_UE2))
    else:
        sdl.sdl_set_ue(sdl.NS_UE1)
        # sdl.sdl_set_ue(sdl.NS_UE2)
    cnt+=1

def start():
    # Initiates xapp api and runs the entry() using xapp.run()
    xapp = Xapp(entrypoint=entry, rmr_port=4560, use_fake_sdl=True)
    xapp.run()