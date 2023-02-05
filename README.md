# mltoolbox
Repository for personal machine learning toolbox project

## Installation (for development)

1. Clone the repository

```bash
git clone https://github.com/professortavares/mltoolbox.git
```

2. Create a virtual environment

```bash
python3 -m venv venv
```

3. Activate the virtual environment

```bash
source venv/bin/activate
```

4. Install the requirements

```bash
pip install -r requirements_dev.txt
```

5. Install the package

```bash
pip install -e .
```

6. To upgrade the requirements

```bash
pip install -U -r requirements_dev.txt
```

7. Execute unit tests

```bash
pytest
```

8. Execute code coverage

```bash
pytest --cov=mltoolbox --cov-report=cov_html
```

## Generate documentation

ref.:https://towardsdatascience.com/documenting-python-code-with-sphinx-554e1d6c4f6d

1. Install the requirements (if not already installed)

```bash
pip install sphinx sphinx_rtd_theme
```

2. Go to the docs folder

```bash
cd docs
```

3. Generate the documentation folder structure (aswer the questions with the default values)

```bash
sphinx-quickstart
```

4. Edit the conf.py file, to include the following lines

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
```

Change the extensions to include the following lines:
```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode']
```

5. Change the html output template

```python
html_theme = 'sphinx_rtd_theme'
```

6. In root folder, generate the .rst files

```bash
sphinx-apidoc -f -o docs mltoolbox
```

7. In docs folder, search for index.rst and include module documentation

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

```

8. In docs folder, generate the html files

```bash
make html
```

9. To clean the docs folder

```bash
make clean
```

## Installation (for production)

1. Install the package

```bash
pip install https://github.com/professortavares/mltoolbox/archive/main.zip
```