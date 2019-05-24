import requests
from flask import Flask 
from bs4 import BeautifulSoup

for i in range(5):
	category = str(input("Language? (E/H)"))
	if category=="E" or category=="e" or category=="English" or category=="english" or category=="eng" or category=="Eng" or category=="Hollywood" or category=="hollywood" or category=="Holly" or category=="holly":
		search = input("Enter song name =")
		search1 = search.replace(" ","+")

		url = "https://search.azlyrics.com/search.php?q=" + str(search1) 

		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html5lib")
		url2 = soup.find_all("table",{"class":"table table-condensed"})
		count = 0
		for i in url2:
			count = count +1
		if count==1:
			url2 = url2[0].find("td",{"class":"text-left visitedlyr"})
			r2 = requests.get(url2.a.get("href"))
			soup2 = BeautifulSoup(r2.content, "html5lib")
			data = soup2.find("div",{"class":"col-xs-12 col-lg-8 text-center"}).find_all("div")
			print('\n')
			print(data[6].text)		
		if count==2:
			url2 = url2[1].find("td",{"class":"text-left visitedlyr"})
			r2 = requests.get(url2.a.get("href"))
			soup2 = BeautifulSoup(r2.content, "html5lib")
			data = soup2.find("div",{"class":"col-xs-12 col-lg-8 text-center"}).find_all("div")
			print('\n')
			print(data[6].text)
		if count==3:
			url2 = url2[2].find("td",{"class":"text-left visitedlyr"})
			r2 = requests.get(url2.a.get("href"))
			soup2 = BeautifulSoup(r2.content, "html5lib")
			data = soup2.find("div",{"class":"col-xs-12 col-lg-8 text-center"}).find_all("div")
			print('\n')
			print(data[6].text)
		break
	elif category=="H" or category=="h" or category=="Hindi" or category=="hindi" or category=="hin" or category=="Hin" or category=="Bollywood" or category=="bollywood" or category=="Bolly" or category=="bolly":
		search = input("Enter song name =")
		search1 = search.replace(" ","+")

		url = "https://www.google.com/search?client=safari&rls=en&q=" + str(search1) + "+:+lyricsmint.com&ie=UTF-8&oe=UTF-8" 

		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html5lib")
		url2 = soup.find("h3",{"class":"r"}).a.get("href")
		abc = str(url2).replace("=","\n").replace(".html","\n")
		final = abc.split('\n')

		r2 = requests.get(final[1])
		soup2 = BeautifulSoup(r2.content, "html5lib")
		data = soup2.find("div",{"id":"lyric"}).find_all("p")
		print("\n")
		for t in data:
			print(str(t).replace("<p>","").replace("</p>","").replace("<br/>","\n").replace("<b>","").replace("</b>","").replace("<em>","").replace("</em>",""))
			print(" ")
		break
	else:
		print("No results found!")
