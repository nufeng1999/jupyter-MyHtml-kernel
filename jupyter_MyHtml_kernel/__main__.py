from ipykernel.kernelapp import IPKernelApp
from .kernel import MyHtmlKernel
IPKernelApp.launch_instance(kernel_class=MyHtmlKernel)
