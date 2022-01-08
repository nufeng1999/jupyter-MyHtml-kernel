##//%file:kernel.py
#
#   MyHtml Jupyter Kernel
#
from math import exp
from queue import Queue
from threading import Thread
from ipykernel.kernelbase import Kernel
from pexpect import replwrap, EOF
from jinja2 import Environment, PackageLoader, select_autoescape,Template
from abc import ABCMeta, abstractmethod
from typing import List, Dict, Tuple, Sequence
from shutil import copyfile,move
from urllib.request import urlopen
import socket
import copy
import mmap
import contextlib
import atexit
import platform
import atexit
import base64
import urllib.request
import urllib.parse
import pexpect
import signal
import typing 
import typing as t
import re
import signal
import subprocess
import tempfile
import os
import stat
import sys
import traceback
import os.path as path
import codecs
import time
import importlib
import importlib.util
import inspect
from . import ipynbfile
from plugins.ISpecialID import IStag,IDtag,IBtag,ITag,ICodePreproc
from plugins._filter2_magics import Magics
try:
    zerorpc=__import__("zerorpc")
    # import zerorpc
except:
    pass
fcntl = None
msvcrt = None
bLinux = True
if platform.system() != 'Windows':
    fcntl = __import__("fcntl")
    bLinux = True
else:
    msvcrt = __import__('msvcrt')
    bLinux = False
from .MyKernel import MyKernel
class MyHtmlKernel(MyKernel):
    implementation = 'jupyter-MyHtml-kernel'
    implementation_version = '1.0'
    language = 'html'
    language_version = ''
    language_info = {'name': 'html',
                     'version': sys.version.split()[0],
                     'mimetype': 'text/html',
                     'codemirror_mode': {
                        'name': 'ipython',
                        'version': sys.version_info[0]
                     },
                     'pygments_lexer': 'ipython%d' % 3,
                     'nbconvert_exporter': 'python',
                     'file_extension': '.html'}
    runfiletype='script'
    banner = "MyHtml kernel.\n" \
             "creates source code files and executables in temporary folder.\n"
    kernelinfo="[MyHtml]"
    main_head = "\n" \
            "\n" \
            "int main(List<String> arguments){\n"
    main_foot = "\nreturn 0;\n}"
##//%include:src/comm_attribute.py
    def __init__(self, *args, **kwargs):
        super(MyHtmlKernel, self).__init__(*args, **kwargs)
        self.runfiletype='script'
        self.kernelinfo="[MyHtmlKernel{0}]".format(time.strftime("%H%M%S", time.localtime()))
        
#################
##do_runcode
    def do_runcode(self,return_code,file_name,magics,code, silent, store_history=True,
                    user_expressions=None, allow_stdin=True):
        return_code=return_code
        file_name=file_name
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        retstr=''
        ##代码运行前
        for line in code.splitlines():
            self.mymagics._write_to_stdout(line,magics)
        ##代码启动后
        return_code=0
        ##代码运行结束
        if return_code != 0:
            self.mymagics._log("Executable exited with code {}".format(return_code),2)
        return bcancel_exec,retinfo,magics, code,file_name,retstr
##do_compile_code
    def do_compile_code(self,return_code,file_name,magics,code, silent, store_history=True,
                    user_expressions=None, allow_stdin=True):
        return_code=0
        file_name=file_name
        sourcefilename=file_name
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        retstr=''
        return bcancel_exec,retinfo,magics, code,file_name,retstr
##do_create_codefile
    def do_create_codefile(self,magics,code, silent, store_history=True,
                    user_expressions=None, allow_stdin=True):
        return_code=0
        file_name=''
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        retstr=''
        source_file=self.mymagics.create_codetemp_file(magics,code,suffix='.html')
        newsrcfilename=source_file.name
        file_name=newsrcfilename
        return_code=True
        return bcancel_exec,self.mymagics.get_retinfo(),magics, code,file_name,retstr
##do_preexecute
    def do_preexecute(self,code,magics,silent, store_history=True,
                user_expressions=None, allow_stdin=False):
        bcancel_exec=False
        retinfo=self.mymagics.get_retinfo()
        
        return bcancel_exec,retinfo,magics, code
