class Solution(object):
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(len(s1), len(s2)):

            new_char = ord(s2[i]) - ord('a')
            old_char = ord(s2[i - len(s1)]) - ord('a')

            count2[new_char] += 1
            count2[old_char] -= 1

            if count1 == count2:
                return True

        return False