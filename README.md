# Fork of [Secreit](https://github.com/SanoKyohei/Secreit/) by [Sano Kyohei](https://github.com/SanoKyohei/)

## Purpose

This modified version of Secreit is set up in order to loop through a folder of images and output data at the end.

## Instructions

### Function Run Location

```Python
App = Stage_Check(debug=0, open_in_excel=1, use_graph=0, ask_for_dir=0, def_images_location='Cell Images')
App.image_loop()
```

### Arguments

* debug=0 (1 turns on debug mode which currently only runs the first image)

* open_in_excel=1 (1 opens the created CSV)

* use_graph=0 (1 sets the Matplotlib data to show although currently not working on my system yet)

* ask_for_dir=0 (opens a file dialog that asks for the location of the folder of images you want to run this through)

* def_images_location='Cell Images' (sets the default folder location)

## Todo

* excel or csv output

## Requirements

Located within Requirements.txt.

Main requirements are shown below.

```python
Python 3.6
numpy 1.19.1
opencv-python 4.1.1
keras (tensorflow backend)== 2.2.4 (NOT 2.3)
tensorflow 1.13.1
```

## Contributors to this fork

[Kaitlyn Roman](https://github.com/kroman4): (enter your title here)

[Michael Ericson](https://github.com/Concrete18): Python Programmer

[Sano Kyohei](https://github.com/SanoKyohei/): Created main repo along with currently used weights
