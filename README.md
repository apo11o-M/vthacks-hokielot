# HokieLot

## Installation

Make sure your python version >= 3.11

Install the necessary dependencies

```bash
pip install ultralytics opencv-python
```

To make predictions, run the following commands

```bash
python main.py
```

## Notes

There are two modes currently, one is to use the webcam another is to use the pre-downloaded images from the `imgs` folder. Change the `filename` variable on top of the `main.py` and comment/uncomment the `webcamCapture()` function call to switch between these two modes.

It should also output the number of cars/trucks it detects in the image in the terminal once it finished executing.