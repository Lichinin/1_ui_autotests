#!/bin/bash
cd ..
pytest --reruns 2 --reruns-delay 1
read -p "Press enter to continue"