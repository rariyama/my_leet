class Solution:
    def __init__(self):
        self.symbol = {
            '1': 'I',
            '5': 'V',
            '10': 'X',
            '50': 'L',
            '100': 'C',
            '500': 'D',
            '1000': 'M'
        }
    
    def first_digit(self, num) -> str:
        if num < 4:
            return self.symbol['1'] * num
        elif num == 4:
            return self.symbol['1'] + self.symbol['5']
        elif num >= 5 and num < 9:
            return self.symbol['5'] + self.symbol['1'] * (num-5)
        elif num == 9:
            return self.symbol['1'] + self.symbol['10']
    
    def second_digits(self, num) -> str:
        numbers = [int(i) for i in str(num)]
        first_num = numbers[0]
        second_num = numbers[1]
        ans = ''
        if first_num < 4:
            ans += self.symbol['10'] * first_num
        elif first_num == 4:
            ans += self.symbol['10'] + self.symbol['50']
        elif first_num >= 5 and first_num < 9:
            ans += self.symbol['50'] + self.symbol['10'] * (first_num-5)
        elif first_num == 9:
            ans += self.symbol['10'] + self.symbol['100']
        if second_num == 0:
            return ans
        else:
            s_digit = self.first_digit(second_num)
            return ans + s_digit

    def third_digits(self, num) -> str:
        numbers = [int(i) for i in str(num)]
        first_num = numbers[0]
        second_num = numbers[1]
        third_num = numbers[2]
        ans = ''
        if first_num < 4:
            ans += self.symbol['100'] * first_num
        elif first_num == 4:
            ans += self.symbol['100'] + self.symbol['500']
        elif first_num >= 5 and first_num < 9:
            ans += self.symbol['500'] + self.symbol['100'] * (first_num-5)
        elif first_num == 9:
            ans += self.symbol['100'] + self.symbol['1000']
        if second_num == 0 and third_num == 0:
            return ans
        elif second_num == 0 and third_num != 0:
            f_digit = self.first_digit(third_num)
            return ans + f_digit
        else:
            s_digit = self.second_digits(int((str(second_num).ljust(2, '0'))))
            f_digit = self.first_digit(third_num)
            return ans + s_digit + f_digit


    def fourth_digits(self, num) -> str:
        numbers = [int(i) for i in str(num)]
        first_num = numbers[0]
        second_num = numbers[1]
        third_num = numbers[2]
        fourth_num = numbers[3]
        ans = ''
        if first_num < 4: 
            ans += self.symbol['1000'] * first_num
        if second_num == 0 and third_num == 0 and fourth_num == 0:
            return ans
        elif second_num == 0 and third_num == 0 and fourth_num != 0:
            f_digit = self.first_digit(fourth_num)
            return ans + f_digit
        elif second_num == 0 and third_num != 0:
            third_value = int((str(third_num)+str(fourth_num)).ljust(3, '0'))
            s_digit = self.second_digits(third_value)
            return ans + s_digit
        else:
            third_value = int((str(second_num)+str(third_num)).ljust(3, '0'))
            t_digit = self.third_digits(third_value)
            f_digit = self.first_digit(fourth_num)
        return ans + t_digit + f_digit

    def intToRoman(self, num: int) -> str:
        num_length = len(str(num))
        if num_length == 1:
            return self.first_digit(num)
        elif num_length == 2:
            return self.second_digits(num)
        elif num_length == 3:
            return self.third_digits(num)
        elif num_length == 4:
            return self.fourth_digits(num)

def main():
    test_data = {'3': 'III',
                 '4': 'IV',
                 '5': 'V',
                 '6': 'VI',
                 '9': 'IX'
                 }
    for v in test_data:
        res = Solution().intToRoman(int(v))
        assert res == test_data[v]
    print('first digit is succeeded!')

    test_data = {'32': 'XXXII',
                 '45': 'XLV',
                 '58': 'LVIII',
                 '66': 'LXVI',
                 '91': 'XCI',
                 '10': 'X',
                 '20': 'XX',
                 '50': 'L',
                 '60': 'LX',
                 '90': 'XC'}
    for v in test_data:
        res = Solution().intToRoman(int(v))
        assert res == test_data[v]
    print('second digit is succeeded!')

    test_data = {'246': 'CCXLVI',
                 '438': 'CDXXXVIII',
                 '597': 'DXCVII',
                 '616': 'DCXVI',
                 '975': 'CMLXXV',
                 '100': 'C',
                 '101': 'CI',
                 '110': 'CX',
                 '200': 'CC',
                 '400': 'CD',
                 '500': 'D',
                 '900': 'CM'
                 }
    for v in test_data:
        res = Solution().intToRoman(int(v))
        assert res == test_data[v]
    print('third digit is succeeded!')

    test_data = {'1991': 'MCMXCI',
                 '2754': 'MMDCCLIV',
                 '3819': 'MMMDCCCXIX',
                 '1000': 'M',
                 '1001': 'MI',
                 '1010': 'MX',
                 '1101': 'MCI'
                 }
    for v in test_data:
        res = Solution().intToRoman(int(v))
        assert res == test_data[v]
    print('fourth digit is succeeded!')



if __name__ == '__main__':
    main()