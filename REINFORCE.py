# %%
#!%load_ext autoreload
#!%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from convert_pandas_html import transform_to_inline_styles


# %%
def REINFORCE_loss(pi_a, A):
    loss = -np.log(pi_a) * A
    return loss


def get_l_df():
    pi_as = np.linspace(0.01, 0.99, 3)
    As = np.linspace(-1, 1, 2)
    losses = []
    for A in As:
        row_lossses = []
        for pi_a in pi_as:
            l = REINFORCE_loss(pi_a, A)
            row_lossses.append(l)
        losses.append(row_lossses)

    df = pd.DataFrame(losses, columns=pi_as.astype(str), index=As.astype(str))
    df.index.name = "A"
    df.columns.name = "pi(a)"
    return df


def apply_style(df):
    def align_pn(x):
        return "text-align: right;"

    return (
        df.style.format(precision=2)
        .background_gradient(cmap="RdYlGn_r", axis=None)
        .map(align_pn)
    )


display(apply_style(get_l_df()))

# print(transform_to_inline_styles(apply_style(get_l_df()).to_html()))
# %%
