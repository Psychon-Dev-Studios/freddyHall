""" Makes my life a lot easier """
import os, sys # Shuddup error

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080 # Screen dimensions
HOUR_LENGTH = 60 # How long, in seconds, each hour should be

if os.name == "nt": # The first step of the long process to get Linux supported. Yeah, specifically Linux, nothing else ;)
    WINDRIVE = str(os.environ['WINDIR'].split(":\\")[0])
else:
    WINDRIVE = ""

class manifest():
    """ The power of MANIFEST compells you """
    appName = "Freddy's Hall"
    appID = u"freehall"
    appVersion = "1.3.0"
    channel = "beta"
    author = "Princess & Kytten"
    autoUpdateSupported = False
    isSuperSecretBuild = True


class autoUpdates():
    """ Data helpful for automatic updates. If you're distributing your own customized version and you don't want to get the normal updates, set this to your own update source """
    UPDATE_URL = ""
    PAST_VERSIONS = ["1.0.0", "1.1.0", "1.2.0", "1.3.0", "1.3.1"] # If the current version on the update URL is in this list, don't download and install it (don't downgrade, basically.) NOTE: IF you chose to distribute a customized version, YOU'RE responsible to keep this up-to-date!


### Verification Checksum. Don't modify this or you'll break it. Break it and you'll make me cry ###
verified_checksum = [['credits.png', 'disclaimer.png', 'flink_beta.png', 'how_to_play.png', 'how_to_quit.png', 'icon_beta.png', 'icon_stable.png', 'icon_stable_large.png', 'missing_asset_warning.png', 'mmenu.png', 'mmenu.svg', 'mpx.png', 'mpx_old.png', 'mp_alert.svg', 'noAutoUpgrade.png', 'office_background.png', 'office_background_outage.png', 'office_door.png', 'office_door.svg', 'secret-build.png', 'title_screen.png', 'title_screen.svg', 'ambient.wav', 'camera_interference.wav', 'cxr_jumpscare_2.wav', 'desktop.ini', 'djmm_jumpscare.wav', 'door_slam.wav', 'fdy_dm_js.wav', 'fh_disclaimer_xep_trial_1.wav', 'heartbeat.wav', 'metallic_fs.mp3', 'metallic_fs.wav', 'mmenu_loop-temp2.wav', 'music_box.wav', 'music_box_2.wav', 'ambient.aup3', 'cam_interference.aup3', 'disclaimer.aup3', 'djmm_jumpscare.aup3', 'heartbeat.aup3', 'studio.aup3', "A freakin' chipmunk.wav", 
'camera_down.png', 'cam_1.png', 'cam_1.png.2022_04_10_21_19_15.0.svg', 'cam_2.png', 'cam_3.png', 'cam_4.png', 'cam_5.png', 'cam_6.png', 'empty_frame.png', 'minimap.png', '1.png', '2.png', '1.png', '2.png', '1.png', '2.png', '1.png', '2.png', '1.png', '2.png', '1.png', '2.png', '1.png', '2.png', '3.png', '5.png', '6.png', 'animated.gif', 'dj.jpeg', 'djmm_js.gif', '0.png', '1.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png', '19.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', 'fred.jpeg', 'freddy_demon_frames.zip', 'ucn_freddy_js.gif', '0.gif', '1.gif', '10.gif', '11.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif', '7.gif', '8.gif', '9.gif', 'frame_00_delay-0.04s.gif', 'frame_01_delay-0.04s.gif', 'frame_02_delay-0.04s.gif', 'frame_03_delay-0.04s.gif', 'frame_04_delay-0.08s.gif', 'frame_05_delay-0.04s.gif', 'frame_06_delay-0.04s.gif', 'frame_07_delay-0.04s.gif', 'frame_08_delay-0.04s.gif', 'frame_09_delay-0.04s.gif', 'frame_10_delay-0.04s.gif', 'frame_11_delay-0.04s.gif', 'frame_12_delay-0.04s.gif', 'frame_13_delay-0.04s.gif', 'frame_14_delay-0.04s.gif', 'frame_15_delay-0.04s.gif', 'frame_16_delay-0.08s.gif', 'frame_17_delay-0.04s.gif', 'frame_18_delay-0.04s.gif', 'frame_19_delay-0.04s.gif', 'frame_20_delay-0.16s.gif', '1.png', '2.png', '3.png', '4.png', '5.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '5.png', '6.png', '7.png', '8.png', '9.png', 'fps.ttf', 'nosifer.ttf', 'silkscreen.ttf', 'silk_condensed.ttf'], ['checksum.option', 'disclaimer.option', 'game.conf', 'showControls.option'], '1.3.0']