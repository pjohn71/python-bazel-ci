#!/bin/bash
set -e

# Install black
pip install black==25.1.0

# Run the check but don't fail the build
black --check src/ tests/ 
exit 0