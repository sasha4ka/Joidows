from time import sleep
import pygame
import keyboard
import mouse

MOUSE_MULT = 25

pygame.init()
pygame.joystick.init()

joysticks = {}
clock = pygame.time.Clock()
alternative = False

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(ev.device_index)
            joysticks[joy.get_instance_id()] = joy
            print(f"Joystick {joy.get_name()} {joy.get_instance_id()} added")
        
        elif ev.type == pygame.JOYDEVICEREMOVED:
            if ev.instance_id in joysticks:
                print(f"Joystick {joysticks[ev.instance_id].get_name()} {ev.instance_id} removed")
                del joysticks[ev.instance_id]

        elif ev.type == pygame.JOYBUTTONDOWN:
            if ev.button == 0 and alternative:
                keyboard.press_and_release("alt+f4")
                print("close")
            elif ev.button == 0 and not alternative:
                keyboard.press_and_release("enter")
                print("enter")
            elif ev.button == 1:
                mouse.click()
                print("left click")
            elif ev.button == 2:
                mouse.right_click()
                print("right click")
            elif ev.button == 9 and not alternative:
                keyboard.press_and_release("shift+tab")
                print("shift+tab")
            elif ev.button == 9 and alternative:
                keyboard.press_and_release("alt+shift+tab")
                print("alt+shift+tab")
            elif ev.button == 10 and not alternative:
                keyboard.press_and_release("tab")
                print("tab")
            elif ev.button == 10 and alternative:
                keyboard.press_and_release("alt+tab")
                print("alt+tab")
            elif ev.button == 11:
                keyboard.press_and_release("up")
                print("key up")
            elif ev.button == 12:
                keyboard.press_and_release("down")
                print("key down")
            elif ev.button == 13:
                keyboard.press_and_release("left")
                print("key left")
            elif ev.button == 14:
                keyboard.press_and_release("right")
                print("key right")
            elif ev.button == 15:
                keyboard.press_and_release("win+tab")
    
    for joy in joysticks.values():
        vx = joy.get_axis(0)
        vy = joy.get_axis(1)
        if vx > -0.04 and vx < 0.04: vx = 0
        if vy > -0.04 and vy < 0.04: vy = 0
        mouse.move(vx*MOUSE_MULT, vy*MOUSE_MULT, absolute=False)

        if joy.get_axis(4) > 0.9:
            alternative = True
        else:
            alternative = False

        if joy.get_button(3):
            keyboard.press("ctrl")
            print("ctrl hold")
        else:
            keyboard.release("ctrl")
    
    clock.tick(30)