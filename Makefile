.PHONY: clean train kill-action-server action-server stop-duckling run-duckling shell server test test-ci-core-nlu test-ci-functional interactive-training cloud-train cloud-server

TEST_PATH=./

.EXPORT_ALL_VARIABLES:

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

test:
	python3 -m pytest tests/