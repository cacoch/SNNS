#!/usr/bin/python

from setuptools import setup, Extension, find_packages

#print extension_keywords

module1 = Extension(
        'snns.krui',
        sources = ['snns/krui.c'],
		include_dirs = ['../kernel/sources'],
        extra_compile_args=['-std=c99'],
		library_dirs = ['../kernel/sources'],
		libraries = ['kernel','func','fl']
        )

setup (
       name = 'snns',
       # ext_package='snns',
       version = '0.1',
       author='Patrick Kursawe',
       author_email='Patrick.Kursawe@web.de',
       description = 'SNNS kernel functions',
       packages=find_packages(),
       # packages = ['snns'],
       ext_modules = [module1],
       #py_modules = ['snns.util']
       )

