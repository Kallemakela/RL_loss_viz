# %%
#!%load_ext autoreload
#!%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from convert_pandas_html import transform_to_inline_styles


# %%
def ppo_loss(pi_as, pi_as_old, A, epsilon=0.1):
    ratio = pi_as / pi_as_old
    term1 = ratio * A
    ratio_clipped = np.clip(ratio, 1 - epsilon, 1 + epsilon)
    term2 = ratio_clipped * A
    loss = -np.min([term1, term2])
    return loss


def get_l_df(A):
    pi_as_olds = np.linspace(0.1, 0.9, 3)
    pi_as_curr = np.linspace(0.1, 0.9, 3)
    losses = []
    for pi_as_old in pi_as_olds:
        row_lossses = []
        for pi_as in pi_as_curr:
            l = ppo_loss(pi_as, pi_as_old, A)
            row_lossses.append(l)
        losses.append(row_lossses)

    df = pd.DataFrame(
        losses, columns=pi_as_curr.astype(str), index=pi_as_olds.astype(str)
    )
    df.index.name = "pi_old(a)"
    df.columns.name = "pi(a)"
    return df


def apply_style(df):
    return df.style.format(precision=2).background_gradient(cmap="RdYlGn_r", axis=None)


A = 1
print(f"Loss with A={A}")
display(apply_style(get_l_df(A)))

A = -1
print(f"Loss with A={A}")
apply_style(get_l_df(A))

# %%
# print(transform_to_inline_styles(apply_style(get_l_df(1)).to_html()))
# print(transform_to_inline_styles(apply_style(get_l_df(-1)).to_html()))
