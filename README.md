# Template for LaTeX-bound Jupyter notebooks

Clone this template and use the directory as the working directory for Jupyter notebooks which you would like to convert to LaTeX documents. This is only tested for Jupyter Lab.

## Converting notebooks to LaTeX

1. Edit the file thmsInNb_article.tplx to set your title, author, and date.
2. Edit the file converter.py to specify the input and output file names (input file should end in .ipynb, output file should end in .tex).
3. Rename temp.ipynb to whatever you prefer and use it as your notebook file.
4. Tag cells you would like to remove from the output file with the "remove_cell" tag.
5. Tag cells whose input you would like to remove from the output file with the "remove_input" tag.
6. Tag cells whose output you would like to remove from the output file with the "remove_output" tag.
7. See section below for details on how to handle matplotlib figures.
8. Run ```python converter.py``` in your command line.

## Handling matplotlib figures

Use matplotlib's ability to export figures to image files, then insert the images into your notebook within a markdown cell using markdown syntax. The alias you give the image will become its caption in the output file. Make sure to tag any cells that output your matplotlib figure with the "remove_output" or "remove_cell" tag.
