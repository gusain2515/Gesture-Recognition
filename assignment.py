import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def classify_gesture(landmarks):
    """
    Classifies a hand gesture based on the relative positions of finger landmarks.
    """
    
    finger_tips_ids = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    
    finger_bases_ids = [
        mp_hands.HandLandmark.INDEX_FINGER_MCP,
        mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
        mp_hands.HandLandmark.RING_FINGER_MCP,
        mp_hands.HandLandmark.PINKY_MCP
    ]
    
    
    fingers_extended = [
        landmarks.landmark[tip].y < landmarks.landmark[base].y
        for tip, base in zip(finger_tips_ids, finger_bases_ids)
    ]
    
    thumb_extended = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    
    
    if all(fingers_extended) and thumb_extended:
        return "Open Palm"
    elif not any(fingers_extended) and not thumb_extended:
        return "Fist"
    elif fingers_extended[0] and fingers_extended[1] and not any(fingers_extended[2:]):
        return "Peace Sign"
    elif thumb_extended and not any(fingers_extended):
        return "Thumbs Up"
    else:
        return "Unknown"


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    
    image = cv2.flip(image, 1)

    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
  
    result = hands.process(rgb_image)

    
    image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    
    gesture_name = "No Hand Detected"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
           
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
            gesture_name = classify_gesture(hand_landmarks)

    
    cv2.putText(image, f'Gesture: {gesture_name}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
 
    cv2.imshow('Hand Gesture Recognition', image)
    
 
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
