Theatre_1 = {"Name":'Lviv',
             "Seats_Number":120,
             "Actors_1":["Andrew Kigan","Jhon Speelberg","Alan Mask","Neil Bambino"],
             "Play_1":["25/03/2018","Aida",80,"Andrew Kigan","Jhon Speelberg",60,"OK"],
             "Play_2":["26/03/2018","War",220,"Jhon Speelberg","Jhon Speelberg","Alan Mask","Neil Bambino",100,"OK"]
             }
Theatre_2 = {"Name":'Sokil',
             "Seats_Number":110,
             "Actors_2":["Julia Portman","Mary Lewis","Carla Mask","Neil Bambino","Natalie Queen"],
             "Play_3":["26/03/2018","Rigoletto",120,"Mary Lewis","Carla Mask","Neil Bambino","Natalie Queen",80,"OK"],
             "Play_4":["27/03/2018","Night Warriors",90,"Andrew Kigan","Julia Portman","Mary Lewis","Carla Mask",75,"NO"]
             }


print('Plays are:    ' + str(Theatre_1["Play_1"][1:2]) + ' ' + str(Theatre_1["Play_2"][1:2]) + ' ' + str(Theatre_2["Play_3"][1:2])  + ' ' + str(Theatre_2["Play_4"][1:2]))

print('Number of actors of Lviv Theatre is : ' + str(len(Theatre_1["Actors_1"])))


Other_play = {"Play_5":["29/03/2018","SomethingNew",90,"Andrew Kigan","Julia Portman","Carla Mask",74,"YES"]}
Theatre_2.update(Other_play)

free_tickets = Theatre_1.get("Play_1")[2] - Theatre_1.get("Play_1")[5]
print('Play  ' + str(Theatre_1["Play_1"][1:2]) + ', availiable tickets num = ' + str(free_tickets))

profit = Theatre_2.get("Play_3")[2] * Theatre_2.get("Play_3")[7]
print('Play  ' + str(Theatre_2["Play_3"][1:2]) + ', profit = ' + str(profit))


One_more_ticket = {"Play_4":["27/03/2018","Night Warriors",90,"Andrew Kigan","Julia Portman","Mary Lewis","Carla Mask",76,"NO"]}
Theatre_2.update(One_more_ticket)
print(Theatre_2)
