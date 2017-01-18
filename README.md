# Facemash Workshop

**A workshop introducing computer vision tools in python.** A python program that goes through photos in a directory, detects faces in them, warps (scale and alignement) them and overlays them to create the average face of the dataset.

##Starting Remarks

**No existing python knowledge is required.**

**Operating System:** This workshop has been written on OSX, others may also work.

**Other dependencies:** opencv, dli, virtualenv (optional). An [installation guide is below](https://github.com/leoneckert/facemash-workshop#installation-guide-for-basic-requirements).  

##Content

* [Using Facemash](https://github.com/leoneckert/facemash-workshop#using-facemash)
* [Setting up a (virtual) working environment](https://github.com/leoneckert/facemash-workshop#setting-up-a-virtual-working-environment)
* [Installation guide for basic requirements](https://github.com/leoneckert/facemash-workshop#installation-guide-for-basic-requirements) (Beginners start here!)

##Using Facemash

**basics 1**

	$ python basics1.py data/face1.jpg

![basics](https://github.com/leoneckert/facemash-workshop/blob/master/screenshots/basics1.png)

**basics 2**

	$ python basics2.py data/face1.jpg data/face2.jpg

![basics](https://github.com/leoneckert/facemash-workshop/blob/master/screenshots/basics2.png)

**facemash**

	$ python facemash.py data/students

![basics](https://github.com/leoneckert/facemash-workshop/blob/master/screenshots/facemash.png)

##Setting up a (virtual) working environment

**[1] Navigate to a directory in which you wanna start the project.**

For example like this:

	$ cd ~/Desktop
	$ mkdir facemash
	$ cd facemash
	
**[2] Create a new "virtualenv", this allows us to run our program within a controlled environment without interferring with the global system.**

	$ virtualenv env
	
`virtualenv` is the command, `env` the name we give our environment, typing `$ ls` shows you that a new directory with that name has been created, DON'T WORRY about that one, ever. 

**[3] Access the virtual environment**

	$ source env/bin/activate
	
A `(env)` at the beginning of your command line prompt signals that you are IN the virtual environment. To exit, simply enter `deactivate` (not for now though).

 
**[4] Transfer our global installation of OpenCv into our virtual environment**

This one is a bit strange, but a little trick does the job in my experience. First we need to find our global opencv files, chances are that

	$ ls /usr/local/lib/python2.7/site-packages/cv*
	
will return 

	/usr/local/lib/python2.7/site-packages/cv.py  
	/usr/local/lib/python2.7/site-packages/cv2.so
	/usr/local/lib/python2.7/site-packages/cv.pyc

Those are the files we are looking for, the location of them can differ. Once found, while still in the virtual environment, we copy them with

	$ cp /usr/local/lib/python2.7/site-packages/cv* $VIRTUAL_ENV/lib/python2.7/site-packages/

	
I found this trick [here](https://medium.com/@manuganji/installation-of-opencv-numpy-scipy-inside-a-virtualenv-bf4d82220313#.i235dr6wb).

**[5] Install Numpy & Scipy and test OpenCV**

Any python module we install with pip, will be installed INTO the virtual enviromnent. OpenCV requires the following

	$ pip install numpy scipy
	
OpenCV should now work! To test open the interactive python interpreter with `$ python`, and enter `import cv2`. No error message should appear. Yes? Great!

[6] Install dlib

With boost and cmake installed (in the installation guide below), this should be easy:

	$ pip install dlib
	
**[6] Download a facial-landmarks-prediction model**

Download the file you find at [https://github.com/biometrics/openbr-models/blob/master/dlib/shape_predictor_68_face_landmarks.dat](https://github.com/biometrics/openbr-models/blob/master/dlib/shape_predictor_68_face_landmarks.dat) and just put it into your project folder.

**[7] Get some datasets of faces**

Store in data/[name of dataset].

For itp, I supply a set of current students' faces.
	
---

This should be it! Now get coding on the project, or [use the finished pieces in this repo](https://github.com/leoneckert/facemash-workshop#using-facemash)!

---

















##Installation guide for basic requirements

The following has only been tested on OSX. It looks like a lot, but the good news is, it has always worked super smoothly when I tried it!

Enter all commands without the `$` symbol :-)

#####Python

This should be installed on your machine bby default, run `$ python --version` to make sure. If you actually run into issues with this, [this](http://docs.python-guide.org/en/latest/starting/install/osx/) should help (chances are, you'll install python with brew (see below) if you actually don't have it yet).

#####Homebrew ([more info](http://brew.sh))

Check if you have it with `$ which brew`, this should return a path.   
If it doesn't, install it by running 

	$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
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

Above test might still return the same error or a different one `[...] ImportError: numpy.core.multiarray failed to import [...]`, but, trust me, DON'T WORRY (we'll fix that within the virtual environent later on).

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

#####cmake

Check with `$ which cmake`. Install it by running 
		
	$ brew install cmake

---

**... Now we should be all set to [set up our virtual environment](https://github.com/leoneckert/facemash-workshop#setting-up-a-virtual-working-environment)!!!**

---


	
