# drawh5: visualize .h5 files structure  
### Quickly visualize the entire structure of h5 files with information about dataset sizes and group relationships. This is a useful tool especially when using large h5 files.

## Example output:
<!-- <div style="text-align:center">
<img src="./resources/output.png" text-align="center">
</div> -->
<p align="center">
  <img src="./resources/output.png" alt="Sublime's custom image"/>
</p>

## Installation:
#### Clone:
```bash
https://github.com/X4ndri/drawh5.git
```

#### Using pip
```bash
# install requirements
pip install -r requirements
pip istall -e .
```
#### Note: This package is built on top of the h5py package, for more info:  h5py.readthedocs.io

## Usage:
### CLI:
```bash
drawh5 path_to_h5_file
```

### Python scripting
#### Can pass a file directory as input
```python
import drawh5
drawh5.drawh5(path_to_h5_file)
```
#### Can also pass an open h5 file object
```python
import drawh5
f = drawh5.h5.File(path_to_h5_file)
drawh5.drawh5(f)
f.close()
```