# Template for LaTeX-bound Jupyter notebooks

Clone this template and use the directory as the working directory for Jupyter notebooks which you would like to convert to LaTeX documents. This is only tested for Jupyter Lab and appears to result in all the figures being added at the end when converting to PDF rather than where they are in the notebook.

## Downloading and using template

1. Run the following commands in your command line:

```
cd desired/path/to/template
git clone https://github.com/lule8706/jupyter-to-latex-temp.git
```
2. Make a copy of the folder containing the cloned repo and place it in your desired directory.
3. Rename your copy to whatever you want.
4. Run the following command in your command line to delete the existing git setup:

```
cd path/to/copy
rm -rf .git
```
5. Set up your own version control if you want.

## Converting notebooks to LaTeX

1. Edit the file thmsInNb_article.tplx to set your title, author, and date.
2. Edit the file converter.py to specify the input and output file names (input file should end in .ipynb, output file should end in .tex).
3. Rename temp.ipynb to whatever you prefer and use it as your notebook file.
4. Tag cells you would like to remove from the output file with the "remove_cell" tag.
5. Tag cells whose input you would like to remove from the output file with the "remove_input" tag.
6. Tag cells whose output you would like to remove from the output file with the "remove_output" tag.
7. See section below for details on how to handle matplotlib figures.
8. Run ```python converter.py``` in your command line to convert your notebook to a TeX file.
9. Run ```xelatex <output-filename>.tex``` twice to convert output the TeX file to a PDF with a table of contents.

## Handling matplotlib figures

Use matplotlib's ability to export figures to image files, then insert the images into your notebook within a markdown cell using markdown syntax. The alias you give the image will become its caption in the output file. Make sure to tag any cells that output your matplotlib figure with the "remove_output" or "remove_cell" tag.

## Attribution for image file used

GiraffeWorld, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons
