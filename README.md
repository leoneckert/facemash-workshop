# Facemash Workshop

**A workshop introducing computer vision tools in python.** A python program that goes through photos in a directory, detects faces in them, warps (scale and alignement) them and overlays them to create the average face of the dataset.


###Starting Remarks

**No existing python knowledge is required.**

**Operating System:** This workshop has been written on OSX, others may also work.

**Other dependencies:** opencv, dli, virtualenv (optional). An [installation guide is below](https://github.com/leoneckert/facemash-workshop#installation-guide-for-basic-requirements).  

###Installation guide for basic requirements

The following has only been tested on OSX. It looks like a lot, but the good news is, it has always worked super smoothly when I tried it!

Enter all commands without the `$` symbol :-)

#####Python

This should be installed on your machine bby default, run `$ python --version` to make sure. If you actually run into issues with this, [this](http://docs.python-guide.org/en/latest/starting/install/osx/) should help (chances are, you'll install python with brew (see below) if you actually don't have it yet).

#####Homebrew ([more info](http://brew.sh))

Check if you have it with `$ which brew`, this should return a path.   
If it doesn't, install it by running 

	$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
you will need to enter your password for this.

#####pip

Check with `$ which pip`. 
Install it by running 

	$ sudo easy_install pip

#####virtualenv (recommended)

Check with `$ which virtualenv`. Install it by running 
		
	$ pip install virtualenv

#####OpenCV ([more info](http://opencv.org))

Check by starting the interactive python interpreter, enter `$ python`, the command line prompt will change to `>>>`, now enter `import cv2`. If nothing happens, great! Something like `[...] ImportError: No module named cv2 [...] ` means you need to install OpenCV by entering the following commands:

	$ brew tap homebrew/science
	$ brew install opencv
	
If above test returns a different error `[...] ImportError: numpy.core.multiarray failed to import [...]`, that's fine (we'll fix that within the virtual environent later on).

#####Boost ([more info](http://www.boost.org))

This, we need to install dlib in our virtual environent later on. Install entering the following commands:

	$ brew install boost --with-python
	$ brew install boost-python

Test if that worked with

	$ brew list | grep 'boost'
	
which should return

	boost
	boost-python

	

The steps to install boost are descript in more detail [here](http://www.pyimagesearch.com/2015/04/27/installing-boost-and-boost-python-on-osx-with-homebrew/).


... Now we should be all set to set up our virtual environment!


	
