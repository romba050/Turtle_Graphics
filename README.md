# README

Spiral             |  Star
:-------------------------:|:-------------------------:
![image](images/png/spiral_2023-12-27T23h10m16.png "tricolor_spiral")  |  ![image](images/png/red-yellow_star_2023-12-28T00h37m34.png "red-yellow_star")
![image](images/png/rainbow_spiral_2023-12-31T10h50m50.png "rainbow_spiral")


## Turtle Documentation
https://docs.python.org/3/library/turtle.html

## Python Setup
I downloaded Python's latest stable release for MacOS from the python webpage
https://www.python.org/downloads/
because this project needs python-tk (a dependency of the turtle module) and homebrew python doesn't come with python-tk
After installing and folllowing the additional instructions of the installer such as running the provided bash script for PATH management and restarting the terminal, python should be localised as follows:
```bash
$ which python
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
```

```bash
$ python -m venv Turtle_Graphics
$ source Turtle_Graphics/bin/activate
```

For some reason, env python insists on using python3.11, which doesn't work, so I force it to use python3.12 by calling the script
```bash
$ python3.12 triangle.py 
```
or simply
```bash
$ ./triangle.py
```

To exit environment:
```bash
$ deactivate
```

## Additional dependency
The function save_layout uses postscript, which is based on ghostscript and needs to be installed seperatly:
```bash
brew install ghostscript
```
This is because the vector image format ESP (Encapsulated PostScript) is used.

## Viewing result images
EPS is no longer supported by MacOs Preview. You can download Skim to open EPS. It is a PDF viewer capable of opening EPS without rasterizing them.
https://skim-app.sourceforge.io/


