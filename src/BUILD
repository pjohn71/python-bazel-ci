load("@rules_python//python:defs.bzl", "py_library")
py_library(
    name = "math_utils",
    srcs = ["math_utils.py"],
    visibility = ["//visibility:public"],
)

py_library(
    name = "string_utils",
    srcs = ["string_utils.py"],
    visibility = ["//visibility:public"],
)

filegroup(
    name = "all_src_files",
    srcs = glob(["*.py"]),
    visibility = ["//visibility:public"],
)

