from setuptools import setup

setup(name='jupyter_MyHtml_kernel',
      version='0.0.1',
      description='Minimalistic Python kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyHtml-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyHtml-kernel/tarball/0.0.1',
      packages=['jupyter_MyHtml_kernel'],
      scripts=['jupyter_MyHtml_kernel/install_MyHtml_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'web','html'],
      include_package_data=True
      )
