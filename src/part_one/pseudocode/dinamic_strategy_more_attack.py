/*
 * Receives: Index of Damage Table representing a state in the game and the Damage Table
 * Returns: Priority list of attacks for that specific state of the game
 * 
 * KnownStates is a global variable known by the Game, that contains all priority list previusly calculated.
 */

def step(state, damage_table):
   priority_list = []
   if (state exists in KnownStates):
       return KnownStates[state]
   else
       priority_list = order_by_max_damage(damage_table[state])
       KnownStates[state] = priority_list
   return priority_list
