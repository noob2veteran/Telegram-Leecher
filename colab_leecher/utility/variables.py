# copyright 2023 © Xron Trix | https://github.com/Xrontrix10


from time import time
from datetime import datetime
from pyrogram.types import Message


class BOT:
    SOURCE = []
    TASK = None
    class Setting:
        stream_upload = "Media"
        convert_video = "Yes"
        convert_quality = "Low"
        caption = "Monospace"
        split_video = "Split Videos"
        prefix = ""
        suffix = ""
        thumbnail = False

    class Options:
        stream_upload = True
        convert_video = True
        convert_quality = False
        is_split = True
        caption = "code"
        video_out = "mp4"
        custom_name = ""
        zip_pswd = ""
        unzip_pswd = ""

    class Mode:
        mode = "leech"
        type = "normal"
        ytdl = False

    class State:
        started = False
        task_going = False
        prefix = False
        suffix = False
        new_folder = False


class YTDL:
    header = ""
    speed = ""
    percentage = 0.0
    eta = ""
    done = ""
    left = ""


class Transfer:
    down_bytes = [0, 0]
    up_bytes = [0, 0]
    total_down_size = 0
    sent_file = []
    sent_file_names = []


class TaskError:
    state = False
    text = ""


class BotTimes:
    current_time = time()
    start_time = datetime.now()
    task_start = datetime.now()


class Paths:
    WORK_PATH = "/content/Telegram-Leecher/BOT_WORK"
    THMB_PATH = "/content/Telegram-Leecher/colab_leecher/Thumbnail.jpg"
    VIDEO_FRAME = f"{WORK_PATH}/video_frame.jpg"
    HERO_IMAGE = f"{WORK_PATH}/Hero.jpg"
    DEFAULT_HERO =  "/content/Telegram-Leecher/custom_thmb.jpg"
    MOUNTED_DRIVE = "/content/drive"
    down_path = f"{WORK_PATH}/Downloads"
    temp_dirleech_path = f"{WORK_PATH}/dir_leech_temp"
    mirror_root = "/content/drive/MyDrive/Colab Leecher Uploads"
    mirror_dir = mirror_root
    temp_zpath = f"{WORK_PATH}/Leeched_Files"
    temp_unzip_path = f"{WORK_PATH}/Unzipped_Files"
    temp_files_dir = f"{WORK_PATH}/leech_temp"
    thumbnail_ytdl = f"{WORK_PATH}/ytdl_thumbnails"
    access_token = "/content/token.pickle"

import os, json
_DEST_CFG = "/content/Telegram-Leecher/destination.json"

def _load_destination():
    try:
        if os.path.exists(_DEST_CFG):
            with open(_DEST_CFG) as f:
                data = json.load(f)
                mdir = data.get("mirror_dir")
                if mdir:
                    Paths.mirror_dir = mdir
    except Exception:
        pass
_load_destination()

def save_destination():
    try:
        os.makedirs(os.path.dirname(_DEST_CFG), exist_ok=True)
        with open(_DEST_CFG, "w") as f:
            json.dump({"mirror_dir": Paths.mirror_dir}, f)
    except Exception:
        pass
    


class Messages:
    caution_msg = "\n\n<i>💖 When I'm Doin This, Do Something Else ! <b>Because, Time Is Precious ✨</b></i>"
    download_name = ""
    task_msg = ""
    status_head = f"<b>📥 DOWNLOADING » </b>\n"
    dump_task = ""
    src_link = ""
    link_p = ""


class MSG:
    sent_msg = Message(id=1)
    status_msg = Message(id=2)



class Aria2c:
    link_info = False
    pic_dwn_url = "https://picsum.photos/900/600"


class Gdrive:
    service = None
