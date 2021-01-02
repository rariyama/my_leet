class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create hashmap for recording count of character in string.
        counter_r = {}
        for i in ransomNote:
            if i not in counter_r:
                counter_r[i] = 1
            else:
                counter_r[i] += 1
        counter_m = {}
        for i in magazine:
            if i not in counter_m:
                counter_m[i] = 1
            else:
                counter_m[i] += 1

        # if ransomNote is bigger, magazine can't cover all words of ransom
        if len(ransomNote) > len(magazine):
            return False
        # if ransomNote is only empty string, \
        # it means that ransom doesn't need to use any char for covering.
        elif ransomNote == "":
            return True
        else:
            count = 0
            for char in counter_r.keys():
                if char not in magazine:
                    return False
                # if count of char in magazine is bigger than or equal that of ransom
                # add true count and if the count is bigger than length of magazine char
                # return True
                elif counter_r[char] <= counter_m[char]:
                    count += 1
            if count >= len(counter_r):
                return True
            else:
                return False