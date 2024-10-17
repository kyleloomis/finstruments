# Financial Instruments

## Linting/Auto-Formatting

This repo lints the code using a tool called [black](https://github.com/psf/black). If the CI pipeline fails in the 
linting stage run this command to autoformat the code to get it passing.

```bash
# Install if you dont have black
pip install black

#Autoformat
black ./finstruments
```

## Documentation

We use [pdoc3](https://medium.com/cemac/simple-documentation-generation-in-python-using-pdoc-16fb86eb5cd5) to
automatically generate documentation. All Python code must use
the [Google docstring format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) be compatible
with pdoc3. Make sure
to [update pycharm](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000784410/comments/115000640424)
to use Google as the default docstring style.

### HTML Documentation

```bash
pdoc3 --html ./finstruments/ --output-dir ./docs/generated --force
```

### Markdown Documentation

```bash
pdoc3 ./finstruments/ --template-dir ./docs/templates --output-dir ./docs/md --force --config='docformat="google"'
```

### Guides

```bash
jupyter nbconvert --execute --to markdown docs/guides/*/*.ipynb --TemplateExporter.extra_template_basedirs=docs --template=jupyter-templates
```

## Help

If you need any help or have feedback, please email me at [kyle@spotlight.dev](mailto:kyle@spotlight.dev).
