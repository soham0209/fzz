from setuptools import setup, Extension
import os.path as pth
import os



__module_file_dir = pth.dirname(pth.realpath(__file__))
__cpp_src_dir = pth.join(__module_file_dir, '.')
src_files = []
src_files.append(pth.join(__cpp_src_dir, 'fzz.cpp'))
setup(name='pyfzz',
      ext_modules=[Extension('pyfzz',include_dirs=[os.path.join(__cpp_src_dir,'phat-include')],
                             sources=src_files, language='c++17', extra_compile_args=['-std=c++17'])],
                             )

