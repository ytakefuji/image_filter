# image_filter
This shows how to interactively build an optimum filter using ipywidgets.
Using the following picture, this example shows how to extract a pupil image.

<img src='p.png' width=209 height=127>
<pre>
$ pip install -U ipywidgets
$ pip install -U jupyterlab widgetsnbextension
$ pip install -U notebook-as-pdf
run the following command
$ pyppeteer-install

</pre>

# How to run jupyter-lab
The following command to run jupyter-lab launcher

$ jupyter-lab --no-browser

http address will be shown on the screen.

copy the URL address and past it to browser (chrome or edge).


<img src='1.png' width=480 height=300>

click Notebook and save Untitle.ipynb file as filter.ipynb. 
And copy the content of c.py file and past it to filter.ipynb

<img src='2.png' width=480 height=300>

run filter.ipynb and three slides will be popped. 
slide channel-1 to 139 to be able to exactly extract a pupil.

<img src='3.png' width=480 height=300>

In order to save the result as pdf file, choose PDFviaHTML menu. 
filter.pdf will be saved in download directory.

<img src='4.png' width=480 height=300>

# Exercise for students
Build c.py program.
