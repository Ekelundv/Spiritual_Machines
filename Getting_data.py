import quandl as ql
import numpy as np
import pandas as pd


X = 1
Y = 1


if ((not isinstance(X, np.ndarray)) and (not isinstance(X, pd.core.frame.DataFrame))  #
        and (not isinstance(X, pd.core.series.Series))):
    raise ValueError("invalid type. Please input Numpy narray or Pandas DataFrame.")

if isinstance(X, pd.core.series.Series) or isinstance(X, pd.core.frame.DataFrame):
    X = X.values
    Y = Y.values
































