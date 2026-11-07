class Solution:
    def countSeniors(self, details: List[str]) -> int:
        numofseniors = 0
        for i in details:
            if int(i[11:13]) > 60:
                numofseniors += 1
        return numofseniors


        