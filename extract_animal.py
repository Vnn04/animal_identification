import cv2 
from ultralytics import YOLO

class Extract_animal():
    def __init__(self, image_path):
        self.image_path = image_path
        self.model = YOLO('yolov8n.pt')
        self.results = self.model(image_path)
        
    def get_bounding_boxes(self):
        for result in self.results:
            tensor = result.boxes.xywh
        arr = tensor.cpu().numpy()
        return arr
    
    def extract_animal(self):
        image = cv2.imread(self.image_path)
        arr = self.get_bounding_boxes()
        for i, box in enumerate(arr):
            x, y, w, h = box 
            top_left = (int(x - w/2), int(y - h/2))
            bottom_right = (int(x + w+2), int(y+h+2))
            cropped_image = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            cv2.imwrite(f'animal_{i}.jpg', cropped_image) 
            
               
if __name__ == '__main__':
    ex = Extract_animal('/home/shin-sun/Downloads/bird.jpeg')
    ex.extract_animal()