import random

class RandomNumber:
    __rng_no = 0

    def __getno__(numb):

        RandNumber.__rng_no = random.randrange(numb)

        return RandNumber.__rng_no

    def get_random_no(numb):

        return RandNumber.__get_no(numb)


#obj = RandomNumber()

RandomNumber.get_random_no(8)
