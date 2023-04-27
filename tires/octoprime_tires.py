from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        sum_wear = 0
        for tire in self.wear:
            sum_wear += tire
        return True if sum_wear >= 3 else False
