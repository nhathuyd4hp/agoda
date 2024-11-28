from agoda import Agoda

app = Agoda()

if __name__ == "__main__":
    # hotel = app.findHotel(38476987)    
    reviews = app.reviewHotel(38476987)
    print(reviews.keys())

