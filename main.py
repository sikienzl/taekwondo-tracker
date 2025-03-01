from models import TaekwondoEntry, Chong, Combination, Kick, Punch

kick = Kick("Ap Chagi", None, "images/dollyo_chagi.jpg")
kick.save()

combo1 = Combination(
    name="Erste Kombination im Stand", 
    steps=[],
    description=None,
    image_path="images/combo.jpg"
)
combo1.save()

combo2 = Combination(
    name="Erste Kombination original", 
    steps=[],
    description=None,
    image_path="images/combo.jpg"
)
combo2.save()

punch = Punch("Jirugi", None, "images/jirugi.jpg")
punch.save()


chong1 = Chong(
    name="Chon-Ji",
    pseudonym="Himmel und Erde",
    stepscount=19,
    steps=[
        "Turn left into L-stance",
        "Right punch",
        "Step forward into front stance",
        "Left punch"
    ],
    description="Anfang und Ende",
    image_path="images/chon_ji.jpg"
)
chong1.save()

print("All entries:")
for entry in TaekwondoEntry.show_all():
    print(entry)


print("search for ap chagi':")
print(TaekwondoEntry.search("Ap Chagi"))

print("Delete punch 'Jirugi':")
TaekwondoEntry.delete("Jirugi")

print("Show all entries after delete:")
for entry in TaekwondoEntry.show_all():
    print(entry)
