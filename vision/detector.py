import cv2
import mediapipe as mp
from vision.direction import DirectionDetector

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# Direction logic
direction_detector = DirectionDetector()

def get_hand_direction(frame):
    """
    Takes a BGR frame and returns:
    'UP', 'DOWN', 'LEFT', 'RIGHT' or None
    """

    # Mirror image for natural movement
    frame = cv2.flip(frame, 1)

    # Convert to RGB for MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if not results.multi_hand_landmarks:
        return None

    # Only one hand
    hand_landmarks = results.multi_hand_landmarks[0]

    # Compute direction
    return direction_detector.get_direction(hand_landmarks)


#hellooooo