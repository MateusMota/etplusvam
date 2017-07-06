# etplusvam
Experiment which the purpose is to collect data for visual attention models (ET+VAM), LaPS project, UFPA.


For reproduction purposes, the required setup is listed below:
1) A webcam (in this project, it was used a Logitech C920 Pro HD)
2) Tobii EyeX (the Eye/Gaze tracking)
3) Psychopy (http://www.psychopy.org)

Experimental steps:

If you don't have the EyeX interface installed/configured, follow the steps below:

1) Connect the EyeX device in the USB 3.0 port
2) If the computer doesn't recognized the EyeX device or the Eyex drives, follow the next steps.
3) Download the EyeX interface in http://www.tobii.com/eyex-setup
3) Disconnect and connect the device again.
4) If the error persists:
a)Acess, in Windows, the Control panel\Hardware and Songs\Device manager
b)Search for the EyeX device
c)Execute the driver updates in Properties

After of installation/configured of EyeX interface, is necessary download the Microsoft Visual Studio, then follow the steps of EyeX setting , according the "Walkthrough: setting up a C/C++ project for the EyeX C API " tutorial ( http://developer.tobii.com/walkthrough-setting-cc-project-eyex-c-api/ ). Is avaiable to EyeX a C/C++ library and examples codes to data collection. To collect data, it was used a "MinimalGazeDataStream" code (developer.tobii.com/c-sample-walk-minimalgazedatastream/) with some changes present in file MinimalGazeDataStream.txt . 

The next step is configure the visual stimuli experiment in Psychopy (http://www.psychopy.org/) using the visual_attention.psyexp. The images created in this experiment for calibration was generated using OpenCV (http://opencv.org/), the others images was used from the Google database (warmup) and from Toyama database (http://ivc.univ-nantes.fr/en/databases/IRCCyN_IVC_Toyama_LCD/). It is also important, to experiment compilation, change the images path and use the csv file containing the experiment conditions.


      

