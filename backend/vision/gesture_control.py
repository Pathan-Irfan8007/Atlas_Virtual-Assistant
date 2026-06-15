import cv2
import mediapipe as mp
import keyboard

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
RunningMode = mp.tasks.vision.RunningMode

def start_gesture_control():
    options = GestureRecognizerOptions(
        base_options=BaseOptions(
            model_asset_path="backend/models/gesture_recognizer.task"
        ),
        running_mode=RunningMode.IMAGE
    )

    recognizer = GestureRecognizer.create_from_options(options)

    cap = cv2.VideoCapture(0)

    last_gesture = ""

    while True:

        success, frame = cap.read()
        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = recognizer.recognize(mp_image)

        gesture = "None"

        if result.gestures:
            gesture = result.gestures[0][0].category_name

        if gesture != last_gesture:
            print("Gesture:", gesture)
            last_gesture = gesture

        cv2.putText(
            frame,
            gesture,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Atlas Vision", frame)

        key = cv2.waitKey(1) & 0xFF

        
        if key == 27 or keyboard.is_pressed("esc"):
            print("Thanks For Visiting")
            break


    cap.release()
    cv2.destroyAllWindows()

