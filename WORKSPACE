workspace(name = "python_bazel_ci")

# If you need external dependencies, you would define them here
# For example, using rules_python:
#
# load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
# http_archive(
#     name = "rules_python",
#     url = "https://github.com/bazelbuild/rules_python/releases/download/0.5.0/rules_python-0.5.0.tar.gz",
#     sha256 = "cd6730ed53a002c56ce4e2f396ba3b3be262fd7cb68339f0377a45e8227fe332",
# )
http_archive(
    name = "pytest",
    urls = ["https://github.com/pytest-dev/pytest/archive/refs/tags/7.4.0.tar.gz"],
    strip_prefix = "pytest-7.4.0",
)
load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    requirements = "//:requirements.txt",
)

