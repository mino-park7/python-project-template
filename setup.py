import os
import subprocess

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(os.path.dirname(__file__))


class CMakeBuild(build_ext):
    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        build_temp = os.path.join(self.build_temp, "build")

        os.makedirs(build_temp, exist_ok=True)
        os.makedirs(extdir, exist_ok=True)

        # 현재 실행 중인 Python 인터프리터의 정보를 가져옴

        cmake_args = [f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}", "-DCMAKE_BUILD_TYPE=Release"]

        subprocess.check_call(["cmake", ext.sourcedir] + cmake_args, cwd=build_temp)

        subprocess.check_call(["cmake", "--build", "."], cwd=build_temp)


setup(
    name="my_project",
    packages=["my_project"],
    ext_modules=[CMakeExtension("my_project.lib.my_project_core")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
    package_data={
        "my_project": ["lib/*.so", "lib/*.pyd", "lib/*.pyi"],
    },
    include_package_data=True,
)
