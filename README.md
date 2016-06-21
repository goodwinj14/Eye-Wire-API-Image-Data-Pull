# EyeWireAPI_Image_Data_Pull
A Simple Python script to pull image stacks from the EyeWire API, auto-generate sub directories and save the images accordingly.

After downloading the python script the first thing you must do befor running it is create the folder that will hold all the data. Running the script once will gennerate alot of images so you want to make sure these are being put into a folder somerwhere and are not just thrown onto your desktop. 

After you have created this folder, open the getImages.py script.

At the top of the file you will see: PATH = "/Users/macBook/EyeWire_Raw_Data/" 
You will want to replace the "/Users/macBook/EyeWire_Raw_Data/" with the file path to the folder you created to hold the data.

Once you have replaced the file path with your own you can simply run the srcipt and it will start downloding the information. The sript will pull a hundred volumes from the Eye Wire API befor terminating. To change the number of volumes being pulled simply edit the "while counter<100:" expersion at the beging of the script.


