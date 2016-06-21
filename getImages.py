import urllib2
import os
import json
 ##---------------------------------------------------------------------------
 ##-----------------------------DO FIRST--------------------------------------
 ##CREATE A FOLDER TO HOLD ALL THE DATA AND THEN INSERT IT IN THE STRING BELOW
PATH = "/Users/macBook/EyeWire_Raw_Data/"
 ##---------------------------------------------------------------------------
 ##-----------------------------DO FIRST--------------------------------------








counter = 0;
while counter<100:
	counter += 1
	##CREATE THE DIRECTORY FOR THE NEW VOLUME##
	firstVolumeID = 503
	workingVolumeID = firstVolumeID+(len(os.listdir("/Users/macBook/EyeWire_Raw_Data/"))-1)
	NewVolumeID = "V_" + str(workingVolumeID)
	path = PATH + NewVolumeID
	os.makedirs(path)

	##Creates the 8 subdirectories to hold the 8 Chunck image Stacks that make up a volume
	##Each chunk folder holds 128 individual 128x128 jpeg or png images
	os.makedirs(path + "/Chunck_0,0,0")
	os.makedirs(path + "/Chunck_1,0,0")
	os.makedirs(path + "/Chunck_0,1,0")
	os.makedirs(path + "/Chunck_1,1,0")
	os.makedirs(path + "/Chunck_0,0,1")
	os.makedirs(path + "/Chunck_1,0,1")
	os.makedirs(path + "/Chunck_0,1,1")
	os.makedirs(path + "/Chunck_1,1,1")
	##---------------------------------------##

	def requestData( URL, CHUNK ):
		print CHUNK
		Eyewire_data = urllib2.urlopen(URL).read()
		parsed_data = json.loads(Eyewire_data)
		
		global imgStrings

		#Gets the bounds of the entire volume based of the extremes of the chunkse
		if CHUNK == "/Chunck_0,0,0":
			global volumeMin_x
			volumeMin_x = parsed_data[0]['bounds']['min']['x']
			global volumeMin_y
			volumeMin_y = parsed_data[0]['bounds']['min']['y']
			global volumeMin_z
			volumeMin_z = parsed_data[0]['bounds']['min']['z']
		if CHUNK == "/Chunck_1,1,1":
			global volumeMax_x
			volumeMax_x = parsed_data[0]['bounds']['max']['x']
			global volumeMax_y
			volumeMax_y = parsed_data[0]['bounds']['max']['y']
			global volumeMax_z
			volumeMax_z = parsed_data[0]['bounds']['max']['z']
		##------------------------------------------------------------------------
		for index in range(len(parsed_data)):
			base64_string = parsed_data[index]['data']
			global fileType 
			fileType = "a"
			if "data:image/png;base64," in base64_string:
				base64_string = base64_string.replace("data:image/png;base64,", "")
				fileType = "png"
			else:
				if "data:image/jpeg;base64," in base64_string:
					base64_string = base64_string.replace("data:image/jpeg;base64,", "")
					fileType = "jpeg"
			
			if fileType == "jpeg" or fileType == "png":

				fh = open(path+CHUNK+"/img_"+str(index)+"."+fileType, "wb")
				fh.write(base64_string.decode('base64'))
				fh.close()

		chunkInfo = '{"volumeID":'+str(workingVolumeID)+","
		chunkInfo +='"chunk":{"x":'+CHUNK[8:-4] + ',"y":'+CHUNK[10:-2]+ ',"z":'+CHUNK[12:] + "},"
		chunkInfo += '"bounds":{"min":{"x":' + str(parsed_data[0]['bounds']['min']['x'])
		chunkInfo += ',"y":' + str(parsed_data[0]['bounds']['min']['y'])
		chunkInfo += ',"z":' + str(parsed_data[0]['bounds']['min']['z']) + "}"
		chunkInfo += ',"max":{"x":' + str(parsed_data[0]['bounds']['max']['x'])
		chunkInfo += ',"y":' + str(parsed_data[0]['bounds']['max']['y'])
		chunkInfo += ',"z":' + str(parsed_data[126]['bounds']['max']['z']) + "}}}"
		fh = open(path+CHUNK+"/chunkINFO.json","wb")
		fh.write(chunkInfo)
		fh.close() 

		return  
	 
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/0/0/0/tile/xy/0:127", "/Chunck_0,0,0" )
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/1/0/0/tile/xy/0:127", "/Chunck_1,0,0" )
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/0/1/0/tile/xy/0:127", "/Chunck_0,1,0" )
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/1/1/0/tile/xy/0:127", "/Chunck_1,1,0" )
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/0/0/1/tile/xy/0:127", "/Chunck_0,0,1" )
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/1/0/1/tile/xy/0:127", "/Chunck_1,0,1" )
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/0/1/1/tile/xy/0:127", "/Chunck_0,1,1" )
	requestData( "http://data.eyewire.org/volume/"+str(workingVolumeID)+"/chunk/0/1/1/1/tile/xy/0:127", "/Chunck_1,1,1" )

	chunkInfo = '{"volumeID":'+str(workingVolumeID)+","
	chunkInfo += '"bounds":{"min":{"x":' + str(volumeMin_x)
	chunkInfo += ',"y":' + str(volumeMin_y)
	chunkInfo += ',"z":' + str(volumeMin_z) + "}"
	chunkInfo += ',"max":{"x":' + str(volumeMax_x)
	chunkInfo += ',"y":' + str(volumeMax_y)
	chunkInfo += ',"z":' + str((volumeMax_z-volumeMin_z)*2+volumeMin_z) + "}}}"
	fh = open(path+"/volumeINFO.json","wb")
	fh.write(chunkInfo)
	fh.close()



