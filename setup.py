from setuptools import setup, Extension
import os.path as pth
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

__module_file_dir = pth.dirname(pth.realpath(__file__))
__cpp_src_dir = pth.join(__module_file_dir, 'pyfzz')
src_files = []
src_files.append(pth.join(__cpp_src_dir, 'fzz.cpp'))
setup(name='fzz',
      version = "0.0.1",
      author = "Soham Mukherjee based on Tao Hou's FastZigzag C++ implementation",
      author_email = "soham.juetce@gmail.com",
      description = ("A Fast Zigzag persistent homology Python wrapper for C++"),
      license = "BSD",
      keywords = "example documentation tutorial",
      url = "http://packages.python.org/an_example_pypi_project",
      ext_modules=[Extension('pyfzz',include_dirs=[os.path.join(__cpp_src_dir,'phat-include')],
                             sources=src_files, language='c++17', extra_compile_args=['-std=c++17'])],
                             long_description=read('README'),)

