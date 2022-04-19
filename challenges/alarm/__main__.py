import alarm_, time

d = time.time() + 5
sound = "ch.mp3"
msg = "Wake up now!"
alarm_.setAlarm(d, sound, msg)