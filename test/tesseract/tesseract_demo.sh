#!/bin/bash
for f in ../sample/*.jpg; do
	python3 tesseract.py --image "$f" -c 50
done
