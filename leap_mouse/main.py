from include import Leap
import mouse_control

def main():
    controller = Leap.Controller()
    controller_state = 0
    print "Hello World"
    while True:
        if controller.is_connected and controller_state == 0:
            controller_state = 1
            print "Leap Motion connected"
        if not controller.is_connected and controller_state == 1:
            controller_state = 0
            print "Leap Motion disconnected"
        if controller_state == 1:
            mouse_control.main(controller)


if __name__ == '__main__':
    main()
