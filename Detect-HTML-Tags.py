import re

# test_string_1 = '2'
# test_string_2 = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>'
# test_string_3 = '<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>'

# Parse all the input lines from HackerRank's weird format
html = str()

for _ in range(int(raw_input())):
    html += raw_input()

# Regular expression to match HTML tags
regex = r"(?<=<|\/)\w+(?=>|\s)"

# Find all the matches
matches = re.findall(regex, html)

# We just want the unique matches, sorted alphabetically
unique_sorted_matches = sorted(set(matches))

# Tweak the output as required by the problem formulation
results = ';'.join(unique_sorted_matches)

print results
