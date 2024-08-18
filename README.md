# Diabetic-Retinopaty-Detection
This project focuses on using image processing techniques to analyze retinal images and detect anomalies indicative of the disease. It is designed to detect Microaneurysms in the images.
# Key Functions
1.	Loads a diabetic retinopathy image
2.	Converts the image to grayscale
3.	Applies median filtering to reduce noise
4.	Applies thresholding to segment the blood vessels
5.	Applies morphological operations to enhance the blood vessels
6.	Find the optic disc using a function
7.	Draws a circle around the optic disc
8.	Calculates the area of the optic disc
9.	Calculates the number of microaneurysms
10.	Displays the results


Project Description: Diabetic Retinopathy Detection Using Image Processing and Machine Learning
This project focuses on the development of an automated system for detecting and classifying diabetic retinopathy (DR) from retinal images. Diabetic retinopathy is a severe eye condition that can lead to blindness if not detected and treated early. The system is designed to assist ophthalmologists by automatically segmenting key anatomical structures in the retina, detecting pathological features, and classifying the stages of diabetic retinopathy.

The system employs a combination of advanced image processing techniques and machine learning algorithms to perform the following tasks:

Blood Vessel Segmentation: Blood vessels are segmented using techniques such as the Frangi filter or Gabor filter, enhancing the visibility of retinal vessels, which are crucial for diagnosing various stages of diabetic retinopathy.

Optic Disc Segmentation: The optic disc, a critical anatomical landmark, is segmented using active contour models (snakes) or level set methods. Accurate segmentation of the optic disc is essential for further analysis of retinal images.

Microaneurysm Detection: Microaneurysms are the earliest signs of diabetic retinopathy. The system detects microaneurysms using blob detection or feature extraction methods, which help in identifying the severity of the condition.

Classification of Diabetic Retinopathy Stages: The segmented features are fed into machine learning models, such as Support Vector Machines (SVM) or Convolutional Neural Networks (CNN), to classify the retinal images into different stages of diabetic retinopathy.

The goal of this project is to create a reliable and efficient tool for early detection and monitoring of diabetic retinopathy, potentially reducing the burden on healthcare providers and improving patient outcomes through timely intervention.

Microaneurysm Detection Using Blob Detection
Microaneurysm Detection using Blob Detection is a critical component of the automated diabetic retinopathy detection system. Microaneurysms are small, circular, reddish spots on the retina, caused by the dilation of capillaries. They are among the earliest clinical signs of diabetic retinopathy, and their detection is crucial for early diagnosis.

Blob Detection is an image processing technique used to identify regions in an image that differ in properties, such as brightness or color, compared to surrounding regions. In the context of retinal images, blob detection is employed to identify microaneurysms by recognizing these small, round, dark spots that stand out against the lighter background of the retina.

The process typically involves the following steps:

Preprocessing: The retinal image is first converted to grayscale, and contrast enhancement techniques are applied to improve the visibility of microaneurysms. This may involve techniques like histogram equalization or contrast stretching.

Blob Detection: The enhanced image is then processed using blob detection algorithms. One common approach is the Maximally Stable Extremal Regions (MSER) algorithm, which detects stable regions in the image that correspond to microaneurysms. Alternatively, other blob detection methods like Laplacian of Gaussian (LoG) can be used.

Feature Extraction: The detected blobs are analyzed based on their size, shape, and intensity to distinguish microaneurysms from other retinal structures. Specific features, such as roundness and intensity, are used to identify true microaneurysms.

Post-processing: False positives are reduced through morphological operations or by combining the blob detection results with other segmentation methods. The final output is a set of detected microaneurysms, which are then used to assess the stage of diabetic retinopathy.

Outcome: The accurate detection of microaneurysms using blob detection is vital for early diagnosis of diabetic retinopathy. By identifying these early signs, the system can help in the timely intervention, potentially preventing the progression of the disease and reducing the risk of vision loss.
