"""Package to create dataset, build training and prediction pipelines.

This file should define or import all the functions needed to operate the
methods defined at yolov8_api/api.py. Complete the TODOs
with your own code or replace them importing your own functions.
For example:
```py
from your_module import your_function as predict
from your_module import your_function as training
```
"""
# TODO: add your imports here
import logging
from pathlib import Path
import yolov8_api.config as cfg
from ultralytics import YOLO
import json
 



logger = logging.getLogger(__name__)
logger.setLevel(cfg.LOG_LEVEL)


# TODO: warm (Start Up)
# = HAVE TO MODIFY FOR YOUR NEEDS =
def warm(**kwargs):
    """Main/public method to start up the model
    """
    # if necessary, start the model
    pass


# TODO: predict
# = HAVE TO MODIFY FOR YOUR NEEDS =
def predict( **args):
    """Main/public method to perform prediction
    """
    # if necessary, preprocess data
    
    # choose AI model, load weights
    
    # return results of prediction
    # Load a pretrained YOLOv8n model
    
    model = YOLO(args['model'])
    test_image_path = args['input']  
    results = []
    for image_path in test_image_path:
        print('Evaluating:', image_path)
       # results = model(image_path)  # results list
        args.pop('input', None)
        args.pop('accept', None)
        args.pop('task_type', None)
        result= model.predict(image_path, **args)
        logger.debug(f"[predict()]: {result}")
        results.append(result)
    return results
 

