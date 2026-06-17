class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pos = [1, 4]
        # spd = [3, 2]

        # cars = [(4, 2), (1, 3)]

        cars = sorted(zip(position, speed), reverse=True)
        time = []

        for p, s in cars:
            t = (target - p) / s
            if time and t <= time[-1]:
                continue
            time.append(t)
        print(time)
            

        return len(time)
