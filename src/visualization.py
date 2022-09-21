from enum import Enum, auto
from typing import TypeVar, Tuple, Iterable, Optional, Callable
from itertools import starmap

import numpy as np
import plotly.graph_objects as go

from src.preprocessing import LabelCropp
from rowwise_metrics import rowwise_cosine

T = TypeVar('T')

class IndexType(Enum):
  """
  Class describing types of index to two dimensional space mappings.
  """
  HORIZONTAL_SNAKE = auto()
  VERTICAL_SNAKE   = auto()
  HORIZONTAL       = auto()
  VERTICAL         = auto()

  
  
def reshape(values:np.array, dim: Tuple[int, int], index_type: IndexType) -> np.array:
  """
  Modifies values!
  """
  if index_type in [IndexType.VERTICAL_SNAKE, IndexType.VERTICAL]:
    values = np.resize(values, dim[::-1]).transpose()
  else:
    values = np.resize(values, dim)

  if index_type == IndexType.HORIZONTAL_SNAKE:
    values[1::2, :] = values[1::2, ::-1]
  elif index_type == IndexType.VERTICAL_SNAKE:
    values[:, 1::2] = values[::-1, 1::2]

  return values


def plot_map(values: np.array,                                                 
             dim: Tuple[int, int],                                      
             index_type: IndexType=IndexType.HORIZONTAL,
             transpose=False,
             only_values=False,
             title: Optional[str]=None,
             *args,
             **kwargs,                                                      
             ):
  values = reshape(values, dim, index_type)
  if transpose:
    values = np.transpose(values)
      
  if only_values:
    return values

  fig = go.Figure(data=go.Heatmap(
        z=values,
        *args,
        **kwargs))

  fig.update_layout(
    title=title,
  )

  return fig


def error_map(y_true: Iterable[T],                                             
              y_pred: Iterable[T],
              dim: Tuple[int, int],                                            
              index_type: IndexType=IndexType.HORIZONTAL, 
              rowwise_error: Callable[[Iterable[T], Iterable[T]], Iterable[float]]=rowwise_cosine,                                          
              title: Optional[str]=None,                                                                                    
              add_stats: bool=False,
              *args,
              **kwargs                                         
              ):
  values = rowwise_error(y_true, y_pred)

  if add_stats:
    if not title:
      title = ''
    title += ' (avg: {}, min: {}, max: {})'.format(np.mean(values), np.min(values), np.max(values))

  return plot_map(values, dim, index_type, *args, **kwargs)


def intensity_map(spectra: np.array,
                  dim: Tuple[int, int],                                            
                  index_type: IndexType=IndexType.HORIZONTAL,                                  
                  start: Optional[T]=None,                                 
                  end: Optional[T]=None,                                   
                  calibration: Optional[Iterable[T]]=None,
                  *args,
                  **kwargs
                  ):
  values = spectra_intensity(spectra, start, end, calibration)

  return plot_map(values, dim, index_type, *args, **kwargs)


def spectra_intensity(spectra: np.array,                                     
                      start: Optional[T]=None,                                 
                      end: Optional[T]=None,                                   
                      calibration: Optional[Iterable[T]]=None,                 
                      ) -> Iterable[float]:
    if calibration is None:
      calibration = np.arange(spectra.shape[0])
    if start is None:
      start = calibration[0]
    if end is None:
      end = calibration[-1]

    return np.sum(LabelCropp(label_from=start, label_to=end, labels=calibration).fit_transform(spectra), axis=1)
    
    
def id_from_snake_index(x, y, dim):
  return y * dim[1] + (x if not y % 2 else dim[1] - x - 1)