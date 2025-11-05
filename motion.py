print("Motion Detection System") 
print("=" * 40) 
print("This module requires:") 
print(" Webcam") 
print(" OpenCV (pip install opencv-python)") 
print() 
input("Press Enter to check webcam...") 
print("Checking camera...") 
try: 
    import cv2 
    cap = cv2.VideoCapture(0) 
    if cap.isOpened(): 
        print("? Webcam is available") 
        print("Press 'q' to quit camera preview") 
        while True: 
            ret, frame = cap.read() 
            cv2.imshow('Motion Detection - Press Q to quit', frame) 
                break 
        cap.release() 
        cv2.destroyAllWindows() 
    else: 
        print("? Cannot access webcam") 
except ImportError: 
    print("? OpenCV not installed. Run: pip install opencv-python") 
except Exception as e: 
    print(f"? Error: {e}") 
input("Press Enter to return to menu...") 
