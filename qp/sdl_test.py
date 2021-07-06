from ricxappframe.xapp_sdl import SDLWrapper
import time
import random

sdl=SDLWrapper(False) #True for debug
NS_UE1="ns_UE1"
NS_UE2="ns_UE2"

PREFIX_POS="pos_"

def get_now_in_sec():
    return round(time.time())

def sdl_set_ue(ns_ue):
    sdl.set(ns_ue, PREFIX_POS+str(get_now_in_sec()), random.random())

def sdl_get_ue_pos_list(ns_ue):
    return sdl.find_keys(ns_ue, PREFIX_POS)