# topnames - Most popular baby names by birth year

This is a simple sample Python program used for demonstration purposes
at FARCON 2016. It reads data on the most popular baby names by birth
year from data provided by the Social Security Administration, and
display the most popular girl's name and most popular boy's name for
each year.

The data is available from
https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data

The data is a ZIP file containing one text data file for each year of
birth 1880–2015, as well as a readme file. For each year of birth,
there is a text file of the form yob1900.txt, which contains a list of
baby names, based on Social Security card applications, one per
line. Each line includes the name, gender, and count of applications
with that name. The girls' names are provided first and the boys'
names second. Within each section, the names are sorted with the most
popular names first.

topnames2.py is a version of the program with sample code for writing
the results to .csv and .xlsx files.