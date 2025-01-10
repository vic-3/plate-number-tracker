from ultralytics import YOLO

#LOAD A MODEL

model = YOLO("yolov8n.yaml") # build a new model from scratch

#use the model
results = model.train(data="plates.yaml", epochs=10)
