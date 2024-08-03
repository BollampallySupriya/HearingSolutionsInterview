from collections import OrderedDict


class NumberStore:
    def __init__(self):
        self.num_count = OrderedDict()
        self.duplicates = set()

    def add(self, number):
        if number in self.num_count:
            self.num_count[number] += 1
            self.duplicates.add(number)
        else:
            self.num_count[number] = 1

    def get_first_unique(self):
        for num in self.num_count:
            if num not in self.duplicates:
                return num
        return None


# Example usage
obj = NumberStore()
obj.add(2)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(1)
obj.add(3)
obj.add(4)
print(obj.get_first_unique())
