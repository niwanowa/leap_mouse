# coding: utf-8
import pyautogui
from include import Leap

def load_fingers(frame):
    fingers = frame.fingers
    return fingers

def load_finger_position(fingers, finger_id, coordinate='y'):
    if coordinate == 'x':
        return fingers[finger_id].tip_position.x
    elif coordinate == 'y':
        return fingers[finger_id].tip_position.y
    elif coordinate == 'z':
        return fingers[finger_id].tip_position.z


def check_fingers(frame):
    if frame.fingers.is_empty:
        return False
    else:
        return True


def move_mouse(latest_fingers, previous_fingers):
    move_x = load_finger_position(previous_fingers, 1, 'x') - load_finger_position(latest_fingers, 1, 'x')
    move_z = load_finger_position(previous_fingers, 1, 'z') - load_finger_position(latest_fingers, 1, 'z')
    # Prevent erroneous detection
    if  -3 <= move_x <= 3 and -3 <= move_z <= 3:
        pyautogui.moveRel(-move_x*10, -move_z*10)
        print move_z


def main(my_controller):
    if check_fingers(my_controller.frame()) and check_fingers(my_controller.frame(1)):
        latest_fingers = load_fingers(my_controller.frame())
        previous_fingers = load_fingers(my_controller.frame(1))
        if load_finger_position(previous_fingers, 1, 'y') < load_finger_position(previous_fingers, 2, 'y'):
            move_mouse(latest_fingers, previous_fingers)
            print("成功！")


if __name__ == '__main__':
    controller = Leap.Controller()
    while True:
        main(controller)
        print controller.frame()
        print controller.frame()
        # time.sleep(3)