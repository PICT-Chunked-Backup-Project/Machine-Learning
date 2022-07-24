import cv2
import matplotlib.pyplot as plt


# classLabels = []
# file_name = r"C:\Users\dell\Desktop\machine learning\Object Detection\Labels.txt"
# with open(file_name,'rt') as fpt:
#     classLabels = fpt.read().rstrip('\n').split('\n')

# model.setInputSize(320,320)
# model.setInputScale(1.0/127.5)
# model.setInputMean(127.5)
# model.setInputSwapRB(True)

class image_classifier:
    config_file =""
    frozen_model = ""
    label_path=""
    def __init__(self,p,c,f,l):
        self.path = p
        self.label_path=l
        self.config_file=c
        self.frozen_model=f
        
    def classify(self):
        model=cv2.dnn_DetectionModel(self.frozen_model,self.config_file)
        tags=""
        img = cv2.imread(self.path)
#         plt.imshow(img)
#         plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        classLabels = []
        with open(self.label_path,'rt') as fpt:
            classLabels = fpt.read().rstrip('\n').split('\n')  
        model.setInputSize(320,320)
        model.setInputScale(1.0/127.5)
        model.setInputMean(127.5)
        model.setInputSwapRB(True)

        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
#         print(type(ClassIndex))
        if (len(ClassIndex)==0):
            return("None")
        else:
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
#     c=image_classifier(r"C:\Users\dell\Desktop\machine learning\Object Detection\ic2.jpg",r"C:\Users\dell\Desktop\machine learning\Object Detection\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt",r"C:\Users\dell\Desktop\machine learning\Object Detection\frozen_inference_graph.pb",r"C:\Users\dell\Desktop\machine learning\Object Detection\Labels.txt")
#     c.classify()