#Class One 
class India:
    def capital(self):
        print('New Delhi is the capital of India')
    def language(self):
        print('Hindi is the most spoken language in India')
    def type(self):
        print('India is a developing country')
    def population(self):
        print('India is the second most populated country in the world')
    def currency(self):
        print('The currency of India is Rupee')
    def religion(self):
        print('India is a Hindu majority country')
    def prime_minister(self):
        print('Narendra Modi is the Prime Minister of India')
    def president(self):
        print('Ram Nath Kovind is the President of India')
    def national_animal(self):
        print('The national animal of India is Tiger')
    def national_bird(self):
        print('The national bird of India is Peacock')
    def national_sport(self):    
        print('The national sport of India is Hockey')

#Class Two

class England:
    def capital(self):
        print('London is the capital of England')
    def language(self):
        print('English is the most spoken language in England')
    def type(self):
        print('England is a developed country')
    def population(self):
        print('England is the 22nd most populated country in the world')
    def currency(self):
        print('The currency of England is Pound')
    def religion(self):
        print('England is a Christian majority country')
    def prime_minister(self):
        print('Boris Johnson is the Prime Minister of England')
    def king(self):
        print('Queen Elizabeth II is the Queen of England')
    def national_animal(self):
        print('The national animal of England is Lion')
    def national_bird(self):
        print('The national bird of England is Robin')
    def national_sport(self):    
        print('The national sport of England is Cricket')

#Class Three

class USA:
    def capital(self):
        print('Washington D.C. is the capital of USA')
    def language(self):
        print('English is the most spoken language in USA')
    def type(self):
        print('USA is a developed country')
    def population(self):
        print('USA is the 3rd most populated country in the world')
    def currency(self):
        print('The currency of USA is Dollar')
    def religion(self):
        print('USA is a Christian majority country')
    def president(self):
        print('Donald Trump is the President of USA')
    def national_animal(self):
        print('The national animal of USA is Bald Eagle')
    def national_bird(self):
        print('The national bird of USA is Bald Eagle')
    def national_sport(self):
        print('The national sport of USA is Baseball')

#Class Four

class Australia:
    def capital(self):
        print('Canberra is the capital of Australia')
    def language(self):
        print('English is the most spoken language in Australia')
    def type(self):
        print('Australia is a developed country')
    def population(self):
        print('Australia is the 56th most populated country in the world')
    def currency(self):
        print('The currency of Australia is Dollar')
    def religion(self):
        print('Australia is a Christian majority country')
    def prime_minister(self):
        print('Scott Morrison is the Prime Minister of Australia')
    def national_animal(self):
        print('The national animal of Australia is Kangaroo')
    def national_bird(self):
        print('The national bird of Australia is Emu')
    def national_sport(self):
        print('The national sport of Australia is Cricket')

#Class Five

class Canada:
    def capital(self):
        print('Ottawa is the capital of Canada')
    def language(self):
        print('English and French are the most spoken languages in Canada')
    def type(self):
        print('Canada is a developed country')
    def population(self):
        print('Canada is the 38th most populated country in the world')
    def currency(self):
        print('The currency of Canada is Dollar')
    def religion(self):
        print('Canada is a Christian majority country')
    def prime_minister(self):
        print('Justin Trudeau is the Prime Minister of Canada')
    def national_animal(self):
        print('The national animal of Canada is Beaver')
    def national_bird(self):
        print('The national bird of Canada is Common Loon')
    def national_sport(self):
        print('The national sport of Canada is Ice Hockey')

#Class Six

class Brazil:
    def capital(self):
        print('Brasília is the capital of Brazil')
    def language(self):
        print('Portuguese is the most spoken language in Brazil')
    def type(self):
        print('Brazil is a developing country')
    def population(self):
        print('Brazil is the 5th most populated country in the world')
    def currency(self):
        print('The currency of Brazil is Real')
    def religion(self):
        print('Brazil is a Christian majority country')
    def president(self):
        print('Jair Bolsonaro is the President of Brazil')
    def national_animal(self):
        print('The national animal of Brazil is Jaguar')
    def national_bird(self):
        print('The national bird of Brazil is Rufous-bellied Thrush')
    def national_sport(self):
        print('The national sport of Brazil is Football')

#Object Creation

India = India()
England = England()
USA = USA()
Australia = Australia()
Canada = Canada()
Brazil = Brazil()

#Common Interface

for country in (India, England, USA, Australia, Canada, Brazil):
    country.capital()
    country.language()
    country.type()
    country.population()
    country.currency()
    country.religion()
    country.national_animal()
    country.national_bird()
    country.national_sport()
    print('\n')
    