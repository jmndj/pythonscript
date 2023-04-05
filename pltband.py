#!/usr/bin/python

from vaspvis import standard

results = standard.band_dos_elements(
    band_folder="./band/band_1",
    dos_folder="./dos/dos_1",
    elements=['H',],
    save=True,
    output='band_dos_1elements.png',
    # shift_efermi=1.833463
    shift_efermi=5,
)
