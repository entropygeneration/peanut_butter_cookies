# Mrs. 3ntr0py's Peanut Butter Cookies

ingredients = [
	{
		"peanutButter": 0.5,
		"unitOfMeasurement": "cups"
	},
	{
		"butter": 0.5,
		"unitOfMeasurement": "cups"
	},
	{
		"sugar": 0.5,
		"unitOfMeasurement": "cups"
	},
	{
		"brownSugar": 0.5,
		"unitOfMeasurement": "cups"
	},
	{
		"allPurposeFlour": 1.25,
		"unitOfMeasurement": "cups"
	},
	{
		"vanilla": 0.5,
		"unitOfMeasurement": "teaspoon"
	},
	{
		"bakingSoda": 0.5,
		"unitOfMeasurement": "teaspoon"
	},
	{
		"salt": 0.25,
		"unitOfMeasurement": "teaspoon"
	},
	{
		"egg": 1
	}
]

class Mixer:
	def __init__(self, speed, beater, mixing_bowl):
		self.speed = speed
		self.beater = beater
		self.ingredients = ingredients
		self.mixing_bowl = mixing_bowl

class Baking_Sheet:
	def __init__(self, cookies, insulator):
		self.cookies = cookies
		self.insulator= insulator

class Oven:
	def __init__(self, baking_sheet, temperature):
		self.cookies = baking_sheet
		self.temperature= temperature

def stage_one(ingredients):
	mixing_bowl = []
	for item in ingredients:
		for ingredient, amount in item.items():
			if ingredient == 'peanutButter':
				mixing_bowl.append(amount)
			elif ingredient == 'butter':
				mixing_bowl.append(amount)
	
	beater = 'flat'
	count = 0 # time in seconds
	mixer = Mixer(0, beater, mixing_bowl)
	while count < 60:
		mixer.speed = 6
		count += 1
		if mixer.mixing_bowl == ['smooth']:
			break
	
	for item in ingredients:
		for ingredient, amount in item.items():
			if ingredient == 'sugar':
				mixer.mixing_bowl.append(amount)
			elif ingredient == 'vanilla':
				mixer.mixing_bowl.append(amount)
			elif ingredient == 'egg':
				cracked = amount - 'shell'
				mixer.mixing_bowl.append(cracked)

	count = 0
	while count < 60:
		mixer.speed = 4
		count += 1
		if mixer.mixing_bowl == ['smooth']:
			break

	return mixer.mixing_bowl

def stage_two(mixing_bowl, ingredients):
	
	beater = 'flat'
	count = 0 # time in seconds
	mixer = Mixer(0, beater, mixing_bowl)

	while count < 30:
		mixer.speed = 'stir'
		for item in ingredients:
			for ingredient, amount in item.items():
				if ingredient == 'brownSugar':
					mixing_bowl.append(amount)
				elif ingredient == 'allPurposeFlour':
					mixing_bowl.append(amount)
				elif ingredient == 'bakingSoda':
					mixing_bowl.append(amount)
				elif ingredient == 'sale':
					mixing_bowl.append(amount)
		count += 1

	if ingredients == None:
		while count < 30:
			mixer.speed = 2
			count += 1
	
	return mixer.mixing_bowl

def stage_three(dough):
	diameter = {"size": 1, "unitOfMeasurement": "inch"}
	utensil = 'fork'
	thickness = {"size": 0.25, "unitOfMeasurement": "inch"}
	cookies = []
	index = 0

	baking_sheet = Baking_Sheet(cookies, 'parchment paper')
	
	while dough:
		dough_ball = dough - diameter
		baking_sheet.cookies.append(dough_ball[index])
		index += 1

		if baking_sheet.cookies.append(dough_ball[index]) + utensil == thickness:
			pass
	
	return baking_sheet
		
def stage_four(panned_cookies):
	temperature = {"degrees": 375, "unitOfMeasurement": "fahrenheit"}
	count = 0 # time in seconds
	oven = Oven(None, temperature)

	if oven.temperature == 375:
		oven.baking_sheet = panned_cookies
	
	while count <= 43200: #12 minutes
		count += 1
	
	if oven.baking_sheet.cookies == 'golden_brown':
		removed_cookies = oven.baking_sheet
		return removed_cookies
	else:
		while count <= 10800: #3 minutes
			count += 1
		removed_cookies = oven.baking_sheet
		return removed_cookies
	
	

# init recipe
mixture = stage_one(ingredients)
finished_mixture = stage_two(mixture, ingredients)
panned_cookies = stage_three(finished_mixture)
finished_cookies = stage_four(panned_cookies)
