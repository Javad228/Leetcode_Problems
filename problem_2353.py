from collections import defaultdict

class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.hashy_cuisine_foods = defaultdict(list)  # cuisine -> [foods]
        self.hashy_foods_ratings = {}    
        for i in range(len(foods)):
            self.hashy_foods_ratings[foods[i]] =ratings[i]
            self.hashy_cuisine_foods[cuisines[i]].append(foods[i])

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        foods = self.foods
        ratings = self.ratings
        self.hashy_foods_ratings[food] = newRating        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        foods = self.foods
        cuisines = self.cuisines 
        ratings = self.ratings
        self.hashy_cuisine_foods[cuisine].sort(
            key=lambda x: (-self.hashy_foods_ratings[x], x)
        )
        return self.hashy_cuisine_foods[cuisine][0]




def main():
    foods = ["kimchi","miso","sushi","moussaka","ramen","bulgogi"]
    cuisines = ["korean","japanese","japanese","greek","japanese","korean"] 
    ratings = [9,12,8,15,14,7]
    obj = FoodRatings(foods, cuisines, ratings)
    print(obj.highestRated("korean"))
    print(obj.highestRated("japanese"))
    print(obj.changeRating("sushi", 16))
    print(obj.highestRated("japanese"))
    print(obj.changeRating("ramen", 16))
    print(obj.highestRated("japanese"))



    
    


if __name__ == "__main__":
    main()
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)