#singleton-->one single instance, orthat single ekta instance thakbe
#if you want a new instance, you will get the old one(already created)instance

class Singleton:
    __instance = None
    def __init__(self) -> None:
        if Singleton.__instance is None: #jodi "Singleton" er moddher instance "_instance" jodi "None" hoy tahole,
            Singleton.__instance=self #"Singleton" er "_instance" a self insert kore dibo
        else:#ar jodi "Singleton" er "instance" theke thake tobe nicher warning ashbe
            raise Exception('This is Singleton. Already have an instance, use that one by calling get_instance method')

    @staticmethod   
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    
first = Singleton.get_instance()
second = Singleton.get_instance()
third = Singleton.get_instance()
print(first)
print(second)
print(third)
# last = Singleton()