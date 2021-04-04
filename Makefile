TEST_PATH=./

.EXPORT_ALL_VARIABLES:

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

test:
	python3 -m pytest tests/