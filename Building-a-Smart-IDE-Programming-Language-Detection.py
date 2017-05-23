"""Detecting C, Java or Python."""
import sys

code = sys.stdin.read()

if "#include" in code:
    print "C"
elif "java" in code:
    print "Java"
else:
    print "Python"
