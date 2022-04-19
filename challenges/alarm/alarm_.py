import sched, time
import winsound as ws

def setAlarm(a_time, wave_file, message):
  s = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)
  s.enterabs(time=a_time, priority=1, action=print, argument=(message,))
  s.enterabs(a_time, 1, ws.PlaySound, argument=(wave_file, ws.SND_FILENAME))
  print(" Alarm set for ", time.asctime(time.localtime(a_time)))
  s.run()