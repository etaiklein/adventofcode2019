input = [
    ['R998','D934','L448','U443','R583','U398','R763','U98','R435','U984','L196','U410','L475','D163','R776','D796','R175','U640','R805','D857','R935','D768','L99','D75','R354','U551','L986','D592','R51','U648','L108','U8','R44','U298','L578','U710','R745','U60','L536','D62','R620','D454','L143','U407','R465','U606','L367','U107','L581','U900','R495','D12','R763','D244','R946','D424','R367','D696','L534','U452','R274','D942','L813','U336','L742','U134','R571','U703','R941','D532','L903','D833','L821','D577','L598','D83','R858','U798','L802','D852','R913','U309','L784','D235','L446','D571','R222','D714','R6','D379','R130','D313','R276','U632','L474','U11','L551','U257','R239','U218','R592','U901','L596','D367','L34','D397','R520','U547','L795','U192','R960','U77','L825','U954','R307','D399','R958','U239','R514','D863','L162','U266','R705','U731','R458','D514','R42','U314','R700','D651','L626','U555','R774','U773','R553','D107','L404','D100','R149','U845','L58','U674','R695','U255','R816','D884','R568','U618','R510','D566','L388','D947','L851','U127','L116','U143','L744','D361','L336','U903','L202','U683','R287','D174','L229','U371','L298','U839','L27','U462','R443','D39','R411','U788','L197','D160','L289','U840','L78','D262','R352','U83','R20','U109','R657','D225','R587','D968','R576','D791','R493','U805','R139','D699','R783','U140','L371','D170','L635','U257','R331','D311','R725','D970','R57','D986','L222','D760','L830','D960','L901','D367','R469','D560','L593','D940','L71','D384','R603','D689','R250','D859','L156','U499','L850','U166','R726','D210','L36','D584','R672','U47','L713','U985','R551','U22','L499','D575','R210','D829','L186','U340','R696','D939','L744','D46','L896','U467','L214','D71','R376','D379','L1','U870','R785','D779','L94','U723','L199','D185','R210','U937','R645','U25','R116','D821','R964','U959','R569','U496','R809','U112','R712','D315','L747','U754','L66','U614','L454','D945','R214','U965','L248','U702','L287','D863','R700','U768','R139','D242','R914','D818','R340','D60','L400','D924','R69','U73','L449','U393','L906'],
    ['L1005','D207','R487','U831','R81','U507','R701','D855','R978','U790','R856','U517','R693','D726','L857','D442','L13','U441','R184','D42','R27','D773','R797','D242','L689','D958','R981','D279','L635','D881','L907','U716','L90','U142','R618','D188','L725','U329','R717','D857','L583','U851','L140','U903','R363','U226','L413','U240','R772','U523','L860','U596','L861','D198','L44','U956','R862','U683','L542','U581','L346','U376','L568','D488','L254','D565','R480','D418','L567','U73','R397','U265','R632','U87','R803','D85','L100','D12','L989','U886','R279','U507','R274','U17','L36','U309','L189','D145','R50','U408','L451','D37','R930','D566','R96','U673','L302','U859','R814','U478','R218','U494','R177','D85','L376','U545','L106','U551','L469','U333','R685','U625','L933','U99','R817','D473','R412','D203','R912','U460','L527','D730','L193','U894','L256','D209','L868','D942','L8','U532','L270','U147','R919','U899','R256','U124','R204','D199','L170','D844','R974','U16','R722','U12','L470','D51','R821','U730','L498','U311','R587','D570','R981','D917','R440','D485','R179','U874','R26','D310','R302','U260','R446','D241','R694','D138','L400','D852','L194','U598','R73','U387','R660','D597','L803','D571','L956','D89','L394','U564','L287','U668','L9','D103','R152','D318','L215','U460','L870','U997','L595','D479','R262','U531','R609','U50','L165','U704','L826','D527','L901','D857','L914','U623','R432','D988','R562','D301','L277','U274','R39','D177','L827','U944','R64','U560','R801','D83','R388','U978','R387','U435','L759','U200','L760','U403','L218','D399','L178','U700','L75','U749','R85','U368','R538','U3','L172','D634','R518','D435','L542','U347','L745','U353','L178','D133','L475','U459','L522','U354','R184','U339','R845','D145','L44','U61','L603','U256','R534','U558','L998','D36','R42','U379','R813','D412','R878','D370','R629','U883','L490','D674','L863','U506','L961','D882','R436','D984','L229','D78','L779','D117','L674','U850','L494','D205','L988','D202','L368','U955','L662','U647','R774','D575','L753','D294','R131','U318','R873','U114','L30']
]

