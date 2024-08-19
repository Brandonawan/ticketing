from django.test import TestCase

# Create your tests here.
possible_issues =( 
    ("1", "Missing results"), 
    ("2", "Biodata update"), 
    ("3", "Assault"), 
)

# print(possible_issues)
for issue in possible_issues:
    print(issue[1])