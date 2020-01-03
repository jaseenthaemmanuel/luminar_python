#regular expression

import re
# count=0
# matcher=re.finditer('ab','abaababa')
# for match in matcher:
#     print(match)
#     print("match available at",match.start())
#     print("group=",match.group())
#     count+=1
#     print("count=",count)

# x='[abc]'
# x='[^abc]'
# x='[a-z]'
# x='[A-Z]'
# x='[0-9]'
x='[a-zA-z0-9]'
matcher=re.finditer(x,'a7b @k9az')
for match in matcher:
    print("match available at",match.start())
    print("group=",match.group())