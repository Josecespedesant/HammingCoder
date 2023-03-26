first_parity_digits = [2, 4, 6, 8, 10, 12, 14]
second_parity_digits = [2, 5, 6, 9, 10, 13, 14]
third_parity_digits = [4, 5, 6, 11, 12, 13, 14]
fourth_parity_digits = [8, 9, 10, 11, 12, 13, 14]

digits_groups = [first_parity_digits, second_parity_digits,
                 third_parity_digits, fourth_parity_digits]

binary_numbers = ["0001", "0010", "0011", "0100",
                  "0101", "0110", "0111", "1000",
                  "1001", "1010", "1011", "1100",
                  "1101", "1110", "1111"]


def is_binary(string):
    """
    Checks if the strings has just 0's and 1's.

    :param string: A binary string
    :return: True if binary, otherwise False
    """
    for bit in string:
        if bit == "0" or bit == "1":
            continue
        else:
            return False
    return True


class HammingVerifier:
    _string = ""
    _received_parity_1 = ""
    _received_parity_2 = ""
    _received_parity_3 = ""
    _received_parity_4 = ""
    _new_parity_1 = ""
    _new_parity_2 = ""
    _new_parity_3 = ""
    _new_parity_4 = ""
    _error_bit_position = -1
    _is_even = True

    def get_parities(self):
        """
        Put all parities old and new ones on a matrix.

        :return: The parities' matrix.
        """
        new_parity_list = [self._new_parity_1, self._new_parity_2, self._new_parity_3, self._new_parity_4]
        old_parity_list = [self._received_parity_1, self._received_parity_2, self._received_parity_3,
                           self._received_parity_4]
        parities_list = [new_parity_list, old_parity_list]

        return parities_list

    def check_parity(self, string_with_error, is_even):
        """
        Public function that calls all other private subprocess.

        :param string_with_error: The string given by the user that contains an error bit.
        :param is_even: True is parity is even, otherwise False\
        """
        if len(string_with_error) == 15:
            if is_binary(string_with_error):
                self._string = string_with_error
                self._is_even = is_even
                self._set_received_parity()
                self._set_new_parity()
                self._compare_parities()

        return self._error_bit_position

    def _compare_parities(self):
        """
        Checks the four digits of parity of both given and analyzed string to find the error bit position.
        """
        error_position = ""
        error_position += "0" if self._received_parity_4 == self._new_parity_4 else "1"
        error_position += "0" if self._received_parity_3 == self._new_parity_3 else "1"
        error_position += "0" if self._received_parity_2 == self._new_parity_2 else "1"
        error_position += "0" if self._received_parity_1 == self._new_parity_1 else "1"

        digit_position = 1
        for number in binary_numbers:
            if error_position == number:
                self._error_bit_position = digit_position
                break
            digit_position += 1

    def _set_received_parity(self):
        """
        Set the wrong received parity as class attributes.
        """
        self._received_parity_1 = self._string[0]
        self._received_parity_2 = self._string[1]
        self._received_parity_3 = self._string[3]
        self._received_parity_4 = self._string[7]

    def _set_new_parity(self):
        """
        Analyses the parity of the string to compare it with the given one.
        """
        parity_group = 1
        for group in digits_groups:
            counter = 0
            for position in group:
                if self._string[position] == "1":
                    counter += 1

            self._set_parity_aux(counter, parity_group)
            parity_group += 1

    def _set_parity_aux(self, counter, group):
        """
        Auxiliar to set each new parity bit.

        :param counter: The amount of 1's.
        :param group: The bit parity being calculated.
        """
        if self._is_even:
            new_parity = "0" if counter % 2 == 0 else "1"
        else:
            new_parity = "1" if counter % 2 == 0 else "0"

        match group:
            case 1:
                self._new_parity_1 = new_parity
            case 2:
                self._new_parity_2 = new_parity
            case 3:
                self._new_parity_3 = new_parity
            case 4:
                self._new_parity_4 = new_parity
