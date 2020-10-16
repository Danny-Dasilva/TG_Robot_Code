from threading import Event

exit = Event()

def main():
    while not exit.is_set():
      do_my_thing()
      exit.wait(60)

    print("All done!")
    # perform any cleanup here

def quit(signo, _frame):
    print("Interrupted by %d, shutting down" % signo)
    exit.set()

if __name__ == '__main__':

    import signal
    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit);

    main()


##############################
import time

def main():
    print("It’s time !")

if __name__ == "__main__":
    print("press ctrl-c to stop")
    loop_forever = True
    while loop_forever:
        main()
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            loop_forever = False
import time


def sleep(seconds):
    for i in range(seconds):
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            continue


sleep(60)


# except (KeyboardInterrupt, SystemExit):


# do keyboard interrupt and sys exit 
# make the process writable IE with open
#context manager or __enter__ exit
