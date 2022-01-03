# pdfsplitter
> A simple way to extract and parse images for machine learning workflows.


This file will become your README and also the index of your documentation.

## Install

`pip install --upgrade pdfsplitter`

## How to use

The highest-level function for exporting image files from a series of images is `extract_images_from_pdfs`, which will take all the PDF files inside a source directory and extract the images to a destination directory. You have the added option of specifying which sort of image filetype you'd like for the exported images, as in this example:

```python
source = Path("./tryout/")
destination = Path("./tryout/processed")

# download all the PDFs listed on a particular list of URLs
download_pdf_files(
    get_pdf_links("https://open.defense.gov/Transparency/FOIA.aspx"), "./tryout"
)

# extracts all the images from the downloaded PDFs and saves them to a directory
extract_images_from_pdfs(source, destination, "jpg")
```

```python
# get stats on the downloaded PDF files
display_stats(get_stats(source))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-style: italic">                                  Stats for your PDF Files                                   </span>
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃<span style="font-weight: bold"> PageCou… </span>┃<span style="font-weight: bold"> Filename                                      </span>┃<span style="font-weight: bold"> ocr_lay… </span>┃<span style="font-weight: bold"> pdf_fil… </span>┃<span style="font-weight: bold"> author   </span>┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│<span style="color: #008000; text-decoration-color: #008000">       27 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2014_ACFO_Report_FINAL_REPORT.pdf             </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 236655   </span>│<span style="color: #000000; text-decoration-color: #000000"> Stephan… </span>│
│          │                                               │          │          │<span style="color: #000000; text-decoration-color: #000000"> Carr     </span>│
│<span style="color: #008000; text-decoration-color: #008000">        3 </span>│<span style="color: #008080; text-decoration-color: #008080"> 7-26-2013_Determination.pdf                   </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 214683   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> DA Determination-DCRIT Hawaii Water Wells.pdf </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 115574   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        3 </span>│<span style="color: #008080; text-decoration-color: #008080"> 12-18-14_Determination.pdf                    </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 50925    </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        4 </span>│<span style="color: #008080; text-decoration-color: #008080"> 6-1-2012_Determination.pdf                    </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 463902   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> 8-19-2021_Determination.pdf                   </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 350438   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">       15 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2012_ACFO_Report_FINAL_REPORT.pdf             </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 242305   </span>│<span style="color: #000000; text-decoration-color: #000000"> CarrS    </span>│
│<span style="color: #008000; text-decoration-color: #008000">        3 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2-12-2014_Determination.pdf                   </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 23823    </span>│<span style="color: #000000; text-decoration-color: #000000"> timothy… </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> DA%20Determination%20DoD%20Flights.pdf        </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 111521   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">       22 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2013_ACFO_Report_FINAL_REPORT.pdf             </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 258462   </span>│<span style="color: #000000; text-decoration-color: #000000"> CarrS    </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2-15-2018_Determination.pdf                   </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 342195   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">       49 </span>│<span style="color: #008080; text-decoration-color: #008080"> DoDFY2020AnnualFOIA_Report.pdf                </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 1247446  </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        3 </span>│<span style="color: #008080; text-decoration-color: #008080"> 7-5-2019_Determination.pdf                    </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 204453   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">       30 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2017_DoD_Chief_FOIA_Officer_Report.pdf        </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 4810077  </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">       28 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2021_DoD_Chief_FOIA_Officer_Report.pdf        </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 1131474  </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">       10 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2011_DoD_Chief_FOIA_OfficerReport.pdf         </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 113387   </span>│<span style="color: #000000; text-decoration-color: #000000"> CarrS    </span>│
│<span style="color: #008000; text-decoration-color: #008000">       27 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2018_DoD_Chief_FOIA_Officer_Report.pdf        </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 788227   </span>│<span style="color: #000000; text-decoration-color: #000000"> brandoct </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> 8-3-15_Determination.pdf                      </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 105563   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        3 </span>│<span style="color: #008080; text-decoration-color: #008080"> 1-21-2016_Determination.pdf                   </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 122706   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> 12-6-2017_Determination.pdf                   </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 189563   </span>│<span style="color: #000000; text-decoration-color: #000000"> deleonv  </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> 12-18-2018_Determination.pdf                  </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 153675   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">       30 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2016_ACFO_Report_FINAL_REPORT.pdf             </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 1108008  </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> 11-29-2017_Determination.pdf                  </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 369290   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        2 </span>│<span style="color: #008080; text-decoration-color: #008080"> DoD SAP IT DCRIT Determination.pdf            </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 127858   </span>│<span style="color: #000000; text-decoration-color: #000000">          </span>│
│<span style="color: #008000; text-decoration-color: #008000">        3 </span>│<span style="color: #008080; text-decoration-color: #008080"> 10-19-2018_Determination.pdf                  </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 70088    </span>│<span style="color: #000000; text-decoration-color: #000000"> JAMES    </span>│
│          │                                               │          │          │<span style="color: #000000; text-decoration-color: #000000"> HOGAN    </span>│
│<span style="color: #008000; text-decoration-color: #008000">       30 </span>│<span style="color: #008080; text-decoration-color: #008080"> 2015_ACFO_Report_FINAL_REPORT.pdf             </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 287445   </span>│<span style="color: #000000; text-decoration-color: #000000"> Stephan… </span>│
│          │                                               │          │          │<span style="color: #000000; text-decoration-color: #000000"> Carr     </span>│
│<span style="color: #008000; text-decoration-color: #008000">        3 </span>│<span style="color: #008080; text-decoration-color: #008080"> 7-31-2020_Determination.pdf                   </span>│<span style="color: #000080; text-decoration-color: #000080"> False    </span>│<span style="color: #af00ff; text-decoration-color: #af00ff"> 88447    </span>│<span style="color: #000000; text-decoration-color: #000000"> Dziecic… </span>│
│          │                                               │          │          │<span style="color: #000000; text-decoration-color: #000000"> Gerald J </span>│
│          │                                               │          │          │<span style="color: #000000; text-decoration-color: #000000"> Jr CIV   </span>│
│          │                                               │          │          │<span style="color: #000000; text-decoration-color: #000000"> OSD OGC  </span>│
│          │                                               │          │          │<span style="color: #000000; text-decoration-color: #000000"> (USA)    </span>│
└──────────┴───────────────────────────────────────────────┴──────────┴──────────┴──────────┘
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000; font-weight: bold">TOTAL PAGECOUNT:</span> <span style="color: #800000; text-decoration-color: #800000; font-weight: bold">311</span>
</pre>



## What is pdfsplitter?

## Features

- statistics generation
- image extraction

## Install

## How to use

## Roadmap
