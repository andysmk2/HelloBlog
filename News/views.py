from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Good Night'
    h1 = 'HAHAHA'
    content = '''
    Barack Hussein Obama II (US Listeni/bəˈrɑːk huːˈseɪn oʊˈbɑːmə/;[2][3]
    born August 4, 1961) is an American politician serving as the 44th President
    of the United States. He is the first African American to hold the office, as
    well as the first president born outside of the continental United States. Born
    in Honolulu, Hawaii, Obama is a graduate of Columbia University and Harvard Law
    School, where he served as president of the Harvard Law Review. He was a community
     organizer in Chicago before earning his law degree. He worked as a civil rights
     attorney and taught constitutional law at University of Chicago Law School between
     1992 and 2004. He served three terms representing the 13th District in the Illinois
     Senate from 1997 to 2004, and ran unsuccessfully in the Democratic primary
     for the United States House of Representatives in 2000 against incumbent
     Bobby Rush.
    '''
    return render(request, 'index.html', locals())

