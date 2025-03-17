"""Setup script for my_project."""

import importlib
import os
import subprocess
import sys

import packaging.version
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
version_module = importlib.import_module("my_project.version")
version_content = version_module.__version__
package_version = packaging.version.parse(version_content)
setup.version = str(package_version)


class CMakeExtension(Extension):
    """CMake extension for my_project."""

    def __init__(self, name, sourcedir=""):
        """Initialize the CMake extension.

        Args:
            name (str): The name of the extension.
            sourcedir (str): The source directory of the extension.
        """
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(os.path.dirname(__file__))


class CMakeBuild(build_ext):
    """CMake build for my_project."""

    def build_extension(self, ext):
        """Build the extension.

        Args:
            ext (CMakeExtension): The extension to build.
        """
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
    version=setup.version,
    ext_modules=[CMakeExtension("my_project.lib.my_project_core")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
    package_data={
        "my_project": ["lib/*.so", "lib/*.pyd", "lib/*.pyi"],
    },
    include_package_data=True,
)
