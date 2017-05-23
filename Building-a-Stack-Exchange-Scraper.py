import re

question_number = r'(?<=questions\/)\d+'
question_text = r'(?<="question-hyperlink">)([^\<]+)(?=\<)'
question_time = r'(?<=class="relativetime">)(.+)(?=\<)'

# Read HackerRank's fucked up standard input
text = str()
while True:
    try:
        text += raw_input()
    except:
        break

numbers = re.findall(question_number, text)
texts = re.findall(question_text, text)
times = re.findall(question_time, text)

result = zip(numbers, texts, times)

for i in xrange(len(result)):
    print ';'.join(result[i])
