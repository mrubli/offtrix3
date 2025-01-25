Getting images from LaMetric:

1. Go to https://developer.lametric.com/icons and search for the icon of your choice.
2. Remember the Icon ID.
3. Access your AWTRIX 3 device in the browser and go to the Icons tab.
4. Enter the Icon ID and download it.
5. Go to the Files tab and download (using right-click) the newly added icon from the ICONS directory.

Converting a PNG to a raw RGB565 file:
```
./image_to_rgb565.py 37235.png
```

Converting a raw RGB565 file into a C-style array:
```
./rgb565_to_c_array.py 37235.raw
```
