#! /bin/bash

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo ""
echo "Downloading pal-camera libraries..."
echo ""

ggID='1pucLRZQr3_lAkMGuzt9zrHUKyTS7ULGd'
ggURL='https://drive.google.com/uc?export=download'

filename="$(curl -sc /tmp/gcokie "${ggURL}&id=${ggID}" | grep -o '="uc-name.*</span>' | sed 's/.*">//;s/<.a> .*//')"

gdown --id ${ggID}

echo ""
echo "Unzipping files..."
echo ""

unzip ${filename} -d ./dev_ws/src/dreamvu_pal_camera

rm "${filename}"

echo ""
echo "Done, pal-camera libraries are kept in 'src/dreamvu_pal_camera/lib'."
echo ""