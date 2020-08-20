# Face Recognition with Voice Output
The objective of this project is to detect and recognise the faces from the scene and give the person name as voice output to the user.<br/>
It has three modules: 
1.	Creator
2.	Trainer
3.	Recognizer
## Creator module
This module is used to create datasets i.e. we save faces and their names.
It first takes the id and name of the person and stores in a file (datatext file). 
Then it will detect the faces from scene using a pre-executed xml file called [**haarcascade_frontalface_default**](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html) (included in OpenCV file).
It takes photos in range 50-100 (this range is based on my personal experience but you may take more if you want) and saves all photos in grayscale for better feature extraction.
## Trainer module 
Datasets are used for training the model. It does by first loading the **LBPHFaceRecognizer** which is an algorithm called [LBPH]( https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b) (Local Binary Patterns Histograms) used for finding patterns in the image and remembering them. After loading, it then separates the name and associated image and gives it to **train()** for training the model to remember the image for the given name. The trained data is saved in yml format.

**For windows users** : You may face a problem like
` IOError: cannot identify image file '*Data\\Thumbs.db*` <br/>
Solution you can either [delete](https://www.youtube.com/watch?v=N7MgnYCMvHE) or ignore it by slicing the imgpaths array.
## Recognizer module
This module is responsible for recognizing and giving voice output. It first detects the faces from the scene and gives to the **predict()** function which returns id and confidence with which it thinks the detected face(s) belong to that id(s). The received id(s) are examined to find out to which name(s) it belongs and gives to **say()** which is a function of [pyttsx]( https://pyttsx.readthedocs.io/) for voice output to the user. It continues until user quits.
## Tools Used
1.  [Python 2.7.14](https://www.python.org/downloads/)
2.  [OpenCV 2.4.13](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.13/)
3.  [Pyttsx](https://pyttsx.readthedocs.io/en/latest/install.html)
4.  Numpy
5.  Pillow
