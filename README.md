# RL-env-examples
Doing some reinforcement learning and a couple of examples. This is the default RL environment I will use for most examples for RL coming soon.

## The full learning algorithm (Maze running robot)
* Initialize G randomly     
* Repeat for number of episodes  
    * While game is not over   
         * Get state and reward from environment  
         * Select action  
         * Update environment   
         * Get updated state and reward  
         * Store new state and reward in memory   
    * Replay memory of previous episode to update G.
    *G state = G<sub>state</sub> + alpha(target - G<sub>state</sub>)*
    

    