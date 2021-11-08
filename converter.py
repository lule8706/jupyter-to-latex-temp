from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import LatexExporter
from nbconvert.preprocessors import TagRemovePreprocessor

c = Config()

c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ("remove_output",)
c.TagRemovePreprocessor.remove_input_tags = ("remove_input",)
c.TagRemovePreprocessor.enabled = True

c.LatexExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor", "nbconvert.preprocessors.ConvertFiguresPreprocessor"]
c.LatexExporter.template_file = "latex_tmpl/thmsInNb_article.tplx"

exporter = LatexExporter(config=c)
exporter.register_preprocessor(TagRemovePreprocessor(config=c), True)

output = LatexExporter(config=c).from_filename("temp.ipynb")

print(output)

with open("temp.tex", "w") as f:
    f.write(output[0])
