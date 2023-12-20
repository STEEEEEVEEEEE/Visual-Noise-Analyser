import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

video_file = 
cap = cv2.VideoCapture(video_file)


def detect_visual_noise():
    ret, frame1 = cap.read()
    
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    avg_change = 0.0 
    last_second_brightness_changes = []
    start_time = time.time()
    reference_time = time.time()
    total_change = []
    Counter = 0
    reference = []
    avg_time = 0

    times = []  # x-axä im Graph
    times2 = []
    avg_changes = []  # y-axä im Graph
    avg_changes2 = []
    

    while True:
        ret, frame2 = cap.read()

        if not ret:
            break

        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(gray1, gray2)
        brightness_change = np.mean(diff)
        last_second_brightness_changes.append(brightness_change)
        reference.append(brightness_change)

        gray1 = gray2


        cv2.imshow('frame', gray2)

        if time.time() > reference_time + 0.5:
            avg_time = np.mean(reference) * 100
            avg_changes2.append(avg_time)
            times2.append(time.time())
            reference = []
            reference_time = time.time()
            
            print('This is the average over a time of 1.5 second:', avg_time)
            plt.figure(2)
            plt.xlabel('Time (seconds)')
            plt.ylabel('Average Brightness Change')
            plt.clf()
            plt.xlabel('Time (seconds)')
            plt.ylabel('Average Brightness Change')
            plt.plot(times2, avg_changes2)
            plt.pause(0.01)

        if time.time() > start_time + 0.3:
            if np.mean(last_second_brightness_changes) * 100 < avg_time * 3:
                avg_change = np.mean(last_second_brightness_changes) * 100
            else:
                avg_change = avg_time
                
        
            last_second_brightness_changes = []
            start_time = time.time()
            Counter = Counter + 0.3
            total_change.append(avg_change)

            # listenä uffüllä
            times.append(time.time())
            avg_changes.append(avg_change)
            # zeichnä
            plt.figure(1)
            plt.xlabel('Time (seconds)')
            plt.ylabel('Average Brightness Change')
            plt.clf()
            plt.xlabel('Time (seconds)')
            plt.ylabel('Average Brightness Change')
            plt.plot(times, avg_changes)
            plt.pause(0.01)
            
            print("Average Brightness Change:", avg_change)

        # q drückä für usä ga
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    plt.show()
    print("Total Noise:", np.mean(total_change))
    print("Time passed:", Counter, "seconds")

detect_visual_noise()
