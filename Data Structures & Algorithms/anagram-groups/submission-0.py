class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        # initialize the "key" of the curr string
        count = [0] * 26

        # initialize hash
        hash = {}
        
        for string in strs:
            # set the "key" to the correct count of the letters in the string
            # if the key is already in the hash map, then add the string to the mapping
            # else, initialize it and map the string to the key
            # then set "key" back to [0] * 26
            for letter in string:
                count[ord(letter) - 97] += 1
            key = tuple(count)

            if key in hash:
                hash[key].append(string)
            else:
                hash[key] = [string]

            count = [0] * 26

        return [hash[x] for x in hash]