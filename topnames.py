# topnames.py - Read most popular names by year from Social Security card applications.

greeting="""
FARCON 2016
August 24, 2016

Sample Python program to read and display the most popular baby names by year.
For each year of birth, the most popular girl's name and the most popular
boy's name is shown. Based on data from Social Security card applications.
"""

import zipfile
import io
import re


def processline(s):
    """Parses line in the form name,sex,count and returns components"""
    b = s.split(",")
    name =  b[0]
    sex =   b[1].upper()
    count = int(b[2])
    return name,sex,count


def getnames(f):
    """Read text stream f and obtain the most popular girls' and boys' names."""
    # Assumes file is sorted with girl names first, boy names second, and the
    # most popular name at the top of each list.

    lineoftext = f.readline()
    girlname,sex,count = processline(lineoftext)

    while sex != "M":
        name,sex,count = processline(f.readline())
    boyname=name

    return girlname,boyname


def process_socsec_zipfile(filepath='names.zip'):
    "Returns dictionary with most popular girl's and boy's name each year"
    topnames = dict()
    zf = zipfile.ZipFile(filepath)

    for filename in zf.namelist():
        m = re.match(r'yob([0-9]+)\.txt$',filename)
        if m:
            year = int(m.group(1))
            with zf.open(filename) as zfile:
                with io.TextIOWrapper(zfile) as f:
                    girlname,boyname = getnames(f)
            topnames[year] = (girlname,boyname)

    return topnames


def display_topnames(topnames):
    print("Year       Top Girl's Name   Top Boy's Name")
    for year in range(1880,2016):
        if year in topnames:
            display = "{year:4d}       {girl:<15s}   {boy:<15s}".format(
                year=year, girl=topnames[year][0], boy=topnames[year][1] )
            print(display)


def main():
    print(greeting)
    topnames = process_socsec_zipfile("names.zip")
    display_topnames(topnames)
    print("End")


if __name__=="__main__":
    main()
