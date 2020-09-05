# VLF-Data-Handler
A python script for extracting VLF data from a GEM systems computer that has collected VLF data I tried to make this as automated as possible, but there are 
still some things you need to do to your data to start. 
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

## VLF_Extract.py tutorial 
This program was mostly written by Kyle Macy who is now a PhD Candidate at St. Louis University. Kyle Originally wrote this in a jupyter notebook and I have modified it to be a command line tool. 
### DATA FORMATING: NOTHING WILL WORK IF YOU DO NOT FORMAT YOUR DATA CORRECTLY
* Initially the data will have double spaces for seemingly random columns. These must be deleted. I suggest Notepad++ for an easy solution or vi/vim
that there are not double spaces. Check it twice, it will just be easier that way. 
* Remove Everything in the header up to the X column name. So if this was your data header
>/Gem Systems GSM-19TGWV 4116852 v7.0 28 X 2014 M t-ewv10l.v7o                       
>/ID 1 file 890402dp.wmv 04 IV 19
>/UTC+13
>/GPS datum WGS84   
>/X Y elevation nT sq cor-nT sat time picket-x picket-y slope n*[kHz ip op h1 h2 pT]
* change it to look like 
>X Y elevation nT sq cor-nT sat time picket-x picket-y slope n*[kHz ip op h1 h2 pT]
* Note the preceding forward slash is also gone. 
* At this point you should be ready to go. One other thing to be sure of is that the header shown above should be the first line in the input file. 

### Example run of VLF_Extract.py
* To run, first give the script permissions 
>chmod +x VLF_Extract.py
* Next all you need to do is call the script with python and your input file
>python VLF_Extract.py some_vlf_data.txt
* This will output 3 new files for each signal band with the name "some_vlf_data.txt_khz_vlf.txt" where kHz will be the value of kHz.

 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
 

## fraser.py tutorial
The fraser.py program was written entirely by me, but I could not have done it without the help of Kyle for the data extraction. The hard part is done. Now all you do is take your files from VLF_Extract.py and put them into fraser.py
>python fraser.py some_vlf_data.txt_khz_vlf.txt 
* This will output a plot of the fraser tilt and the distance along the profile in meters as well as a CSV file with all of the new columns (fraser tilt, distance along profile) added so that you may plot in a GIS software if you would like. 



