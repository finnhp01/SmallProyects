from pynput import mouse, keyboard
import pygame
from pathlib import Path

pygame.mixer.init()
pipe_path = Path(__file__).parent / "ThePipe.ogg"
pipe = pygame.mixer.Sound("ThePipe.ogg")

def on_click(x, y, button, pressed):
    if pressed:
        print("Mouse click!")
        pipe.play()
    else:
        print("PIPE!")
        
def on_press(key):
    global listener
    if key == keyboard.Key.esc:
        listener.stop()
        return False

with mouse.Listener(on_click=on_click) as listener:
    with keyboard.Listener(on_press=on_press) as klistener:
        listener.join()
