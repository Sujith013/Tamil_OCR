from Tamil_OCR import TamilImageDetection

Tamil = TamilImageDetection.TamilImageDetection("./test/7.png",0)

Tamil.lineExtract()
Tamil.wordExtract()
Tamil.characterExtract()
Tamil.recognize()
Tamil.transliterate()
Tamil.count_segregate()

"""
text = "தமிழில் என்னையும் வரவேற்கிறேன்! இது ஒரு சொந்த சொற்பொழிவுக்குரிய உரையாகும், ஆனால் அது பெரும் அழகினை உள்ளது. தமிழ் என்பது பழமையான மொழி மற்றும் தனிமையான எழுத்துக்கள் உடையது. நம் தமிழ் பேசும் பலரும் இந்த மொழியின் அழகைக் கண்டு மெய்ப்பொருளைக் கண்டுபிடிக்கின்றனர்."
text1 = "தமிழில் என்னையும் வரவேற்கிறேன்!"


Tamil = TamilImageDetection.TamilImageDetection(text,1)

Tamil.transliterate()            
Tamil.pronounce()
Tamil.count_segregate()
"""