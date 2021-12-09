"""Robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    robot.sleep(2)


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while True:
        robot.set_wheels_speed(10)
        robot.sleep(0.1)
        sensor_x = robot.get_left_line_sensor()
        sensor_y = robot.get_right_line_sensor()
        if sensor_x <= 200 or sensor_y <= 200:
            robot.set_wheels_speed(0)
            break
    robot.set_wheels_speed(30)
    robot.sleep(1)
    robot.set_wheels_speed(0)
    robot.done()


def a(robot):
    """K."""
    while True:
        robot.set_right_wheel_speed(25)
        robot.set_left_wheel_speed(25)
        new_sensor_5 = robot.get_second_line_sensor_from_right()
        new_sensor_2 = robot.get_second_line_sensor_from_left()
        robot.sleep(0.01)
        if new_sensor_5 >= 700 or new_sensor_2 >= 700:
            robot.set_wheels_speed(0)
            break


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(100)
    robot.sleep(0.1)
    while True:
        sensor_2 = robot.get_second_line_sensor_from_left()
        sensor_1 = robot.get_third_line_sensor_from_left()
        sensor_3 = robot.get_left_line_sensor()
        sensor_4 = robot.get_right_line_sensor()
        sensor_5 = robot.get_second_line_sensor_from_right()
        sensor_6 = robot.get_third_line_sensor_from_right()
        print(robot.get_line_sensors())
        if sensor_2 >= 700 and (sensor_4 < 200 or sensor_5 < 200 or sensor_6 < 200):
            while True:
                print("world")
                robot.set_right_wheel_speed(55)
                robot.set_left_wheel_speed(35)
                new_sensor_5 = robot.get_second_line_sensor_from_right()
                robot.sleep(0.01)
                if new_sensor_5 >= 700:
                    robot.set_wheels_speed(0)
                    break
        elif sensor_5 >= 700 and (sensor_3 < 200 or sensor_2 < 200 or sensor_1 < 200):
            while True:
                robot.set_right_wheel_speed(35)
                robot.set_left_wheel_speed(55)
                new_sensor_2 = robot.get_second_line_sensor_from_left()
                robot.sleep(0.01)
                if new_sensor_2 >= 700:
                    robot.set_wheels_speed(0)
                    break
        elif sensor_3 < 200 and sensor_4 < 200 and sensor_2 < 200 and sensor_5 < 200:
            a(robot)

        elif sensor_6 < 200 and sensor_3 > 200 and sensor_4 > 200 and sensor_2 > 200 and sensor_5 > 200:
            while True:
                print("tere")
                robot.set_right_wheel_speed(50)
                robot.set_left_wheel_speed(0)
                new_sensor_3 = robot.get_left_line_sensor()
                new_sensor_4 = robot.get_right_line_sensor()
                robot.sleep(0.01)
                if new_sensor_3 < 200 and new_sensor_4 < 200:
                    robot.set_wheels_speed(0)
                    break
        elif sensor_1 >= 700 and sensor_2 >= 700 and sensor_3 >= 700 and sensor_4 >= 700 and sensor_5 >= 700 and sensor_6 >= 700:
            robot.set_wheels_speed(100)
            robot.sleep(0.1)
            break
    robot.set_wheels_speed(0)
    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
