#python3 setup.py install
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='pointops',
    install_requires=[
        "numpy",
        "torch",
    ],
    ext_modules=[
        CUDAExtension('pointops_cuda', [
            'pointops/src/pointops_api.cpp',

            'pointops/src/ballquery/ballquery_cuda.cpp',
            'pointops/src/ballquery/ballquery_cuda_kernel.cu',
            'pointops/src/knnquery/knnquery_cuda.cpp',
            'pointops/src/knnquery/knnquery_cuda_kernel.cu',
            'pointops/src/grouping/grouping_cuda.cpp',
            'pointops/src/grouping/grouping_cuda_kernel.cu',
            'pointops/src/grouping_int/grouping_int_cuda.cpp',
            'pointops/src/grouping_int/grouping_int_cuda_kernel.cu',
            'pointops/src/interpolation/interpolation_cuda.cpp',
            'pointops/src/interpolation/interpolation_cuda_kernel.cu',
            'pointops/src/sampling/sampling_cuda.cpp',
            'pointops/src/sampling/sampling_cuda_kernel.cu',

            'pointops/src/labelstat/labelstat_cuda.cpp',
            'pointops/src/labelstat/labelstat_cuda_kernel.cu',

            'pointops/src/featuredistribute/featuredistribute_cuda.cpp',
            'pointops/src/featuredistribute/featuredistribute_cuda_kernel.cu'
        ],
                      extra_compile_args={'cxx': ['-g'],
                                          'nvcc': ['-O2']})
    ],
    cmdclass={'build_ext': BuildExtension})
