#Local installation guide
##Anaconda environment installation
Firstly, above doing a local install we recommend you to make use of the VM. With the VM environment you are far less likely to encounter trouble with the code from the labs. Nevertheless, if you have more experience with such troubleshooting and have worked with Python before, you could also consider doing a local install. We will be making use of Anaconda, and a .yml specifying a set of different packages that are used by Python in the labs. In Anaconda you can create such a Python environment by importing this .yml file. This is done as follows:

1. Firstly download the Anaconda Python 3.7 version for your operating system from: https://www.anaconda.com/distribution/
2. Install Anaconda from the installer
3. Download the Conda environment file (.yml) from: https://drive.google.com/uc?export=download&id=1vsKuxxg_B7X-bIb9_XtkY0sBllgkjpst
4. Open the Anaconda-Navigator
5. Go to the environment tab and click on import
6. As a name fill in "MMA2020" and choose the Conda environment file under "Specification file"


Congratulations! You have installed an Anaconda environment with the packages we will be using for the labs.

##Using the environment in the shell
Now whenever you are going to work on the labs you will have to activate this particular environment. Most of the labs can be done by running .py scripts from a shell window.

1. Open Terminal/Powershell or your preferred shell of choice.
2. Type in: "conda activate MMA2020"
3. Now you will be making use the environment with the correct Python version and packages we will be using for the labs!

Type this in everytime before you start working on the labs otherwise the environment won't be activated within the terminal!

##Using the environment in an IDE

This can be done by choosing the Conda environment as your project interpreter in an IDE such as Intellij IDEA. Follow the tutorial how to configure this Conda environment in an IDE here: https://www.jetbrains.com/help/idea/configuring-python-sdk.html

##Troubleshooting
If following this installation guide didn't work for you please consider following the VM installation guide since using the VM will prove less troublesome.
