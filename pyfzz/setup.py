from setuptools import setup, Extension
import os.path as pth
import os


__module_file_dir = pth.dirname(pth.realpath(__file__))
__cpp_src_dir = pth.join(__module_file_dir, '.')
src_files = []
extension = '*.cpp'
src_files.append(pth.join(__cpp_src_dir, 'fzz.cpp'))
setup(name='fzz',
      ext_modules=[Extension('fzz',include_dirs=['./phat-include/'],sources=src_files, language='c++17', extra_compile_args=['-std=c++17'])],)
# ext = Extension(
#     name='mpml',
#     sources=src_files,
#     include_dirs=cpp_extension.include_paths(),
#     language='c++',
#     extra_compile_args=['-fopenmp'],
#     extra_link_args=['-lgomp'])

# setup(name='mpml',
#       ext_modules=[ext],
#       cmdclass={'build_ext': cpp_extension.BuildExtension})
