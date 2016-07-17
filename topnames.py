# topnames.py - Read most popular names by year from Social Security card applications.

greeting="""
FAR Con
August 24, 2016

Read and display the most popular baby names by year.
For each year of birth, the most popular girl's name and the most
popular boy's name is shown.
Based on data from Social Security card applications.
"""

import zipfile
import re


def processline(s):
    """Parses line in the form name,sex,count and returns components"""
    b = s.split(",")
    name =  b[0]
    sex =   b[1].upper()
    count = int(b[2])
    return name,sex,count


def getnames(f):
    """Read file f and obtain the most popular girls' and boys' names."""
    # Assumes file is sorted with girl names first, boy names second, and the
    # most popular name at the top of each list.

    lineoftext = f.readline().decode()
    girl,sex,count = processline(lineoftext)

    while sex != "M":
        name,sex,count = processline(f.readline().decode())
    boy=name

    return girl,boy


def process_socsec_zipfile(filepath='names.zip'):
    "Returns dictionary with most popular girl's and boy's name each year"
    d = dict()
    zf = zipfile.ZipFile(filepath)

    for filename in zf.namelist():
        m = re.match("yob([0-9]+)\.txt",filename)
        if m:
            year = int(m.group(1))
            with zf.open(filename) as f:
                girl,boy = getnames(f)
            d[year] = (girl,boy)

    return d


def display_topnames(topname):
    print("Year       Top Girl's Name   Top Boy's Name")
    for year in range(1880,2016):
        if year in topname:
            display = "{year:4d}       {girl:<15s}   {boy:<15s}".format(
                year=year, girl=topname[year][0], boy=topname[year][1] )
            print(display)


def main():
    print(greeting)
    topname = process_socsec_zipfile("names.zip")
    display_topnames(topname)
    print("End")


if __name__=="__main__":
    main()
