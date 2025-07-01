# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/description/


from collections import Counter
import math


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons: dict[str, float] = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0,
        }
        for char in text:
            count = balloons.get(char, None)
            if count is None:
                continue
            add = 0.5 if char == "l" or char == "o" else 1
            balloons[char] += add
        return min(math.floor(count) for count in balloons.values())

    # Time Cx: O(n), Space Cx: O(1) since there only exists
    # 25 characters in the alphabet
    def maxNumberOfBalloons2(self, text: str) -> int:
        text_counter = Counter(text)
        return min(
            text_counter.get("b", 0),
            text_counter.get("a", 0),
            text_counter.get("l", 0) // 2,
            text_counter.get("o", 0) // 2,
            text_counter.get("n", 0),
        )

    # Time Cx: O(n), Space Cx: O(1)
    def maxNumberOfBalloons3(self, text: str) -> int:
        return min(
            text.count("b"),
            text.count("a"),
            text.count("l") // 2,
            text.count("o") // 2,
            text.count("n"),
        )


sol = Solution()
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
res = sol.maxNumberOfBalloons3(text)
print(res)
