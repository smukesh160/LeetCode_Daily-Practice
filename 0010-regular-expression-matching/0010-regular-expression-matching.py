from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def match(i: int, j: int) -> bool:
            # Pattern exhausted: input must also be exhausted.
            if j == len(p):
                return i == len(s)

            first_matches = (
                i < len(s) and
                (p[j] == s[i] or p[j] == ".")
            )

            # The current pattern character is followed by '*'.
            if j + 1 < len(p) and p[j + 1] == "*":
                return (
                    match(i, j + 2) or              # Use zero occurrences.
                    (first_matches and match(i + 1, j))  # Use one or more.
                )

            return first_matches and match(i + 1, j + 1)

        return match(0, 0)