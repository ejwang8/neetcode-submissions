class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # ith car: position[i] + speed[i] * x = y

        # a   b    c --->

        # first need to sort increasing by position
        # then go reverse order (c->b->a) thru and compare times to finish
            # if stack empty, append (e.g. time_c)
            # if stack > 2 elems then 
                # if time_b < time_c then append time_b, otherwise leave as is
        # time to finish t is solved by target = position[i] + speed[i] * t

        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars = sorted(cars)
        fleets = [(target - cars[-1][0]) / cars[-1][1]]
        # cars = [[pos, sp] for [pos, sp] in zip(position, speed)]
        for i in range(len(cars)-1)[::-1]:
            # t = (target - position[i]) / speed[i]
            if (target - cars[i][0]) / cars[i][1] > fleets[-1]:
                fleets.append((target - cars[i][0]) / cars[i][1])

        return len(fleets)
