import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, sec)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

pomodoro_timer(25)  # 25分钟的专注时间
