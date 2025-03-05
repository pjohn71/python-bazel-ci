# Define targets for linting and formatting

# Linting with pylint
sh_test(
    name = "lint",
    srcs = ["scripts/lint.sh"],
    data = [
        "//src:all_src_files",
        "//tests:all_test_files",
    ],
    size = "small",
)


# Formatting with black
sh_test(
    name = "format",
    srcs = ["scripts/format.sh"],
    data = [
        "//src:all_src_files",
        "//tests:all_test_files",
    ],
     size = "small",
)