#
# @lc app=leetcode id=193 lang=bash
#
# [193] Valid Phone Numbers
#

# @lc code=start
# Read from the file file.txt and output all valid phone numbers to stdout.

awk '$0 ~ /^([0-9]{3}-){2}[0-9]{4}$/ || $0 ~ /^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/ {print $0}' file.txt

# @lc code=end
