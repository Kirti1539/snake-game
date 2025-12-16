class DirectionDetector:
    def __init__(self):
        pass

    def get_direction(self, hand):
        wrist = hand.landmark[0]
        index = hand.landmark[8]

        x_diff = index.x - wrist.x
        y_diff = index.y - wrist.y

        deadzone = 0.03

        if abs(x_diff) > abs(y_diff):
            if x_diff > deadzone:
                return "RIGHT"
            elif x_diff < -deadzone:
                return "LEFT"
        else:
            if y_diff < -deadzone:
                return "UP"
            elif y_diff > deadzone:
                return "DOWN"

        return None
