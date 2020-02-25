# Local installation guide
## Anaconda environment installation
Firstly, above doing a local install we recommend you to make use of the VM. With the VM environment you are far less likely to encounter trouble with the code from the labs. Nevertheless, if you have more experience with such troubleshooting and have worked with Python before, you could also consider doing a local install.

This procedure only work for Linux and OSX installs. We will be making use of Anaconda, and a .yml specifying a set of different packages that are used by Python in the labs. In Anaconda you can create such a Python environment by importing this .yml file. This is done as follows:

1. Firstly download the Anaconda Python 3.7 version for your operating system from: https://www.anaconda.com/distribution/
2. Install Anaconda from the installer
3. Download the Conda environment file (MMA2020.yml) from this Github repository (or clone the repository).
4. Open the Anaconda-Navigator
5. Go to the environment tab and click on import
6. As a name fill in "mma2020" and choose the Conda environment file under "Specification file"

## Using the environment
Now whenever you are going to work on the labs you will have to activate this particular environment. Most of the labs can be done by running .py scripts from a shell window.

1. Open Terminal/Powershell or your preferred shell of choice.
2. Type in: "conda activate mma2020". Type this in everytime before you start working on the labs otherwise the environment won't be activated within the terminal!
3. Now you are making use the environment with the correct Python version and packages. Make sure to use the command "python" and not "python3" or other variante when running your programs.
4. Check that everything is correctly installed by running the executable scripts in the "Code" folder of this repository, for example `python Code/video_query.py --help`. If you get an error and do not see the "help" of the program, notify the teaching team. These are the programs you will be running during the course, so if there are issues with them, they must be fixed.

## Using the environment in an IDE

This can be done by choosing the Conda environment as your project interpreter in an IDE such as Intellij IDEA. Follow the tutorial how to configure this Conda environment in an IDE here: https://www.jetbrains.com/help/idea/configuring-python-sdk.html

## Troubleshooting

If you encounter any packages missing make use of the "conda install ..." command to install these.

On Linux the OpenCV package might not be installed well directly. This can be resolved by activating the mma2020 environment, and then running the command "conda install -c conda-forge opencv=3.4.2"

If following this installation guide didn't work for you please consider following the VM installation guide since using the VM will prove less troublesome.
