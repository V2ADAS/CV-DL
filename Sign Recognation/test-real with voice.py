import cv2
import time
import numpy as np
from ultralytics import YOLO
import pygame
def play_audio(file_path):
    try:
        # Initialize Pygame
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load(file_path)

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error playing audio:", e)
    finally:
        # Clean up Pygame
        pygame.mixer.quit()



# Load the YOLOv8 model

model = YOLO('best.pt')
classes = model.names
print(model.names)

cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if  success:
        # Run YOLOv8 inference on the frame
        result = model.predict(frame, conf=0.6)
        # print(result.boxes)

        # Visualize the results on the frame
        annotated_frame = result[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Testing", annotated_frame)
        
        # Check if signs are detected

        stop_sign_index = 8  # 'Stop' sign has index 8
        Speed_limit_100_sign_index =0
        Speed_limit_120_sign_index = 1
        Speed_limit_20_sign_index = 2
        Speed_limit_30_sign_index = 3
        Speed_limit_50_sign_index =4
        Speed_limit_60_sign_index = 6
        Speed_limit_80_sign_index = 7
        Speed_limit_70_sign_index = 5

        for r in result:
            # Get the detected classes from the result
            if r.boxes:
                box = r.boxes[0]
                class_id = int(box.cls)
                object_name = model.names[class_id]

                if classes[stop_sign_index] in object_name:
                    text = "\nWarning: You need to stop!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\stop.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)

                
                elif classes[Speed_limit_50_sign_index] in object_name:
                    text2= "\nWarning: Speed ​​Limit 50 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text2, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed50.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)



                elif classes[Speed_limit_100_sign_index] in object_name:
                    text3 = "\nWarning: Speed ​​Limit 100 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text3, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed100.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)
                
                elif classes[Speed_limit_120_sign_index] in object_name:
                    text5 = "\nWarning: Speed ​​Limit 120 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text5, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed120.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)

                elif classes[Speed_limit_60_sign_index] in object_name:
                    text10 ="\nWarning: Speed ​​Limit 60 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text10, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed60.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)
                
                elif classes[Speed_limit_80_sign_index] in object_name:
                    text12 ="\nWarning: Speed ​​Limit 80 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text12, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed80.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)
                
                elif classes[Speed_limit_20_sign_index] in object_name:
                    text13 ="\nWarning:Speed ​​Limit 20 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text13, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed20.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)
                
                elif classes[Speed_limit_30_sign_index] in object_name:
                    text15 ="\nWarning: Speed ​​Limit 30 please watch your speed!\n"
                    # im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text15, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed30.mp3'
                    # Play the audio file
                    play_audio(audio_file_path)

                
                elif classes[Speed_limit_70_sign_index] in object_name:
                    text20 ="\nWarning: Speed ​​Limit 70 please watch your speed!\n"
                    #im_array = r.plot()  # plot a BGR numpy array of predictions
                    cv2.putText(annotated_frame, text20, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # Replace 'your_audio_file.mp3' with the path to your audio file
                    audio_file_path = r'C:\Users\Tahany\PycharmProjects\YOLO SIGN RECOGNATION\speed70.mp3'

                    # Play the audio file
                    play_audio(audio_file_path)
                else:
                    print("No Detection!")

            # Display the annotated frame
            cv2.imshow("YoloV8 Detection - Traffic Signs", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()