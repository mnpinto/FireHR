# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_cli.ipynb (unless otherwise specified).

__all__ = ['firehr_from_banet_events']

# Cell
from pathlib import Path
import re
import numpy as np
from fastscript import *
from fire_split.core import save_data
from .data import get_event_data
from .predict import get_preds

# Cell
@call_parse
def firehr_from_banet_events(
        file:Param("BA-Net event tif file",str),
        path:Param("Path to save outputs",str)='.',
        composite_days_before:Param("Time window for composite before fire",int)=120,
        composite_days_after:Param("Time window for composite after fire",int)=120,
        max_cloud_fraction:Param("Maximum fraction of cloud pixels",float)=None,
        use_least_cloudy:Param("Number of least cloudy images to use",int)=None,
        topography:Param("Download also topography for the event region",bool)=False,
        skip_preds:Param("Skip computation of high resolution burned area", bool)=False):
    path = Path(path)
    path.mkdir(exist_ok=True, parents=True)
    event_id = '_'.join(Path(file).stem.split('_')[1:])
    year = int(re.findall('(\d{4})', Path(file).stem.split('_')[1])[0])
    if topography in [True, 'true', 'True', 'TRUE']: topography = True
    im, transform, crs = get_event_data(
        event_id, year, file, composite_days=[composite_days_before,composite_days_after],
        max_cloud_fraction=max_cloud_fraction, use_least_cloudy=use_least_cloudy, path=path,
        topography=topography)
    if not skip_preds:
        preds = get_preds(im, gpu=False)
    save_data(path/f'{event_id}/firehr_{event_id}.tif', (preds*255).astype(np.uint8), crs=crs, transform=transform)