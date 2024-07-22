nepali = {
    'school' : 'विद्यालय',
    'flower' : 'फूल',
    'father' : 'बुबा',
    'mother' : 'आमा',
    'banana' : 'केरा',
    'egg' : 'अण्डा',
    'book' : 'पुस्तक',
    'apple' : 'स्याउ',
    'water' : 'पानी',
    'friend' : 'साथी',
    'house' : 'घर',
    'dog' : 'कुकुर',
    'cat' : 'बिरालो',
    'tree' : 'रुख',
    'sun' : 'सूर्य',
    'moon' : 'चन्द्रमा',
    'star' : 'तारा',
    'fire' : 'आगो',
    'river' : 'नदी',
    'mountain' : 'पहाड',
    'food' : 'खाना',
    'clothes' : 'लुगा',
    'road' : 'बाटो',
    'car' : 'गाडी',
    'bicycle' : 'साइकल'
}
print("\t\t\t\t\t welcome to Nepali Dictionary")
search = input("What do you want to translate: ").lower()
print(search)
print("The nepali translation of ", search , "is: ")
try:
    print(nepali[search])
except:
    print("Sorry there is no word like ", search , "in our dictionary.")