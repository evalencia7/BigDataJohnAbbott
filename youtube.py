import time
import webbrowser

print("Starting")
count = 1
while (count <= 2):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=eJSik6ejkr0", 1, True)
    count = count + 1
