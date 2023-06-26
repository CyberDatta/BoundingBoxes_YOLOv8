# purpose of this file is to render the bounding boxes
import numpy as np

#below function carries first release version of the library? can we even call it one at this point
def render_boxes(results,class_colors,font_class_colors,font_id,font_scale):
    # class ids of the yolo v8 ultralytics results
    coordinates_ordered_list_classes=results[0].boxes.cls.cpu()
    coordinates_ordered_list_classes=coordinates_ordered_list_classes.numpy()
    #dict for class id and class names
    classes=results[0].names
    # xyxy bounding boxes
    coordinates_ordered_list=results[0].boxes.xyxy.cpu()
    coordinates_ordered_list=coordinates_ordered_list.numpy()
    #original image used for object detection
    img=results[0].orig_img 

    working_length=len(coordinates_ordered_list_classes)
    for object_id in range(0,working_length):
        pass   
