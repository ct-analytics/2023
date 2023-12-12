import re

f = 'day 5/day5.txt'
seed_to_soil = {'flag':False, 'mapping':dict()}
soil_to_fertilizer = {'flag':False, 'mapping':dict()}
fertilizer_to_water = {'flag':False, 'mapping':dict()}
water_to_light = {'flag':False, 'mapping':dict()}
light_to_temperature = {'flag':False, 'mapping':dict()}
temperature_to_humidity = {'flag':False, 'mapping':dict()}
humidity_to_location = {'flag':False, 'mapping':dict()}


with open(f,'r') as almanac:
    for i, l in enumerate(almanac):
        # print(f"{i}: {l}")
        if l[0] == '\n':
            seed_to_soil['flag'] = False
            soil_to_fertilizer['flag'] = False
            fertilizer_to_water['flag'] = False
            water_to_light['flag'] = False
            light_to_temperature['flag'] = False
            temperature_to_humidity['flag'] = False
            humidity_to_location['flag'] = False
            continue

        if l[0:5] == "seeds":
            k = [int(x) for x in l[7:].split(' ')]
            v = [dict() for x in k]
            seeds = dict(zip(k,v))

        if l.strip() == 'seed-to-soil map:':
            seed_to_soil['flag'] = True
            # print('Seed to Soil mapping calculation...')
            continue

        if l.strip() == 'soil-to-fertilizer map:':
            soil_to_fertilizer['flag'] = True
            # print('Soil to Fertilizer mapping calculation...')
            continue

        if l.strip() == 'fertilizer-to-water map:':
            fertilizer_to_water['flag'] = True
            # print('Fertilizer to Water mapping calculation...')
            continue

        if l.strip() == 'water-to-light map:':
            water_to_light['flag'] = True
            # print('Water to Light mapping calculation...')
            continue

        if l.strip() == 'light-to-temperature map:':
            light_to_temperature['flag'] = True
            # print('Light to Temperature mapping calculation...')
            continue

        if l.strip() == 'temperature-to-humidity map:':
            temperature_to_humidity['flag'] = True
            # print('Temperature to Humidity mapping calculation...')
            continue

        if l.strip() == 'humidity-to-location map:':
            humidity_to_location['flag'] = True
            # print('Humidity to Location mapping calculation...')
            continue

        if seed_to_soil['flag']:
            # print(l.split(' '))
            seed_to_soil['map'] = [int(x) for x in l.split(' ')]
            
            for i in range(seed_to_soil['map'][2]):
                seed_to_soil['mapping'][seed_to_soil['map'][1]+i] = seed_to_soil['map'][0]+i

            # print('Seed to Soil mapping completed.')

        if soil_to_fertilizer['flag']:
            # print(l.split(' '))
            soil_to_fertilizer['map'] = [int(x) for x in l.split(' ')]
            
            for i in range(soil_to_fertilizer['map'][2]):
                soil_to_fertilizer['mapping'][soil_to_fertilizer['map'][1]+i] = soil_to_fertilizer['map'][0]+i

            # print('Soil to Fertilizer mapping completed.')

        if fertilizer_to_water['flag']:
            # print(l.split(' '))
            fertilizer_to_water['map'] = [int(x) for x in l.split(' ')]
            
            for i in range(fertilizer_to_water['map'][2]):
                fertilizer_to_water['mapping'][fertilizer_to_water['map'][1]+i] = fertilizer_to_water['map'][0]+i

            # print('Fertilizer to Water mapping completed.')
            
        if water_to_light['flag']:
            # print(l.split(' '))
            water_to_light['map'] = [int(x) for x in l.split(' ')]
            
            for i in range(water_to_light['map'][2]):
                water_to_light['mapping'][water_to_light['map'][1]+i] = water_to_light['map'][0]+i

            # print('Water to Light mapping completed.')

        if light_to_temperature['flag']:
            # print(l.split(' '))
            light_to_temperature['map'] = [int(x) for x in l.split(' ')]
            
            for i in range(light_to_temperature['map'][2]):
                light_to_temperature['mapping'][light_to_temperature['map'][1]+i] = light_to_temperature['map'][0]+i

            # print('Light to Temperature mapping completed.')

        if temperature_to_humidity['flag']:
            # print(l.split(' '))
            temperature_to_humidity['map'] = [int(x) for x in l.split(' ')]
            
            for i in range(temperature_to_humidity['map'][2]):
                temperature_to_humidity['mapping'][temperature_to_humidity['map'][1]+i] = temperature_to_humidity['map'][0]+i

            # print('Temperature to Humidity mapping completed.')

        if humidity_to_location['flag']:
            # print(l.split(' '))
            humidity_to_location['map'] = [int(x) for x in l.split(' ')]
            
            for i in range(humidity_to_location['map'][2]):
                humidity_to_location['mapping'][humidity_to_location['map'][1]+i] = humidity_to_location['map'][0]+i

            # print('Humidity to Location mapping completed.')
        
print(f"Seeds: {seeds}")
print(f"Seed to soil: {seed_to_soil}")
print(f"Soil to ferilizer: {soil_to_fertilizer}")
print(f"Fertilizer to water: {fertilizer_to_water}")
print(f"Water to light: {water_to_light}")
print(f"Light to temperature: {light_to_temperature}")
print(f"Temperature to humidity: {temperature_to_humidity}")
print(f"Humidity to location: {humidity_to_location}")

def custom_map(source,m):
    # print(source)
    # print(m)
    if source in m['mapping'].keys():
        destination = m['mapping'][source]
    else:
        destination = source

    return destination

for seed,d_ in seeds.items():
    seeds[seed]['soil'] = custom_map(seed,seed_to_soil)
    seeds[seed]['fertilizer'] = custom_map(seeds[seed]['soil'],soil_to_fertilizer)
    seeds[seed]['water'] = custom_map(seeds[seed]['fertilizer'],fertilizer_to_water)
    seeds[seed]['light'] = custom_map(seeds[seed]['water'],water_to_light)
    seeds[seed]['temperature'] = custom_map(seeds[seed]['light'],light_to_temperature)
    seeds[seed]['humidity'] = custom_map(seeds[seed]['temperature'],temperature_to_humidity)
    seeds[seed]['location'] = custom_map(seeds[seed]['humidity'],humidity_to_location)
    print("********************")
    print(f"Seed number {seed} corresponds to: \n\tSoil: {seeds[seed]['soil']}\n\tFertilizer: {seeds[seed]['fertilizer']}\n\tWater: {seeds[seed]['water']}\n\tLight: {seeds[seed]['light']}\n\tTemperature: {seeds[seed]['temperature']}\n\tHumidity: {seeds[seed]['humidity']}\n\tLocation: {seeds[seed]['location']}")

print("*****************************")
print(f"Lowest location number: {min(seed['location'] for n,seed in seeds.items())}")