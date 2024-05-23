import re

text = "We are what we pretend to be, so we must be careful about what we pretend to be."
result = re.search('\w{7}',text)# Matches any word character (alphanumeric & underscore) that occurs exactly 7 times
matched_text = result.group(0)

print(matched_text)

