import time
import pychromecast

chromecasts = pychromecast.get_chromecasts()
[cc.device.friendly_name for cc in chromecasts]

cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Dormitorio")
# Start worker thread and wait for cast device to be ready
cast.wait()

mc = cast.media_controller

while 1:
    print("{} - {}".format(mc.status.title, mc.status.artist ))
    print(mc.status.album_name)
    # print("Image url: {}".format(mc.images[0].url))
    time.sleep(1)

'''
mc = cast.media_controller
#mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
mc.block_until_active()
print(mc.status)

mc.pause()
time.sleep(5)
mc.play()
'''