'''
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
'''

def up(index, current_wires_position):
    current_wires_position[index]['y'] += 1

def down(index, current_wires_position):
    current_wires_position[index]['y'] -= 1

def left(index, current_wires_position):
    current_wires_position[index]['x'] -= 1

def right(index, current_wires_position):
    current_wires_position[index]['x'] += 1

def default(index, current_wires_position):
    # TODO halt and catch fire
    print("halt and catch fire")
    return -1

direction_function_map = {
  'U': up,
  'D': down,
  'L': left,
  'R': right,
}

def distance(index, current_wires_position):
    return abs(current_wires_position[index]['x']) + abs(current_wires_position[index]['y'])

def compute_closest_intersections(input):
    closest_intersection_distance = float("inf")
    wire_path_map = {}
    current_wires_position = [{'x': 0, 'y': 0}, {'x': 0, 'y': 0}]

    for index in range(0, len(input)):
        for step in range(0, len(input[index])):
            direction = input[index][step][0]
            amplitude = int(input[index][step][1:])
            move_in_direction_function = direction_function_map.get(direction, default)

            for _ in range(0, amplitude):
                move_in_direction_function(index, current_wires_position)
                wire_key = '%s'%(current_wires_position[index])
                wire_val = wire_path_map.get(wire_key)
                if wire_val != None and wire_val.get('index') != index:
                    # print(wire_val)
                    closest_intersection_distance = min(wire_val['distance'], closest_intersection_distance)
                else:
                    wire_path_map[wire_key] = {
                        'distance': distance(index, current_wires_position),
                        'index': index
                    }

    # print(wire_path_map)
    # print("closest_intersection_distance", closest_intersection_distance)
    return closest_intersection_distance
            
assert compute_closest_intersections([['R8','U5','L5','D3'], ['U7','R6','D4','L4']]) == 6
assert compute_closest_intersections([['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]) == 159
assert compute_closest_intersections([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]) == 135
print(compute_closest_intersections(input))

'''
--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
'''

def compute_closest_steps(input):
    closest_intersection_steps = float("inf")
    wire_path_map = {}
    current_wires_position = [{'x': 0, 'y': 0}, {'x': 0, 'y': 0}]

    for index in range(0, len(input)):
        steps_so_far = 0
        for step in range(0, len(input[index])):
            direction = input[index][step][0]
            amplitude = int(input[index][step][1:])
            move_in_direction_function = direction_function_map.get(direction, default)

            for _ in range(0, amplitude):
                move_in_direction_function(index, current_wires_position)
                steps_so_far += 1
                wire_key = '%s'%(current_wires_position[index])
                wire_val = wire_path_map.get(wire_key)
                if wire_val != None and wire_val.get('index') != index:
                    # print(wire_val)
                    closest_intersection_steps = min(wire_val['steps'] + steps_so_far, closest_intersection_steps)
                else:
                    wire_path_map[wire_key] = {
                        'index': index,
                        'steps': steps_so_far
                    }

    # print(wire_path_map)
    # print("closest_intersection_steps", closest_intersection_steps)
    return closest_intersection_steps

assert compute_closest_steps([['R8','U5','L5','D3'], ['U7','R6','D4','L4']]) == 30
assert compute_closest_steps([['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]) == 610
assert compute_closest_steps([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]) == 410
print(compute_closest_steps(input))
