#!/usr/bin/env bash

# Emit the current Asia/Bangkok timestamp in ISO-8601 format.
set -euo pipefail

format="${1:-%Y-%m-%dT%H:%M:%S%z}"
TZ=Asia/Bangkok date +"${format}"
