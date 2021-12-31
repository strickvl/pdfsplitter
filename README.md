# pdfsplitter
> A simple way to extract and parse images for machine learning workflows.


This file will become your README and also the index of your documentation.

## Install

`pip install --upgrade pdfsplitter`

## How to use

The highest-level function for exporting image files from a series of images is `extract_images_from_pdfs`, which will take all the PDF files inside a source directory and extract the images to a destination directory. You have the added option of specifying which sort of image filetype you'd like for the exported images, as in this example:

```python
from pathlib import Path

source = Path("./tryout/")
destination = Path("./tryout/processed")

extract_images_from_pdfs(source, destination, "jpg")
```

## What is pdfsplitter?

## Features

- statistics generation
- image extraction

## Install

## How to use

## Roadmap
