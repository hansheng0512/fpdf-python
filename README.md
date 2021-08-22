# pdf-python
Create a pdf using Python. Explanation in this [Medium article](https://github.com/hansheng0512/fpdf-python).

## Table of contents
* [General info](#general-info)
* [Setup](#setup)

## General info
This project create a receipt in PDF using 'PyFPDF' Library and 
Python. PyFPDF is a library for PDF document generation under 
Python, ported from PHP 'FPDF', a well-known PDFlib-extension 
replacement. <br>

To include font in languages other than English, we use the 
extended version 'tFPDF' library that adds UTF-8 support. 
To use a new font, add the font.ttf file in './font/unifont/' 
and call the font using *add_font* in *main.py*. Please take 
note that not all font is compatible and able to be used 
with 'tFPDF'. <br>

You can find the documentation of PyFPDF and tFPDF here:
- [FPDF](https://pyfpdf.readthedocs.io/en/latest/)
- [tFPDF](http://www.fpdf.org/en/script/script92.php)
	
## Steps
### Git clone this project
```
$ git clone https://github.com/Techyhans/pdf-python.git
```

### To Enable FPDF With Multiple Languages: <br>
1. Install PHP
- [How to install PHP on Windows](https://www.sitepoint.com/how-to-install-php-on-windows/)

### Install FPDF
```
$ pip install fpdf
```

### Run and create PDF
```
$ python sample.py
```

