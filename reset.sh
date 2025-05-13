#!/bin/sh
esptool.py --port /dev/ttyUSB0 --before default_reset --after hard_reset --no-stub run
