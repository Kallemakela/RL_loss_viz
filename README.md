# Visualizing RL Loss Functions

## PPO loss

loss = -min(ratio * A, clip(ratio, 1 - e, 1 + e) * A)

ratio = pi(a) / pi_old(a)

e = 0.1

#### A=1

![](fig/ppo_loss_A_1.png)

#### A=-1

![](fig/ppo_loss_A_-1.png)

### Loss deltas

This shows how much the loss changes when pi(a) changes by +0.01. The diagonal is the most relevant as it won't get clipped and the non-clipped are the same on each row since:
L_delta = (pi_a + delta) * A - pi_a * A = delta * A. 

#### A=10

![](fig/ppo_loss_change_A_10_delta_0.01.png)

#### A=-10

![](fig/ppo_loss_change_A_-10_delta_0.01.png)

- Improvement where pi_old(a) is low results in much bigger loss changes.
- The loss gets clipped where the improvement is high with and without delta resulting in delta=0.

## REINFORCE loss

loss = -log(pi(a)) * A

![](fig/REINFORCE_loss.png)

#### Loss Delta

This shows how much the loss changes when pi(a) changes by +0.01.

![](fig/REINFORCE_loss_change_0.01.png)

- The loss changes drastically more when pi(a) is low since log(pi(a)) grows hyperbolically as pi(a) approaches 0.
