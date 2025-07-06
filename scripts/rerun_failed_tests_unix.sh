#!/bin/bash
cd ..
pytest --last-failed
read -p "Press enter to continue"