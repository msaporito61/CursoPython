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
