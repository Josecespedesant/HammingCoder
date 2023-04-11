from enum import Enum


class Parity(Enum):
    ODD = 2
    EVEN = 1


def num_to_list(num):
    list_of_binaries = [int(i) for i in str(num)]
    if len(list_of_binaries) < 11:
        while len(list_of_binaries) != 11:
            list_of_binaries.insert(0, 0)
    if len(list_of_binaries) > 11:
        return -1
    return list_of_binaries


def has_only_binary_numbers(num):
    return all(n == '1' or n == '0' for n in num)


# Format (15,11)
class HammingEncoder:
    positions = ["0001", "0010", "0011", "0100",
                 "0101", "0110", "0111", "1000",
                 "1001", "1010", "1011", "1100",
                 "1101", "1110", "1111"]

    def __init__(self, parity: Parity = Parity.EVEN):
        self._parity = parity
        self._parity_positions = [0, 1, 3, 7]
        self.trace = [[], [], [], []]

    def get_trace(self):
        return self.trace

    def _assign_parity_position_trace(self, parity_position, list_for_parity):
        self.trace[parity_position] = list_for_parity

    def _adjust_amount_of_bits(self, num):
        for index in range(15):
            if index in self._parity_positions:
                num.insert(index, 2)
        return num

    def _assign_parity_bits(self, num):
        data_position_index = 3
        parity_position = 0
        while data_position_index >= 0:
            list_for_parity = []
            for index in range(15):
                if index not in self._parity_positions and int(self.positions[index][data_position_index]) == 1:
                    list_for_parity.append(num[index])
                    continue
                list_for_parity.append(None)
            amount_of_ones = list_for_parity.count(1)
            self._assign_parity_position_trace(parity_position, list_for_parity)
            num = self._assign_parity_bit(amount_of_ones, parity_position, num)

            data_position_index -= 1
            parity_position += 1
        return num

    def _assign_parity_bit(self, amount_of_ones, parity_position, num):
        if self._parity == Parity.ODD:
            if amount_of_ones % 2 == 0:
                num[self._parity_positions[parity_position]] = 1
            else:
                num[self._parity_positions[parity_position]] = 0
            return num
        if amount_of_ones % 2 != 0:
            num[self._parity_positions[parity_position]] = 1
        else:
            num[self._parity_positions[parity_position]] = 0
        return num

    def encode_list(self, num):
        if not num or len(num) != 11:
            return -1
        num = self._adjust_amount_of_bits(num)
        num = self._assign_parity_bits(num)
        return num

    def encode(self, num):
        if isinstance(num, int):
            num = num_to_list(num)
        if not has_only_binary_numbers(num) and not isinstance(num, list):
            return -1
        return self.encode_list(num)
