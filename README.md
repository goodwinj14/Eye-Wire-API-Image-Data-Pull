# EyeWireAPI_Image_Data_Pull
A Simple Python script to pull image stacks from the EyeWire API, auto-generate sub directories and save the images accordingly.

After downloading the python script the first thing you must do before running it is create the folder that will hold all the data. Running the script once will generate a lot of images so you want to make sure these are being put into a folder somewhere and are not just thrown onto your desktop. 

After you have created this folder, open the getImages.py script.

At the top of the file you will see: PATH = "/Users/macBook/EyeWire_Raw_Data/" 
You will want to replace the "/Users/macBook/EyeWire_Raw_Data/" with the file path to the folder you created to hold the data.

Once you have replaced the file path with your own you can simply run the script and it will start downloading the information. The script will pull a hundred volumes from the Eye Wire API before terminating. To change the number of volumes being pulled simply edit the "while counter<100:" expression at the begging of the script.

Inside the folder targeted by the file path you specified earlier the script will create a sub-directory of each of the volumes it pulls. Inside each volume will be eight chunks that will each have 128 individual 128x128 images. Each chunk folder is given a name with a x,y,z coordinate. The name specifies the position with the volume that the chunk lies. The image below should help clarify this.



