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

class image_classifier:
    def __init__(self,p):
        self.path = p
        
    def classify(self):
        tags=""
        img = cv2.imread(self.path)
#         plt.imshow(img)
#         plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
#         print(ClassIndex)

        font_scale = 3
        font = cv2.FONT_HERSHEY_SIMPLEX
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
                    if(ClassInd<=80):
                        cv2.rectangle(img,boxes,(255, 0, 0), 2 )
                        cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font, fontScale=font_scale,color=(0,255,0),thickness=3)


#         plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        for ClassInd, conf, boxes in zip(set(ClassIndex.flatten()), confidence.flatten(), bbox):
            if(ClassInd<=80):
                tags = classLabels[ClassInd-1] 
                print((classLabels[ClassInd-1]))
#                 print(type(tags))
        return tags

# if __name__ == "__main__":
#     c=image_classifier("C:\\Users\\dell\\Desktop\\machine learning\\Object Detection\\ic2.jpg")
#     c.classify()
