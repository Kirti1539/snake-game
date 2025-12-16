import cv2
from vision.detector import get_hand_direction
from game.main_game import SnakeGame

def main():
    cap = cv2.VideoCapture(0)
    game = SnakeGame()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        direction = get_hand_direction(frame)
        game.update_direction(direction)

        # RUN ONE FRAME OF THE GAME
        alive = game.run_step()
        if not alive:
            print("Game Over")
            break

        cv2.imshow("Hand", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    