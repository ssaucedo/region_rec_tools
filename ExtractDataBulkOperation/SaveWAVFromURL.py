#!/usr/bin/python3

import json
import os
import requests
import sys
import xml.etree.ElementTree as ElementTree
import urllib
import shutil
import webbrowser

from urllib.request import Request, urlopen


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def retrieve_wav_url(tree):
    for child in tree:
        if(child.tag == "{http://www.clarin.eu/cmd/}Resources"):
            for a in child:
                if a.tag == "{http://www.clarin.eu/cmd/}ResourceProxyList":
                    for proxy in a:
                        for e in proxy:
                            if "WAV" in e.text:
                                 url =  e.text
        if(child.tag == "{http://www.clarin.eu/cmd/}Components"):
           for a in child:
               for e in a:
                   if(e.tag == "{http://www.clarin.eu/cmd/}CommunicationInfo"):
                       for data in e:
                           if(data.tag == "{http://www.clarin.eu/cmd/}Location"):
                               for data_e in data:
                                   if(data_e.tag == "{http://www.clarin.eu/cmd/}Region"):
                                       region = data_e.text
                   if(e.tag == "{http://www.clarin.eu/cmd/}GeneralInfo"):
                       for data in e:
                           if(data.tag == "{http://www.clarin.eu/cmd/}Name"):
                               name = data.text
    return url, region, name


def retrieve_name(tree):
    for child in tree:
        if(child.tag == "{http://www.clarin.eu/cmd/}Components"):
            for a in child:
                for e in a:
                    if(e.tag == "{http://www.clarin.eu/cmd/}CommunicationInfo"):
                        for data in e:
                            if(data.tag == "{http://www.clarin.eu/cmd/}Location"):
                                for data_e in data:
                                    if(data_e.tag == "{http://www.clarin.eu/cmd/}Region"):
                                        region = data_e.text




a = ["Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F07-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F0C-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F10-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F14-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F18-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F1C-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F20-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F24-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F28-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F30-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F2C-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F34-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F38-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F3C-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F40-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F44-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F48-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F4C-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F50-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F54-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F58-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F5C-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F60-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F64-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F68-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F6C-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F70-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F74-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F78-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F7C-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F80-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F88-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F84-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F8C-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F94-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F98-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F9C-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5F90-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FA0-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FA8-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FA4-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FAC-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FB0-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FB4-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FB8-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FBC-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FC0-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FC4-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FC8-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FCC-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FD0-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FD4-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FD8-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FDC-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FE0-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FE4-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FE8-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FEC-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FF0-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FF4-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FF8-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-5FFC-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6000-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6004-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6008-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-600C-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6010-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6015-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6019-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-601D-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6021-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6025-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6029-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-602D-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6031-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6035-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6039-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-603D-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6041-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6049-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6045-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-604D-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6051-8"]

corpus_urls = [
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6055-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6059-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-605D-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6061-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6065-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6069-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-606D-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6075-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6079-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6071-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-607D-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6081-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6085-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-608D-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6091-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6089-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6095-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6099-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-609D-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60A1-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60A5-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60A9-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60AD-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60B1-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60B5-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60B9-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60BD-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60C1-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60C5-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60C9-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60CD-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60D5-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60D1-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60D9-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60DD-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60E1-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60E5-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60E9-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60ED-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60F1-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60F5-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60F9-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-60FD-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6101-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6105-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6109-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-610D-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6111-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6115-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6119-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-611D-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6121-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6125-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6129-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-612D-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6131-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6135-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6139-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-613D-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6141-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6145-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6149-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-614D-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6151-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6155-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6159-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-615D-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6161-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6165-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6169-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-616D-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6171-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6175-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6179-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-617D-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6181-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6185-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6189-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-618D-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6191-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6195-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6199-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-619D-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61A1-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61A5-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61A9-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61AD-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61B1-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61B5-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61B9-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61BD-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61C1-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61C5-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61C9-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61CD-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61D1-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61D5-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61D9-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61DD-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61E1-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61E5-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61E9-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61ED-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61F1-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61F5-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61F9-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-61FD-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6201-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6205-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6209-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-620D-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6211-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6215-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6219-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-621D-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6221-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6225-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6229-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-622D-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6235-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6231-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6239-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-623D-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6241-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6249-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6251-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-624D-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6255-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6259-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-625D-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6261-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6265-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6269-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-626D-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6271-2",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6275-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6279-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-627D-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6281-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6285-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6289-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-628D-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6291-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6295-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6299-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-629D-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62A1-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62A5-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62A9-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62AD-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62B1-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62B5-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62B9-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62BD-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62C1-7",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62C5-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62C9-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62CD-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62D1-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62D5-1",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62D9-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62DD-9",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62E1-3",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62E5-F",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62E9-B",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62EE-6",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62F2-0",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62F6-C",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62FA-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-62FE-4",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6302-E",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6306-A",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-630B-5",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6311-D",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-6316-8",
"Metadata	application/xml+cmdi	http://hdl.handle.net/11022/0000-0000-631B-3"]


class AudioFile:
    def __init__(self, url,region,name):
        self.url = url
        self.region = region
        self.name = name
downloadDir = "/home/santiagosau/proyectos/PFI/repository/spoken-corpus-hacaspa/"

def getKey(audiofile):
    return audiofile.region

l = []
for url in corpus_urls:
    url = url[30:]
    tree = ElementTree.fromstring(requests.get(url).content)
    url, region, name =  retrieve_wav_url(tree)
    print(str(url)+"   "+str(region)+"   "+str(name))
    #l.append(AudioFile(url, region, name))
ordered = sorted(l, key=getKey)
for o in ordered:
    print(o.region)

for o in ordered:
    print(o.url)
