#!/usr/bin/env bash

set -e
python -m aerich upgrade
exec "$@"