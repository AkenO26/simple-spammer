import threading
import time
import tkinter as tk

from pynput.keyboard import Controller


def main():
    main_window = tk.Tk()
    main_window.title("Simple python spammer")
    w = 400
    h = 300
    main_window.minsize(w, h)
    main_window.maxsize(w, h)
    ws = main_window.winfo_screenwidth()
    hs = main_window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    main_window.attributes('-topmost', 'true')

    def stop():
        exit_event.set()

    exit_event = threading.Event()

    def get_input():
        input = entry.get("1.0", "end-1c") + "\n"
        ms = float(delay.get())
        counter = int(times.get())
        time.sleep(2)
        for i in range(counter):
            time.sleep(ms)
            keyboard = Controller()
            keyboard.type(input)
            if exit_event.is_set():
                exit_event.clear()
                break

    def start_t1():
        t1 = threading.Thread(target=get_input)
        t1.start()

    entry = tk.Text(main_window, height=10, width=100)
    entry.pack(padx=20, pady=20, side="top")

    delay = tk.Entry(main_window, width=3)
    delay.pack(padx=20, pady=10, side="right")

    delay_label = tk.Label(main_window, text="Delay(sec) :")
    delay_label.pack(pady=10, side="right")

    times_label = tk.Label(main_window, text="Number :")
    times_label.pack(pady=10, side="left")

    times = tk.Entry(main_window, width=4)
    times.pack(padx=20, pady=10, side="left")

    start_button = tk.Button(main_window, text="Start", width="10", command=start_t1)
    start_button.pack(padx=20, pady=10)

    stop_button = tk.Button(main_window, text="Stop", width="10", command=stop)
    stop_button.pack(padx=20, pady=10)

    main_window.mainloop()


main()
