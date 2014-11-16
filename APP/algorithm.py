def similar(input):
    pass

def lang_model(input):
    pass

def classification(input):
    pass

def get_rating(input):    
    score1 = similar(input)
    score2 = lang_model(input)
    score3 = classification(input)   
    rating = (score1+score2+score3)/3    
    return round(rating,0)	

def main():
    input = " "
    
    rating = get_rating(input)
    print rating

if __name__ == "__main__":
    main()