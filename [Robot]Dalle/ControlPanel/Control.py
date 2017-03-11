import sys
import re
import os
import speech_recognition as sr
r = sr.Recognizer()
speedup_regx = re.compile("s.+up")
speedup_cmd ="node hawx-grove-edison-speedup.js"

stop_regx = re.compile("st.+p*")
stop_cmd ="node hawx-grove-edison-stop.js"

slow_regx = re.compile("sl.+d.+n")
slow_cmd ="node hawx-grove-edison-slow-down.js"

rock_regx = re.compile("roc*")
rock_cmd ="node hawx-grove-edison-rock.js"

turn_regx = re.compile("roc*")
rock_cmd ="node hawx-grove-edison-rock.js"

video_cmd = "python ./videoRecording.py"
once = True
def execute_cmd(tgt):
    print 'before match', tgt
    if speedup_regx.match(tgt):
        print 'match', tgt
        os.system(speedup_cmd)
        if(once):
            os.system(video_cmd)
            once = False
    elif stop_regx.match(tgt):
        print 'match', tgt
        os.system(stop_cmd)

    elif slow_regx.match(tgt):
        print 'match', tgt
        os.system(slow_cmd)
    
    elif rock_regx.match(tgt):
        print 'match', tgt
        os.system(rock_cmd)

while True:
    print('Start Listening')
    with sr.Microphone() as source:
         # audio = r.listen(source)
        audio = r.listen(source)
        print("Done Listening")
    try:
        in_str = str(r.recognize_google(audio)).lower()
        print("Yout said: " + in_str)
        execute_cmd(in_str)

    except KeyboardInterrupt:
        sys.exit()
    except:
        # print("Could not understand audio")
        pass
