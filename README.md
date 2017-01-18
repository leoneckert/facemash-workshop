# Facemash Workshop

**A workshop introducing computer vision tools in python.** A python program that goes through photos in a directory, detects faces in them, warps (scale and alignement) them and overlays them to create the average face of the dataset.


###Starting Remarks

**No existing python knowledge is required.**

**Operating System:** This workshop has been written on OSX, others may also work.

**Other dependencies:** opencv, dli, virtualenv (optional). An installation guide is below.  

###Installation guide for basic requirements

The following has only been tested on OSX.

#####Python

This should be installed on your machine bby default, run `python --version` to make sure. If you actually run into issues with this, [this](http://docs.python-guide.org/en/latest/starting/install/osx/) should help.

#####Homebrew ([more info](http://brew.sh))

Check if you have it with `which brew`, this should return a path.   
If it doesn't, install it by running 

		/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
you will need to enter your password for this.

#####pip

Check with `which pip`. 
Install it by running 

		sudo easy_install pip

#####virtualenv (recommended)

Check with `which virtualenv`. Install it by running 
		
		pip install virtualenv

#####OpenCV ([more info](http://opencv.org))