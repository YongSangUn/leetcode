#
# @lc app=leetcode id=192 lang=bash
#
# [192] Word Frequency
#

# @lc code=start
# Read from the file words.txt and output the word frequency list to stdout.

sed 's/^ \+//g;s/ \+$//g;s/ \+/\n/g;/^$/d' words.txt |
    sort |
    uniq -c |
    sort -nr |
    awk '{print $2,$1}'

# @lc code=end
