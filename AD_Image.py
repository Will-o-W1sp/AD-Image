import pyautogui as gui
import obspython as obs

'''
    All of this just works
'''

# ------------------------------------------------------------

def script_description():
    return "Takes a screenshot of dota"

# ------------------------------------------------------------

hotkey_id = obs.OBS_INVALID_HOTKEY_ID

def script_load(settings):
    global hotkey_id
    hotkey_id = obs.obs_hotkey_register_frontend("ReloadDraftImages", "Reload Draft Images", hotkey_pressed)
    
    hotkey_save_array = obs.obs_data_get_array(settings, "reload_draft_images_hotkey")
    obs.obs_hotkey_load(hotkey_id, hotkey_save_array)
    obs.obs_data_array_release(hotkey_save_array)

# ------------------------------------------------------------

def script_save(settings):
    hotkey_save_array = obs.obs_hotkey_save(hotkey_id)
    obs.obs_data_set_array(settings, "reload_draft_images_hotkey", hotkey_save_array)
    obs.obs_data_array_release(hotkey_save_array)
    
# ------------------------------------------------------------

def hotkey_pressed(pressed):
    if pressed == True:
        # Take Screenshot
        image = gui.screenshot()

        # IMPORTANT: the following will need to be edited if you are not wizzle

        # Crop the image into two regions
        region1 = image.crop((787, 183, 1230, 1252))
        region2 = image.crop((2207, 183, 2660, 1252))

        # Save the two regions as separate PNG files
        region1.save("C:/Users/wpeza/Pictures/Screenshots/Radiant Draft.png")
        region2.save("C:/Users/wpeza/Pictures/Screenshots/Dire Draft.png")