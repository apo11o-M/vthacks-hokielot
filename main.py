from ultralytics import YOLO
import cv2
import time

print("Program Starts..")

# filename = "imgs/captures/captured_img.png"
# filename = "imgs/low-angle/low-5-top-left.jpg"

# def webcamCapture(filename: str):
#     # Take a pic from the webcam, store it in the local directory with the 
#     # current timestamp
#     webcam = cv2.VideoCapture(0)
#     if not webcam.isOpened():
#         print("Failed to open the webcam")
#         exit(0)

#     _, frame = webcam.read()
#     cv2.imwrite(filename, frame)
#     webcam.release()

# webcamCapture(filename)

def predictCarCount(fileCounter: int):
    filename = "timelapsePhotos/"
    # Use the pretrained model from the YOLOv8 library
    model = YOLO('yolov8n.pt')

    # Make the predictions
    s = filename + str(fileCounter) + ".jpg"
    results = model(source=s)

    # print(results[0])

    carCount = 0
    truckCount = 0
    busCount = 0
    for object in results[0].boxes.cls:
        if model.names[int(object)] == "car":
            carCount += 1
        elif model.names[int(object)] == "truck":
            truckCount += 1
        elif model.names[int(object)] == "bus":
            busCount += 1
    print("---------------------------------")
    print("Car count:", carCount + truckCount + busCount)
    print("---------------------------------")

    # res_plotted = results[0].plot()
    # cv2.imshow("Image", res_plotted)
    # cv2.waitKey(0)

    print("..Finished")

    return carCount + truckCount + busCount