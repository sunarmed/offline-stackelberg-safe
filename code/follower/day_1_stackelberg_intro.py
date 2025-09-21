# offline-stackelberg-safe/notes/day1_stackelberg_basics.md

# Day 1 – Stackelberg Basics

## Goal
Understand classical Stackelberg games, leader–follower equilibrium, and solve a simple 2x2 example.

## Key References
- Vamvoudakis, Lewis, Dixon (2017). *Open-loop Stackelberg learning solution for hierarchical control problems.*
- Karwowski (2023). *Sequential Stackelberg Games with bounded rationality.*

## Concepts
- **Leader–follower structure:** The leader commits to a strategy first, the follower best-responds.
- **Stackelberg Equilibrium (SE):** Pair (leader strategy, follower strategy) where the leader anticipates the follower’s best response.
- **Difference from Nash:** Leader moves first, has an advantage by anticipating.

## Exercise
Solve the following payoff matrix game:

Leader (rows), Follower (columns)
```
        F1   F2
L1    (3,2) (1,0)
L2    (2,1) (0,3)
```
- Step 1: For each leader action, compute follower’s best response.
- Step 2: Knowing this, find the leader’s optimal commitment.

---

# offline-stackelberg-safe/code/follower/stackelberg_2x2.py

"""
Simple solver for a 2x2 Stackelberg game.
"""

def follower_best_response(payoff_matrix, leader_action):
    """
    Given leader_action index, return follower's best response index.
    payoff_matrix: dict mapping (L,F) -> (r_L, r_F).
    leader_action: 0 or 1 (L1 or L2).
    """
    best_f = None
    best_val = float('-inf')
    for f in [0, 1]:
        _, r_f = payoff_matrix[(leader_action, f)]
        if r_f > best_val:
            best_val = r_f
            best_f = f
    return best_f

def stackelberg_equilibrium(payoff_matrix):
    """
    Compute Stackelberg equilibrium in a 2x2 game.
    """
    best_leader_val = float('-inf')
    best_pair = None
    for l in [0, 1]:
        f = follower_best_response(payoff_matrix, l)
        r_l, r_f = payoff_matrix[(l, f)]
        if r_l > best_leader_val:
            best_leader_val = r_l
            best_pair = (l, f, r_l, r_f)
    return best_pair

if __name__ == "__main__":
    # Define payoff matrix as dictionary
    # (L,F) -> (r_L, r_F)
    payoff_matrix = {
        (0,0): (3,2),
        (0,1): (1,0),
        (1,0): (2,1),
        (1,1): (0,3),
    }
    l, f, r_l, r_f = stackelberg_equilibrium(payoff_matrix)
    print(f"Leader plays L{l+1}, Follower responds F{f+1}")
    print(f"Payoffs: Leader={r_l}, Follower={r_f}")
