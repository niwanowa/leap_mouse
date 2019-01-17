from include import Leap
import pyautogui


def main():
    controller = Leap.Controller()
    # controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
    # controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
    controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
    # controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

    controller.config.set("Gesture.Circle.MinRadius", 10.0)
    controller.config.set("Gesture.Circle.MinArc", .5)
    controller.config.set("Gesture.Swipe.MinLength", 200.0)
    controller.config.set("Gesture.Swipe.MinVelocity", 750)
    controller.config.set("Gesture.KeyTap.MinDownVelocity", 40.0)
    controller.config.set("Gesture.KeyTap.HistorySeconds", .2)
    controller.config.set("Gesture.KeyTap.MinDistance", 1.0)
    controller.config.set("Gesture.ScreenTap.MinForwardVelocity", 30.0)
    controller.config.set("Gesture.ScreenTap.HistorySeconds", .5)
    controller.config.set("Gesture.ScreenTap.MinDistance", 1.0)
    controller.config.save()

    while True:
        frame = controller.frame()
        old_frame = controller.frame(1)
        try:
            new_position = hand_position(frame.hands)
            old_position = hand_position(old_frame.hands)

            pyautogui.moveRel(20*(new_position[0] - old_position[0]), 20*(new_position[1] - old_position[1]), 0.1)
        except:
            pass
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_KEY_TAP:
                key_tap = Leap.KeyTapGesture(gesture)
                print(key_tap)
                pyautogui.click()


def hand_position(frame):
        position = None
        try:
            for hand in frame:
                position = hand.palm_position
            return position
        except:
            pass


if __name__ == '__main__':
    main()
