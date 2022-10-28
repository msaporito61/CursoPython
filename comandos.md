# Instaladores

### Instalacion de modulos para generar instalaciones


```sh
$ pip install setuptools 
$ pip install wheel 
$ pip install twine 
$ pip install tqdm 
```

### Creo el archivo README para comentar el modulo a generar

```sh
$ touch README.md
```

### Creo el archivo *setup.py* 

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PaqueteSumar",
    version="0.0.1",
    scripts=["main.py"],
    author="Juan Perez",
    author_email="jperez@mail.com",
    description="Un paquete para sumar numeros",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msaporito61/CursoPython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

```

### Ejecuto el *setup.py* con la opcion *bdist_wheel* para crea el archivo local instalable con el comando *pip*
```sh
$ python setup.py bdist_wheel 
```

### Procedo a instalar el archivo generado y comprobar su funcionamiento
```sh
$ pip install dist/PaqueteSumar-0.0.1-py3-none-any.whl
$ pip list
```
### En caso de publicarlo pypi.org, genereo el archivo de configuracion con mis datos y lo publico

```sh
$ touch .pypirc

$ python -m twine upload dist/*
```

### Para generar ejecutables instalo en siguiente modulo

```sh
$ pip install cx_freeze 
```
### Para comprobar que puedo generar un instalable basico ejecuto lo siguente:

```sh
$ cxfreeze -c main.py --target-dir dist
```
### Creo el archivo *setup.py*

```python
from cx_Freeze import setup, Executable

build_options = {"packages": [], "excludes": ["tkinter"], "includes": []}

import sys

base = "Win32GUI" if sys.platform == "win32" else None

executables = [Executable("main.py", base=base, target_name="imc_calc")]

setup(
    name="IMC Calc",
    version="0.0.2",
    description="Calculador IMC",
    author="Juan Perez",
    options={"build_exe": build_options},
    executables=executables,
)
```

### Para generar un producto instalable en un disco virtual de Mac ejecuto lo siguiente:

```sh
$ python setup.py bdist_dmg
```

### Para generar un producto instalable en formato *rpm* ejecuto lo siguiente:

```sh
$ python setup.py bdist_rpm
```

### Para generar un producto instalable en formato *Win Installer* ejecuto lo siguiente:

```sh
$ python setup.py bdist_msi
```


### Para crear aplicaciones de entorno GUI, instalo el siguente Framework:
```sh
$ pip3 install -U vxPython
```
### Programa de test de GUI
```python
# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
``` 
### Para crear aplicaciones de entorno WEB, instalo el siguente Framework:
```sh
pip install Flask
```
### Programa de test de WEB
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

### Ejecuto para verificar:
```sh
$ flask --app main run
```