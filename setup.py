#/usr/bin/env python

from distutils.core import setup

setup(	name = "calcpkg",
		version = "2.0",
		description = "ticalc.org package manager",
		long_description = "CLI software to access TI calculator software sites such as ticalc.org.",
		author = "Ben Rosser",
		license = "MIT",
		author_email = "rosser.bjr@gmail.com",
		url = "http://www.ticalc.org/archives/files/fileinfo/433/43348.html",
		packages = ["calcrepo"],
		scripts = ["calcpkg"],
		package_data={'calcrepo': ['ticalc.files.index', 'ticalc.names.index']} )
