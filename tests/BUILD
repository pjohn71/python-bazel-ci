load("@pytest//:requirements.bzl", "requirement")
py_library(
    name = "test_utils",
    srcs = glob(["*.py"]),
    visibility = ["//visibility:public"],
    deps = [
        requirement("pytest")
    ]
)

py_test(
    name = "test_math_utils",
    srcs = ["test_math_utils.py"],
    deps = [
        "//src:math_utils",
    ],
    # Use pytest instead of the default test runner
    main = "test_math_utils.py",
    python_version = "PY3",
    srcs_version = "PY3",
)

py_test(
    name = "test_string_utils",
    srcs = ["test_string_utils.py"],
    deps = [
        "//src:string_utils",
    ],
    # Use pytest instead of the default test runner
    main = "test_string_utils.py",
    python_version = "PY3",
    srcs_version = "PY3",
)

filegroup(
    name = "all_test_files",
    srcs = glob(["*.py"]),
    visibility = ["//visibility:public"],
)
