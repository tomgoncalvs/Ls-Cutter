import sys
import time

def loading_animation(duration=1):
    animation = "|/-\\"
    idx = 0
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write("\r" + animation[idx % len(animation)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write("\r")