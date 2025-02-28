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
def ppo_loss(pi_as, pi_as_old, A, epsilon=0.1):
    ratio = pi_as / pi_as_old
    term1 = ratio * A
    ratio_clipped = np.clip(ratio, 1 - epsilon, 1 + epsilon)
    # term2 = ratio_clipped * A
    term2 = term1
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


A = 1
print(f"Loss with A={A}")
df = apply_style(get_l_df(A))
display(df)
# dfi.export(df, f"fig/ppo_loss_A_{A}.png", dpi=300)

A = -1
print(f"Loss with A={A}")
df = apply_style(get_l_df(A))
display(df)
# dfi.export(df, f"fig/ppo_loss_A_{A}.png", dpi=300)
# %% Deltas


def get_loss_change_df(A, delta):
    pi_a_values = np.linspace(0.1, 0.9, 3)
    loss_changes = []
    for pi_a_old in pi_a_values:
        row_changes = []
        for pi_a_new in pi_a_values:
            loss_n = ppo_loss(pi_a_new + delta, pi_a_old, A)
            loss_o = ppo_loss(pi_a_new, pi_a_old, A)
            row_changes.append(loss_n - loss_o)
        loss_changes.append(row_changes)

    df = pd.DataFrame(
        loss_changes, columns=pi_a_values.astype(str), index=pi_a_values.astype(str)
    )
    df.index.name = "pi_old(a)"
    df.columns.name = "pi(a)"
    return df


delta = 0.01
A = 10
print(f"Loss Change with A={A}, delta={delta}")
df = apply_style(get_loss_change_df(A, delta), 2)
display(df)
# dfi.export(df, f"fig/ppo_loss_change_A_{A}_delta_{delta}.png", dpi=300)

A = -10
print(f"Loss Change with A={A}, delta={delta}")
df = apply_style(get_loss_change_df(A, delta), 2)
display(df)
# dfi.export(df, f"fig/ppo_loss_change_A_{A}_delta_{delta}.png", dpi=300)
# %%
