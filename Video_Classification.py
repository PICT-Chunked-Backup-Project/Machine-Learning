import cv2
import matplotlib.pyplot as plt

config_file =r"C:\Users\dell\Desktop\machine learning\Object Detection\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = r"C:\Users\dell\Desktop\machine learning\Object Detection\frozen_inference_graph.pb"
model = cv2.dnn_DetectionModel(frozen_model,config_file)

classLabels = []
file_name = r"C:\Users\dell\Desktop\machine learning\Object Detection\Labels.txt"
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean(127.5)
model.setInputSwapRB(True)

cap = cv2.VideoCapture(r"C:\Users\dell\Desktop\machine learning\Object Detection\icv.mp4")

if not cap.isOpened():
    cap = cv2.VideoCapture(0) 
if not cap.isOpened():
    raise IOError("Cannot open video")

font_scale = 3
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,frame = cap.read()

    ClassIndex, confidence, bbox = model.detect(frame,confThreshold=0.55)

    print(ClassIndex)
    if (len(ClassIndex)!=0):
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            if(ClassInd<=80):
                cv2.rectangle(frame,boxes,(255, 0, 0), 2 )
                cv2.putText(frame,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font, fontScale=font_scale,color=(0,255,0),thickness=3)

    cv2.imshow('Object Detection Tutorial', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

for ClassInd, conf, boxes in zip(set(ClassIndex.flatten()), confidence.flatten(), bbox):
    if(ClassInd<=80):
        print((classLabels[ClassInd-1]))
