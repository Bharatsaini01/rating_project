def avg_rating(rating):
    avg_rating =0
    for i in rating:
        avg_rating += i[0]
    avg_rating = avg_rating // len(rating)
    return avg_rating

def rate_exp(avg_rating):
    if avg_rating == 1:
        return "Very Bad"
    elif avg_rating == 2:
        return "Bad"
    elif avg_rating == 3:
        return "Good"
    elif avg_rating == 4:
        return "Very Good"
    elif avg_rating == 5:
        return "Excellent"
    else:
        return "invalid input!"