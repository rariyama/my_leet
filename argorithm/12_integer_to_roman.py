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
            return 'IV'        
        elif num >= 5 and num < 9:
            return 'V' + self.symbol['1'] * (num-5)
        elif num == 9:
            return 'IX' 
    
    def second_digits(self, num) -> str:
        numbers = [int(i) for i in str(num)]
        first_num = numbers[0]
        second_num = numbers[1]
        ans = ''
        if first_num < 4:
            ans += self.symbol['10'] * first_num
        elif first_num == 4:
            ans += 'XL'
        elif first_num >= 5 and first_num < 9:
            ans += 'L' + self.symbol['10'] * (first_num-5)
        elif first_num == 9:
            ans += 'XC'
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
            ans += 'CD'
        elif first_num >= 5 and first_num < 9:
            ans += 'D' + self.symbol['100'] * (first_num-5)
        elif first_num == 9:
            ans += 'CM'
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
    input = [3, 4, 5, 6, 9]
    collects = ['III', 'IV', 'V', 'VI', 'IX']
    for i, v in enumerate(input):
        res = Solution().intToRoman(v)
        assert res == collects[i]
    print('first digit is succeeded!')

    input = [32, 45, 58, 66, 91, 10, 20, 50, 60, 90]
    collects = ['XXXII', 'XLV', 'LVIII', 'LXVI', 'XCI', 'X', 'XX', 'L', 'LX', 'XC']
    for i, v in enumerate(input):
        res = Solution().intToRoman(v)
        assert res == collects[i]
    print('second digit is succeeded!')

    input = [246, 438, 597, 616, 975, 100, 101, 110, 200, 400, 500, 900]
    collects = ['CCXLVI', 'CDXXXVIII', 'DXCVII', 'DCXVI', 'CMLXXV', 'C', 'CI', 'CX', 'CC', 'CD', 'D', 'CM']
    for i, v in enumerate(input):
        res = Solution().intToRoman(v)
        assert res == collects[i]
    print('third digit is succeeded!')

    input = [1991, 2754, 3819, 1000, 1001, 1010, 1101]
    collects = ['MCMXCI', 'MMDCCLIV', 'MMMDCCCXIX', 'M', 'MI', 'MX', 'MCI']
    for i, v in enumerate(input):
        res = Solution().intToRoman(v)
        assert res == collects[i]
    print('fourth digit is succeeded!')



if __name__ == '__main__':
    main()