# Template for LaTeX-bound Jupyter notebooks

Clone this template and use the directory as the working directory for Jupyter notebooks which you would like to convert to LaTeX documents.

## Converting notebooks to LaTeX

1. Edit the file thmsInNb_article.tplx to set your title, author, and date.
2. Edit the file converter.py to specify the input and output file names (input file should end in .ipynb, output file should end in .tex).
3. Run ```python converter.py``` in your command line.

## Handling matplotlib figures

Use matplotlib's ability to export figures to image files, then insert the images into your notebook within a markdown cell using markdown syntax. The alias you give the image will become its caption in the output file.
