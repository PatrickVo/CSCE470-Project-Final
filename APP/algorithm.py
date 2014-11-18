list5 = []
list4 = []
list3 = []
list2 = []
list1 = []

def openfiles():
	star5 = open('star5.json', 'r')
	star4 = open('star4.json', 'r')
	star3 = open('star3.json', 'r')
	star2 = open('star2.json', 'r')
	star1 = open('star1.json', 'r')
	print 'reading star5'
	for line in star5:
		list5.append(line)
	print 'reading star4'
	for line in star4:
		list4.append(line)
	print 'reading star3'
	for line in star3:
		list3.append(line)
	print 'reading star2'
	for line in star2:
		list2.append(line)
	print 'reading star1'
	for line in star1:
		list1.append(line)
	
	
def similar(input):
    return 5.0

def lang_model(input):
    return 4.0

def classification(input):
    return 5.0

def get_rating(input):    
    score1 = similar(input)
    score2 = lang_model(input)
    score3 = classification(input)   
    rating = (score1+score2+score3)/3    
    return round(rating,0)
		
	
def main():
    input = " "
    openfiles()
    rating = get_rating(input)
    print rating
    

if __name__ == "__main__":
    main()