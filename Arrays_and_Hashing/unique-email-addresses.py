# https://leetcode.com/problems/unique-email-addresses

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            res.add(local_name + "@" + domain_name)

        return len(res)


# Time Complexity: O(n)
# Space Complexity: O(n)
