from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:

        if comfort_class < 1 or comfort_class > 10:
            raise ValueError("comfort_class must be between 1 and 10")
        if clean_mark < 0 or clean_mark > 10:
            raise ValueError("clean_mark must be between 0 and 10")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        if distance_from_city_center <= 0:
            distance_from_city_center = 1.0
        if clean_power < 0:
            clean_power = 1
        if average_rating < 1.0 or average_rating > 5.0:
            average_rating = 3.0
        if count_of_ratings < 0:
            count_of_ratings = 0

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = sum(
            self.wash_single_car(car)
            for car in cars
            if car.clean_mark < self.clean_power
        )
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if not isinstance(car, Car):
            raise ValueError("The argument must be a Car instance")

        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center, 1
        )

    def wash_single_car(self, car: Car) -> float:
        if not isinstance(car, Car):
            raise ValueError("The argument must be a Car instance")

        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

    def rate_service(self, new_rating: float) -> None:
        if not (1.0 <= new_rating <= 5.0):
            raise ValueError("new_rating must be between 1.0 and 5.0")

        self.count_of_ratings += 1
        self.average_rating = round(
            ((self.average_rating * (self.count_of_ratings - 1)) + new_rating)
            / self.count_of_ratings, 1
        )
