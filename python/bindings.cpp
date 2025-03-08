#include "project.hpp"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(my_project_core, m) {
  py::class_<myproject::Calculator>(m, "Calculator")
      .def(py::init<>())
      .def("add", &myproject::Calculator::add)
      .def("subtract", &myproject::Calculator::subtract);
}
