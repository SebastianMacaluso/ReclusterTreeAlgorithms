# Makefile for ReclusterTreeAlgorithms
SHELL := /bin/bash

# You can set these variables from the commandline.
VERSION=$(shell python setup.py --version)

./dist/ReclusterTreeAlgorithms-${VERSION}-py3-none-any.whl:
	python ./setup.py sdist bdist_wheel

install: ./dist/ReclusterTreeAlgorithms-${VERSION}-py3-none-any.whl # pip install
	pip install --upgrade ./dist/ReclusterTreeAlgorithms-${VERSION}-py3-none-any.whl


%: Makefile