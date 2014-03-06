# Makefile: implement basic setup.py commands in make

all: build
	python setup.py build

build:
	python setup.py build

install:
	sudo python setup.py install

clean:
	python setup.py clean

dist:
	python setup.py sdist --formats=gztar,zip
