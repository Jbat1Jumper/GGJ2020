set -e

pyinstaller -wF start.py

cp -r assets dist/assets
