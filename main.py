from  Clasess.game import bcolors,person

magic = [{"name":"Ammu","cost":10,"dmg":60},
		 {"name": "Balu", "cost": 10, "dmg": 77},
		 {"name": "kumar", "cost": 10, "dmg": 85}]
player = person(460,65,60,34,magic)

enemy = person(1200, 69, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.HEADER + "An Enemy Attack" + bcolors.ENDC)
while running:
	print("==================================")
	player.choose_actions()

	choice = input("Choose Action:")
	index = int(choice) - 1

	if index == 0:
		dmg = player.genarete_random()
		enemy.take_damage(dmg)
		print("YOU aTTACKEd for",dmg, "points of damage. Enemy HP:",enemy.get_hp())

		enemy_choice = 1
		enemy_dmg = enemy.genarete_random()
		player.take_damage(enemy_dmg)
		print("Enemy Attack for ",enemy_dmg," Player Hp",player.get_hp())



