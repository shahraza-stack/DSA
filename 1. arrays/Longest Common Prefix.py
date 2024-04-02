# Longest Common Prefix


def longestCommonPrefix(strs):
    result = ""
    for i in range(len(strs[0])):
        for str in strs:
            if i == len(str) or str[i] != strs[0][i]:
                return result
        result += strs[0][i]

    return result

strs = ["shah","shahaa","s"]

print(longestCommonPrefix(strs))
