# %%
#!%load_ext autoreload
#!%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
import dataframe_image as dfi
from utils import apply_style


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


# display(apply_style(get_l_df()))
# print(transform_to_inline_styles(apply_style(get_l_df()).to_html()))

df = apply_style(get_l_df())
display(df)
dfi.export(df, f"fig/REINFORCE_loss.png", dpi=300)
# %% Deltas


def get_loss_change_df(delta):
    pi_as = np.linspace(0.01, 0.99, 3)
    As = np.linspace(-1, 1, 2)
    deltas = []
    for A in As:
        row_deltas = []
        for pi_a in pi_as:
            loss_n = REINFORCE_loss(pi_a + delta, A)
            loss_o = REINFORCE_loss(pi_a, A)
            delta_loss = loss_n - loss_o
            row_deltas.append(delta_loss)
        deltas.append(row_deltas)

    df = pd.DataFrame(deltas, columns=pi_as.astype(str), index=As.astype(str))
    df.index.name = "A"
    df.columns.name = "pi(a)"
    return df


delta = 0.01
print(f"Loss Change with pi(a) delta={delta}")
df = apply_style(get_loss_change_df(delta), 2)
display(df)
# dfi.export(df, f"fig/REINFORCE_loss_change_{delta}.png", dpi=300)
